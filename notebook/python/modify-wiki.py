import re

def replace_markdown_links(text):
    # 使用 re.sub 进行替换，将 ![[xxx]] 替换为 ![](xxx)，并将 xxx 中的空格替换为 %20
    def replace_space(match):
        # 获取匹配的内容（即 xxx）
        content = match.group(1)
        # 将内容中的空格替换为 %20
        content = content.replace(" ", "%20")
        # 返回替换后的格式 ![](xxx)
        return f'![](image/{content})'
    
    # 使用 re.sub 并传入替换函数
    replaced_text = re.sub(pattern, replace_space, text)
    
    return replaced_text


file_name = 'D:\\MyRepository\\notebook-publish\\notebook\\docs\\cs\\misc\\ctf\\misc\\misc-lab1.md'

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

new_content = []
for line in content.split('\n'):
    pattern = r'!\[\[(.*?)\]\]'
    if re.search(pattern, line):
        replace= replace_markdown_links(line)
        line = re.sub(pattern, replace, line)
    new_content.append(line)

with open(file_name, 'w', encoding='utf-8') as file:
    file.write('\n'.join(new_content))
