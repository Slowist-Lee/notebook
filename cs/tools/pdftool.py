import os
import sys
import argparse
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PIL import Image
import comtypes.client

def merge_pdfs(directory):
    """Merges all PDF files in the specified directory."""
    merger = PdfMerger()
    # Ensure the path exists and is a directory
    if not os.path.isdir(directory):
        print(f"Error: The provided path '{directory}' is not a valid directory.")
        return
        
    files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.pdf')])
    if not files:
        print(f"No PDF files found in the directory '{directory}'.")
        return

    print(f"Starting to merge PDF files in directory '{directory}'...")
    for filename in files:
        filepath = os.path.join(directory, filename)
        merger.append(filepath)
        print(f"  Adding file: {filename}")

    output_filename = os.path.join(directory, "merged_output.pdf")
    merger.write(output_filename)
    merger.close()
    print(f"\nPDF files have been merged into: {output_filename}")

def convert_word_to_pdf(files):
    """Converts a list of Word documents to PDF."""
    if not files:
        print("No Word documents found to convert.")
        return

    word = None
    try:
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False
        print("Microsoft Word application started, converting...")

        for in_file in files:
            in_file_abs = os.path.abspath(in_file)
            out_file_abs = os.path.abspath(os.path.splitext(in_file)[0] + '.pdf')
            try:
                doc = word.Documents.Open(in_file_abs)
                doc.SaveAs(out_file_abs, FileFormat=17)  # 17 is the code for PDF format
                doc.Close()
                print(f"  Converted: {os.path.basename(in_file)} -> {os.path.basename(out_file_abs)}")
            except Exception as e:
                print(f"  Conversion failed: {os.path.basename(in_file)}, error: {e}")
    finally:
        if word:
            word.Quit()
        print("\nWord document conversion task completed.")


def convert_pptx_to_pdf(files):
    """Converts a list of PowerPoint presentations to PDF."""
    if not files:
        print("No PowerPoint files found to convert.")
        return

    powerpoint = None
    try:
        powerpoint = comtypes.client.CreateObject('Powerpoint.Application')
        print("Microsoft PowerPoint application started, converting...")

        for in_file in files:
            in_file_abs = os.path.abspath(in_file)
            out_file_abs = os.path.abspath(os.path.splitext(in_file)[0] + '.pdf')
            try:
                presentation = powerpoint.Presentations.Open(in_file_abs, WithWindow=False)
                presentation.SaveAs(out_file_abs, 32)  # 32 is the code for PDF format
                presentation.Close()
                print(f"  Converted: {os.path.basename(in_file)} -> {os.path.basename(out_file_abs)}")
            except Exception as e:
                print(f"  Conversion failed: {os.path.basename(in_file)}, error: {e}")
    finally:
        if powerpoint:
            powerpoint.Quit()
        print("\nPowerPoint file conversion task completed.")

def convert_images_to_pdf(files):
    """Merges a list of image files into a single PDF file."""
    if not files:
        print("No image files found to convert.")
        return

    images = []
    for filename in files:
        try:
            img = Image.open(filename)
            # Ensure the image is in RGB mode to be compatible with PDF saving
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            images.append(img)
            print(f"  Adding image: {os.path.basename(filename)}")
        except Exception as e:
            print(f"  Failed to process image: {os.path.basename(filename)}, error: {e}")
    
    if not images:
        print("No valid images to process.")
        return

    # Save the output file in the current working directory
    output_filename = os.path.join(os.getcwd(), "images_output.pdf")
    images[0].save(output_filename, save_all=True, append_images=images[1:])
    print(f"\nAll images have been merged into PDF: {output_filename}")


def compress_pdf(files):
    """Compresses a list of PDF files."""
    if not files:
        print("No PDF files found to compress.")
        return

    for filepath in files:
        print(f"\nCompressing: {os.path.basename(filepath)}...")
        if not os.path.isfile(filepath):
            print(f"  Error: File '{filepath}' does not exist or is not a file, skipped.")
            continue

        try:
            reader = PdfReader(filepath)
            writer = PdfWriter()

            for page in reader.pages:
                page.compress_content_streams()  # Enable content stream compression
                writer.add_page(page)

            output_filename = os.path.splitext(filepath)[0] + '_compressed.pdf'
            with open(output_filename, 'wb') as f:
                writer.write(f)

            original_size = os.path.getsize(filepath) / 1024
            compressed_size = os.path.getsize(output_filename) / 1024

            print(f"  -> Output file: {os.path.basename(output_filename)}")
            print(f"  Original size: {original_size:.2f} KB | Compressed size: {compressed_size:.2f} KB")
            if original_size > 0:
                compression_rate = (1 - compressed_size / original_size) * 100
                print(f"  Compression rate: {compression_rate:.2f}%")
        except Exception as e:
            print(f"  Compression failed: {os.path.basename(filepath)}, error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="A versatile command-line tool for PDF and document processing.",
        epilog="Example: pdftool word2pdf my_doc.docx C:\\temp"
    )
    parser.add_argument('--version', action='version', version='1.0.0')
    parser.add_argument('action', nargs='?', choices=['merge', 'word2pdf', 'ppt2pdf', 'img2pdf', 'compress'], help="The action to perform.")
    parser.add_argument('paths', nargs='*', default=['.'], help="Paths to target files or directories. Defaults to the current directory if not provided.")

    args = parser.parse_args()
    
    if not args.action:
        parser.print_help()
        return

    action = args.action
    paths = args.paths

    # 'merge' action only handles a single directory
    if action == 'merge':
        if len(paths) > 1 or not os.path.isdir(paths[0]):
            print("Error: 'merge' action requires exactly one directory path.")
            return
        merge_pdfs(paths[0])
        return

    # Define valid file extensions for other actions
    file_extensions = {
        'word2pdf': ('.docx',),
        'ppt2pdf': ('.pptx',),
        'img2pdf': ('.png', '.jpg', '.jpeg', '.bmp', '.gif'),
        'compress': ('.pdf',)
    }
    valid_extensions = file_extensions[action]
    
    # Collect all valid files from the provided paths
    target_files = []
    for path in paths:
        if os.path.isdir(path):
            for filename in sorted(os.listdir(path)):
                if filename.lower().endswith(valid_extensions):
                    target_files.append(os.path.join(path, filename))
        elif os.path.isfile(path):
            if path.lower().endswith(valid_extensions):
                target_files.append(path)
            else:
                print(f"Warning: File '{path}' extension does not match action '{action}', ignored.")
        else:
            print(f"Warning: Path '{path}' is not a valid file or directory, ignored.")

    # Deduplicate and sort
    target_files = sorted(list(set(target_files)))

    if not target_files:
        print(f"No files matching the action '{action}' were found in the specified paths.")
        return

    # Call the corresponding function based on the action
    function_map = {
        'word2pdf': convert_word_to_pdf,
        'ppt2pdf': convert_pptx_to_pdf,
        'img2pdf': convert_images_to_pdf,
        'compress': compress_pdf,
    }
    function_map[action](target_files)


if __name__ == '__main__':
    # In Windows, initialize and uninitialize for COM operations
    if sys.platform == 'win32':
        comtypes.CoInitialize()
    try:
        main()
    finally:
        if sys.platform == 'win32':
            comtypes.CoUninitialize()