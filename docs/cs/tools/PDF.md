# 基于命令行的PDF处理工具

我写了一个基于命令行的PDF处理工具（目前仅打包了exe），地址 [exe](https://github.com/Slowist-Lee/pdftool/blob/master/pdftool.exe) | [py](https://github.com/Slowist-Lee/pdftool/blob/master/pdftool.py)
（Python需要安装一下库文件，懒得写requirements了（x）

将pdftool.exe添加到Windows的环境路径，就可以在命令行调用pdftool了，这样就不用每次打开网页端的pdf处理工具处理了（x

因为写起来很简单，再加上平时比较喜欢命令行工作，就随便搞了一下，也没有特意去找有没有这样的工具

只写了 pdf 合并，word转pdf，pptx转pdf，图片转pdf，pdf压缩

具体功能：

```bash
PS C:\Users\slowist> pdftool -h
usage: pdftool.exe [-h] [--version] [{merge,word2pdf,ppt2pdf,img2pdf,compress}] [paths ...]

A versatile command-line tool for PDF and document processing.

positional arguments:
  {merge,word2pdf,ppt2pdf,img2pdf,compress}
                        The action to perform.
  paths                 Paths to target files or directories. Defaults to the current directory if not provided.

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

Example: pdftool word2pdf my_doc.docx C:\temp
```

有一个bug是文件名不能有空格。如果有空格的话，请用`"` 包裹，例如：

```bash
PS D:\MyRepository\study\Junior\ds\a1\作业答案> pdftool compress "算法设计与分析基础 第3版 Anany Levitin 潘彦答案.pdf"

Compressing: 算法设计与分析基础 第3版 Anany Levitin 潘彦答案.pdf...
  -> Output file: 算法设计与分析基础 第3版 Anany Levitin 潘彦答案_compressed.pdf
  Original size: 3560.40 KB | Compressed size: 3422.82 KB
  Compression rate: 3.86%
```

