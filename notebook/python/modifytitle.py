import re

file_name = "D:\\MyRepository\\notebook-publish\\notebook\\docs\\cs\\misc\\ctf\\misc\\misc-lab1.md"

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
pattern=r'#+'

def replace_title(line):
    title = re.search(pattern,line).group(0)
    return f"#{title}"
new_content = []
for line in content.split('\n'):
    if re.search(pattern, line):
        replace=replace_title(line)
        line = re.sub(pattern, replace, line)
    new_content.append(line)

with open(file_name, 'w', encoding='utf-8') as file:
    file.write('\n'.join(new_content))

