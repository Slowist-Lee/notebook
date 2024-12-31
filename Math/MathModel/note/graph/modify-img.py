import re

def replace_image_refs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 正则表达式匹配 Obsidian 图片引用格式
    pattern = r'!\[\[(.*?)\]\]'
    
    # 替换为新的 Markdown 图片引用格式，并删除路径前的“Pasted image”
    def replace(match):
        image_path = match.group(1)
        # 检查路径是否以“Pasted image”开头
        if image_path.startswith("Pasted image "):
            # 删除“Pasted image”前缀
            new_path = image_path.replace("Pasted image ", "")
            return f'![{new_path}]({new_path})'
        else:
            # 如果不是以“Pasted image”开头，直接返回原格式
            return f'![{image_path}]({image_path})'

    new_content = re.sub(pattern, replace, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 替换 'your-document.md' 为你的 Markdown 文件路径
replace_image_refs('D:\\MyRepository\\notebook-publish\\notebook\\docs\\cs\\pl\\Asm\\sum.md')