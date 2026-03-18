document.addEventListener('DOMContentLoaded', () => {
    // 检查是否在 TPO 格式化工具页面
    if (document.querySelector('.tpo-formatter-container')) {

        const paragraphInput = document.getElementById('paragraph-input');
        const questionInput = document.getElementById('question-input');
        const answerInput = document.getElementById('answer-input');
        const generateBtn = document.getElementById('generate-btn');
        const copyBtn = document.getElementById('copy-btn');
        const outputText = document.getElementById('output-text');

        // 核心功能：生成格式化文本
        function generateFormattedText() {
            const paragraph = paragraphInput.value.trim();
            const question = questionInput.value.trim();
            const answer = answerInput.value.trim();

            if (!paragraph && !question && !answer) {
                outputText.value = "请至少输入一项内容...";
                return;
            }

            // 辅助函数，为多行文本的每一行前添加 "> "
            const formatBlock = (text) => {
                if (!text) return '>';
                return '> ' + text.replace(/\n/g, '\n> ');
            };

            // 构建最终的格式化文本
            const formattedText = 
`> [!note]+ Paragraph
${formatBlock(paragraph)}

> [!question]+ Question
${formatBlock(question)}

> [!check]- Answer
${formatBlock(answer)}`;

            // 将结果放入输出文本框
            outputText.value = formattedText;
        }

        // 核心功能：复制到剪贴板
        function copyToClipboard() {
            // 如果输出框是空的，先生成一次内容
            if (outputText.value === "" || outputText.value === "请至少输入一项内容...") {
                generateFormattedText();
                // 如果生成后依然为空，则提示并退出
                if (!paragraphInput.value.trim() && !questionInput.value.trim() && !answerInput.value.trim()) {
                    alert('请输入内容后再复制！');
                    return;
                }
            }
            
            navigator.clipboard.writeText(outputText.value).then(() => {
                const originalText = copyBtn.textContent;
                copyBtn.textContent = '复制成功!';
                setTimeout(() => {
                    copyBtn.textContent = originalText;
                }, 2000);
            }).catch(err => {
                console.error('复制失败: ', err);
                alert('复制失败，请检查浏览器权限或手动复制。');
            });
        }

        // 绑定事件监听器
        generateBtn.addEventListener('click', generateFormattedText);
        copyBtn.addEventListener('click', copyToClipboard);
    }
});

// --- PDF 打印工具的逻辑 ---
document.addEventListener('DOMContentLoaded', () => {
    // 检查是否在 PDF 打印工具页面
    if (document.querySelector('.printer-container')) {

        const markdownInput = document.getElementById('markdown-input');
        const printBtn = document.getElementById('print-btn');
        const printContentArea = document.getElementById('print-content-area');

        printBtn.addEventListener('click', () => {
            const markdownText = markdownInput.value;

            if (!markdownText.trim()) {
                alert('请输入需要打印的内容！');
                return;
            }

            // 检查 marked.js 是否加载成功
            if (typeof marked === 'undefined') {
                alert('Markdown 渲染库加载失败，请检查网络或配置。');
                return;
            }

            // 1. 将用户输入的 Markdown 转换为 HTML
            const htmlContent = marked.parse(markdownText);
            
            // 2. 将转换后的 HTML 放入专门用于打印的容器中
            printContentArea.innerHTML = htmlContent;

            // 3. 调用浏览器的打印功能
            window.print();
        });
    }
});
