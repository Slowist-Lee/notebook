import re

file_name = "D:\\MyRepository\\notebook-publish\\notebook\\docs\\Math\\MathModel\\note\\program\\program.md"

# 读取文件内容
with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

# 定义替换模式
pattern = r'\$\$\n'

# 替换操作
new_content = re.sub(pattern, '$', content)

# 将修改后的内容写回文件
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(new_content)

print(f"文件 {file_name} 中的 $$\n 已被替换为 $")