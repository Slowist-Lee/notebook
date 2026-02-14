import re
import os

def process_markdown(input_file, output_file):
    # 定义匹配逻辑
    def add_offset(match):
        page_num = int(match.group(1))
        new_page = page_num + 74
        return f"![alt text](images/page_{new_page}.png)"

    # 正则表达式：匹配 [这里插入第 xxx 页图片]
    pattern = r"\[这里插入第\s*(\d+)\s*页图片\]"

    try:
        # 1. 读取原始文件内容
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 2. 执行全局替换
        new_content = re.sub(pattern, add_offset, content)

        # 3. 将结果写入新文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ 处理完成！已生成: {output_file}")
    
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_file}'")

# --- 使用设置 ---
input_filename = "1.md"  # 这里改成你的文件名
output_filename = "2.md"

process_markdown(input_filename, output_filename)