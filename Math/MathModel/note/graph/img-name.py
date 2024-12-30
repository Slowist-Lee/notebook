import os

# 指定你的文件夹路径
folder_path = 'D:\\MyRepository\\notebook-publish\\notebook\\docs\\Math\\MathModel\\note\\graph\\'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查文件是否以.jpg结尾
    if filename.endswith(".png"):
        # 构建完整的文件路径
        old_file = os.path.join(folder_path, filename)
        # 检查文件名是否以"Pasted image"开头
        if filename.startswith("Pasted image "):
            # 构建新的文件名，移除"Pasted image"部分
            new_filename = filename.replace("Pasted image ", "")
            # 构建新的文件路径
            new_file = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed "{old_file}" to "{new_file}"')

print("All files have been renamed.")