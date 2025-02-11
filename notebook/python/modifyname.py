import re

file_name = 'D:\\MyRepository\\notebook-publish\\notebook\\docs\\cs\\misc\\ctf\\web\\note-1.md'

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
pattern=r'!\[(.*?)\]\((.*?)\)'

def replace_image_refs(line):
    image_path = (re.search(pattern,line)).group(2)
    new_path = f"image/{image_path}"
    return f'![]({new_path})'
new_content = []
for line in content.split('\n'):
    if re.search(pattern, line):
        replace=replace_image_refs(line)
        line = re.sub(pattern, replace, line)
    new_content.append(line)

with open(file_name, 'w', encoding='utf-8') as file:
    file.write('\n'.join(new_content))

