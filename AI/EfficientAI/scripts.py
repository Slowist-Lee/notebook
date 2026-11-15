import re
import os
import shutil
from tqdm import tqdm
import fitz  # PyMuPDF

def check_dependencies():
    """
    检查必要的依赖
    """
    try:
        import fitz  # PyMuPDF
        from tqdm import tqdm
        print("✔ 所有必要的库都已安装 (PyMuPDF, tqdm)")
        return True
    except ImportError as e:
        print(f"❌ 缺少必要的库: {e}")
        print("请运行以下命令安装所需库:")
        print("python -m pip install PyMuPDF tqdm")
        return False

def get_pdf_page_count(pdf_path):
    """
    获取PDF文件的页数
    :param pdf_path: PDF文件路径
    :return: PDF页数，如果出错返回0
    """
    try:
        doc = fitz.open(pdf_path)
        page_count = doc.page_count
        doc.close()
        return page_count
    except Exception as e:
        print(f"❌ 无法读取PDF文件: {e}")
        return 0

def get_existing_image_count(image_folder):
    """
    获取图片文件夹中已有的图片数量
    :param image_folder: 图片文件夹路径
    :return: 已有的图片数量
    """
    if not os.path.exists(image_folder):
        return 0
    
    count = 0
    for file in os.listdir(image_folder):
        if file.startswith('page_') and file.endswith('.png'):
            try:
                page_num = int(file.split('_')[1].split('.')[0])
                count = max(count, page_num)
            except (IndexError, ValueError):
                pass
    return count

def pdf_to_images(pdf_path, image_folder):
    """
    将PDF文件转换为图片
    :param pdf_path: PDF文件路径
    :param image_folder: 输出图片文件夹
    :return: 生成的图片文件列表
    """
    # 确保输出文件夹存在
    if not os.path.exists(image_folder):
        try:
            os.makedirs(image_folder)
            print(f"✔ 已创建输出文件夹: {image_folder}")
        except OSError as e:
            print(f"❌ 无法创建输出文件夹 '{image_folder}'。请检查路径和权限: {e}")
            return []
    
    try:
        # 打开PDF文件
        print(f"⚙️ 开始转换PDF: {pdf_path}")
        doc = fitz.open(pdf_path)
        page_count = doc.page_count
        print(f"文件已打开，共 {page_count} 页")
        
        # 保存图片
        image_files = []
        for i in tqdm(range(page_count), desc="生成图片"):
            page = doc[i]
            # 渲染页面为图片，设置较高的清晰度
            pix = page.get_pixmap(dpi=300)
            # 保存图片
            image_path = os.path.join(image_folder, f"page_{i+1}.png")
            pix.save(image_path)
            image_files.append(image_path)
        
        # 关闭PDF文件
        doc.close()
        print(f"✔ PDF转换完成，共生成 {len(image_files)} 张图片到 {image_folder}")
        return image_files
    except fitz.FileNotFoundError:
        print(f"❌ PDF文件不存在或无法访问: {pdf_path}")
        return []
    except Exception as e:
        print(f"❌ PDF转换失败: {e}")
        return []

def backup_markdown(md_path):
    """
    备份Markdown文件
    :param md_path: Markdown文件路径
    :return: 备份文件路径，如果失败返回None
    """
    try:
        backup_path = md_path + '.bak'
        shutil.copy2(md_path, backup_path)
        print(f"✔ 已备份原文件: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"❌ 备份文件失败: {e}")
        return None

def process_markdown(md_path, image_folder):
    """
    处理Markdown文件，替换图片占位符
    :param md_path: Markdown文件路径
    :param image_folder: 图片文件夹路径
    """
    print(f"⚙️ 开始处理Markdown文件: {md_path}")
    
    # 获取图片文件夹的相对路径
    md_dir = os.path.dirname(md_path)
    image_folder_name = os.path.basename(image_folder)
    image_folder_relative = os.path.relpath(image_folder, md_dir).replace(os.sep, '/')
    
    # 定义匹配逻辑（用户提供）
    def add_offset(match):
        page_num = int(match.group(1))
        new_page = page_num
        return f"![alt text]({image_folder_relative}/page_{new_page}.png)"

    # 正则表达式：匹配 [这里插入第 xxx 页图片]
    pattern = r"\[这里插入第\s*(\d+)\s*页图片\]"

    try:
        # 读取原始文件内容
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✔ 已读取Markdown文件")

        # 执行全局替换
        new_content = re.sub(pattern, add_offset, content)
        
        # 统计替换数量
        total_placeholders = len(re.findall(pattern, content))
        replaced_placeholders = len(re.findall(pattern, new_content))
        replacements_made = total_placeholders - replaced_placeholders
        print(f"ℹ️ 找到 {total_placeholders} 个图片占位符，替换了 {replacements_made} 个")

        # 将结果写回原文件
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✔ 已成功更新Markdown文件: {md_path}")
    
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{md_path}'")
    except Exception as e:
        print(f"❌ 处理Markdown文件失败: {e}")

def main():
    print("===== PDF转图片并更新Markdown脚本 =====")
    
    # 检查依赖
    if not check_dependencies():
        print("脚本已终止，请先安装所需依赖。")
        return
    
    # 配置参数
    input_pdf_name = "Lec12-Transformers-and-LLM.pdf"
    input_md = "2.md"
    
    # 构建完整路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, input_pdf_name)
    md_path = os.path.join(base_dir, input_md)
    
    # 创建与PDF名称强关联的images文件夹
    pdf_name_without_ext = os.path.splitext(input_pdf_name)[0]
    image_folder = os.path.join(base_dir, f"images_{pdf_name_without_ext}")
    
    print("\n===== 检查文件路径 =====")
    # 检查PDF文件是否存在
    if not os.path.exists(pdf_path):
        print(f"❌ 错误: PDF文件不存在。请检查路径是否正确，或文件是否存在。")
        print(f"  当前PDF路径: '{pdf_path}'")
        return
    else:
        print(f"✔ PDF文件存在: '{pdf_path}'")
    
    # 检查Markdown文件是否存在
    if not os.path.exists(md_path):
        print(f"❌ 错误: Markdown文件不存在。请检查路径是否正确，或文件是否存在。")
        print(f"  当前Markdown路径: '{md_path}'")
        return
    else:
        print(f"✔ Markdown文件存在: '{md_path}'")
    
    print(f"\n===== 图片文件夹设置 =====")
    print(f"图片文件夹路径: '{image_folder}'")
    
    # 获取PDF页数
    pdf_page_count = get_pdf_page_count(pdf_path)
    if pdf_page_count == 0:
        print("❌ 无法获取PDF页数，脚本终止。")
        return
    print(f"PDF总页数: {pdf_page_count}")
    
    # 检查图片是否已生成
    existing_image_count = get_existing_image_count(image_folder)
    print(f"现有图片数量: {existing_image_count}")
    
    # 转换PDF为图片（如果需要）
    if existing_image_count >= pdf_page_count:
        print(f"✔ 图片已完整生成，跳过转换步骤")
    else:
        print(f"\n===== 开始转换PDF为图片 =====")
        image_files = pdf_to_images(pdf_path, image_folder)
        if not image_files:
            print("❌ PDF转换失败，脚本终止。")
            return
    
    # 备份原始Markdown文件
    print(f"\n===== 备份Markdown文件 =====")
    backup_path = backup_markdown(md_path)
    if not backup_path:
        print("❌ 备份失败，脚本终止。")
        return
    
    # 处理Markdown文件
    print(f"\n===== 处理Markdown文件 =====")
    process_markdown(md_path, image_folder)
    
    print("\n===== 任务完成！ =====")

if __name__ == "__main__":
    main()
