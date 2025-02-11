import re

file_name = "D:\\MyRepository\\notebook-publish\\notebook\\docs\\Math\\MathModel\\note\\combination-optimize\\note.md"

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'\$\$(.*?)\$\$'

def replace_math(match):
    math = match.group(1)
    return f"$$\n{math}\n$$\n"

# 直接用 re.sub 进行全局替换
new_content = re.sub(pattern, replace_math, content)

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(new_content)

