# Misc

!!! abstract
    第二部分笔记.

## Part.1 文件系统基础

1. 不同文件系统的组织方式：
	-  MS
2. 文件：二进制数据
	- 文件名、大小、时间→不是文件的数据的部分
3. 文件类型
	- 扩展名
    - .jpg .webp .txt .docx ...
    - 是文件名的一部分，可以随意修改
    - （在一些桌面环境下）  
        决定了打开文件的默认程序
	- **通过文件内容来识别文件类型**（√）
	- file 命令：根据文件内容判断文件类型
	- 不同文件类型有不同的**魔数**

4. 可以用二进制查看文件与分析来看**魔数**/文件头

VSCode, 装完插件，ctrl+shift+p 输hex

![](image/Pasted%20image%2020240709184107.png)

魔数：

![](image/Pasted%20image%2020240709184219.png)

- 通过 file 命令进行文件类型的检测
- 可以使用 exiftool 读取部分类型文件的元信息

5. 文件结束的标记：

![](image/Pasted%20image%2020240709184601.png)

- 大部分文件类型都有一个标记文件内容结束的标志
    - 比如 PNG 的 IEND 块、JPEG 的 EOI 标志（FF D9）
- 所以一般在文件末尾添加其他字节时，不会影响原文件本身的用途
    - 因此有些隐写是将数据隐藏在文件末尾达到的

- 在linux中，你可以`cat cover.jpg secret.zip` 
- 图片可以正常显示，但是文件内容里会发现一份`secret.zip`
- binwalk 可以检测叠加的文件
- 附加文件的分离
    - binwalk 或 foremost 识别并分离
    - `dd if=_<src>_ of=_<dst>_ bs=1 skip=_<offset>_ `手动分离

## Part.2 图像隐写基础技术

### 1. 内容基本隐写

- 文件末尾添加数据
    - exiftool 识别短数据，或者十六进制编辑器直接观察
    - binwalk 识别叠加文件，foremost 提取
    - 图像末尾叠加一个压缩包，就是所谓的“图种”
        - 修改后缀名可能可以解压（部分解压软件会忽略前面的图像）
	        - 1.jpg改成1.zip, 尝试解压
        - 其实不如直接分离
- 直接利用元信息
    - exiftool 即可读取
e.g.
创建了`a.zip`
`cat a.png a.zip`
图片不变
然后解压，会把前面的图片数据扔掉


### 2. 色彩空间

色彩空间（sRGB、Adobe RGB、Display P3 等）是一个相对非常复杂的概念，而且是针对显示的，我们不详细介绍

我们注重于表示颜色的数据上，一般称为色彩模式（color mode）：

- 二值图像（bitonal）：每个像素只有两种颜色，如黑白
- 灰度图像（grayscale）：每个像素有多种灰度，如 256 级灰度
- RGB(A)：3(+1) 通道，表示 RGB 三种颜色，A 表示透明度通道
- CMYK：青 cyan、品红 magenta、黄 yellow、黑 black 四种颜色混合
- HSV：色调 hue、饱和度 saturation、明度 value
- HSL：色调 hue、饱和度 saturation、亮度 lightness
- （不常见）YCbCr：亮度 luminance、蓝色色度 blue chroma、红色色度 red chroma
- （不常见）LAB：亮度 lightness、绿红色度 A、蓝黄色度 B
- ...

#### 2.1 LSB 隐写

least significant bit

- 人眼对于微小的颜色变化不敏感
    - 对于 8 bit 的颜色值，最低位的变化不会被察觉
    - 可以随意修改最低位，而不影响图像的显示效果
- LSB 隐写将颜色通道的最低位用来编码信息
    - 图像：stegsolve / CyberChef View Bit Plane
    - 数据：stegsolve / CyberChef Extract LSB / zsteg / PIL
- PIL 图像处理基础 [官方文档](https://pillow.readthedocs.io/en/stable/)
- 基本用法
    - from PIL import Image 导入和图像读写处理有关的 Image 类
    - img = Image.open(file_name) 打开图像
    - img.show() 显示图像；img.save(file_name) 保存图像
    - img.size 图像大小，img.mode 图像模式
    - img.convert(mode) 转换图像模式
    - img.getpixel((x, y)) 获取像素点颜色
    - img.putpixel((x, y), color) 设置像素点颜色
    - np.array(img) 将图像转换为 numpy 数组
- 具体图像模式以及转换
    - '1'：黑白二值（0/255）；'L'：灰度（8 bit），'l'：32 bit 灰度
        - `L = 0.299 R + 0.587 G + 0.114 B`
    - 'P'：8bit 调色盘，获取的像素值是调色盘索引
    - 'RGB'、'RGBA'
    - 'CMYK'：转换时有色差，CMY = 255 - RGB，K = 0
    - 'YCbCr'、'LAB'、'HSV' 等，转换时有复杂公式（可能出现新的隐写）
- PIL 其他模块用途
    - ImageDraw 用于绘制图像、绘制图形
    - ImageChops 用于图像通道的逻辑运算
    - ImageOps 用于图像整体的运算一类
    - ImageFilter 用于图像的滤波处理

## Part.3 图像格式介绍

- 图像信息：宽高、色彩模式、色彩空间等
    - EXIF 信息：拍摄设备、拍摄时间、GPS 信息等
- 像素数据：每个像素的颜色信息；二值、灰度、RGB、CMYK、调色盘等
    - 对于标准 RGB 图像，每个像素需要 24 bits
    - 对于一张 1080p 图像，需要 6.22 MB，4K 则需要 24.88 MB
    - BMP 格式
- 压力给到了图像格式的压缩算法
    - bmp -> PNG 无损，**JPEG 有损**
    - GIF 有损且只支持 256 色
    - 新兴格式如 HEIF、WebP、AVIF 等
- JPEG 文件格式：JPEG 使用分段的结构来进行存储，各段以 0xFF 开头，后接一个字节表示类型：
	- FFD8（SOI）：文件开始
	- FFE0（APP0）：应用程序数据段，包含文件格式信息（上图没有）
	- FFE1（APP1）：应用程序数据段，包含 EXIF 信息（上图没有）
	- FFDB（DQT）：量化表数据
	- FFC0（SOF）：帧数据，包含图像宽高、色彩模式等信息
	- FFC4（DHT）：huffman 表数据
	- FFDA（SOS）：扫描数据，包含数据的扫描方式，huffman 表的使用方式等
	- FFD9（EOI）：文件结束

![](image/Pasted%20image%2020240709191116.png)

- PNG
	-  文件头 89 50 4E 47 0D 0A 1A 0A | .PNG....
	- 采用分块的方式存储数据
	    - 每块的结构都是 **4 字节长度 + 4 字节类型（比如：IHDR) + 数据 + 4 字节 CRC 校验**
	    - 四个标准数据块：IHDR、PLTE、IDAT、IEND
	    - 其他辅助数据块：eXIf、tEXt、zTXt、tIME、gAMA……
	        - eXIf 元信息，tIME 修改时间，tEXt 文本，zTXt 压缩文本
	- 四种标准数据块：
	
	- IHDR：包含图像基本信息，必须位于开头
	    - 4 字节宽度 + 4 字节高度
	    - 1 字节位深度：1、2、4、8、16
	    - 1 字节颜色类型：0 灰度，2 RGB，3 索引，4 灰度透明，6 RGB 透明
	    - 1 字节压缩方式，1 字节滤波方式，均固定为 0
	    - 1 字节扫描方式：0 非隔行扫描，1 Adam7 隔行扫描
	- PLTE：调色板，只对索引颜色类型有用,预先定义好颜色，在后面用编号进行引用
	- IDAT：图像数据，可以有多个，每个数据块最大 $2^{31}-1$  字节
	- IEND：文件结束标志，必须位于最后，内容固定
	    - PNG 标准不允许 IEND 之后有数据块

所以看到misc_lab0:

![](image/Pasted%20image%2020240709192247.png)

看到`IEND B` 之后都是我们要的`flag`

## Part.4 隐写进阶技术

### 图像大小修改

- PNG 图像按行进行像素数据的压缩，以及存储 / 读取
- 当解码时已经达到了 IHDR 中规定的大小就会结束
- 因此题目可能会故意修改 IHDR 中的高度数据，使之显示不全
- 恢复的话更改高度即可，同时注意 crc 校验码，否则可能报错
    - binascii.crc32(data)，data 为从 IHDR 开始的数据

![](https://courses.zjusec.com/slides/misc-lec2/misc-lec2/modify_size.webp)

### 需要原图的图像隐写

有些情况下的图像隐写需要原图才能解密，这时第一步一般是 OSINT 搜索原图

- 使用识图工具进行搜索
- 一般需要搜原图的题题目描述会带有来源暗示之类的
- 多注意搜到的图像大小、质量，确保是真正的原图

接下来利用原图和隐写图像的差异进行分析

- 图像像素异或观察差异
    - PIL 手动处理 / ImageChops.difference
    - stegsolve image combiner
- 盲水印系列
    - 给了打水印的代码的话直接尝试根据代码逆推即可
    - 没有给代码的可能就是常见的现有盲水印工具
        - [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)


### 音频文件隐写

MP3 → 一般听得出来

- mp3：有损压缩
    - 具体格式不多介绍，遇到了基本上也就是声音本身的隐写
- wav：无损无压缩（waveform）
    - 直接存储的是音频的波形数据，可操作性更高
    - 文件结构也是分 chunk 的，有 RIFF、fmt、data 等
    - 编码音频数据的 sample 也可以进行 LSB 隐写
- flac：无损压缩，如果出现可能考虑转换为 wav
- 使用 Python 的 soundfile / librosa 库进行音频处理

一般使用 Adobe Audition 打开来进行进一步的分析

- 频谱隐写是观察音频的频谱图，可能会有部分信息经过了调整
    - 比如如下攻防世界的一道题目 Hear with your eyes
    - Audacity
- 也可以用音频叠加来解决
	- 如果可以找到原音频，或提供了原音频，可以进行比较
	- 方法是在 Audition 中创建多轨会话
	    - 将两个音频拖入两个轨道
	    - 效果 > 匹配响度，将两条音轨的响度匹配
	    - 点进其中一条音轨，效果 > 反相，将波形上下颠倒
	    - 两条音轨匹配上波形之后播放 / 混音，就能听到差异了

## Part.5 一些其他的 misc 类型题目

- ZIP 也使用分段的方式存储数据
    - 本地文件记录 50 4B 03 04，可以有多个
    - 中央目录记录 50 4B 01 02，可以有多个
    - 中央目录结束 50 4B 05 06
- 在中央目录记录中有一个字段记录加密方式
    - 如果不为 0 表示有加密
- 其他字段，如最小版本
    - 可能修改为一个不合法的值，无法用解压软件解压

防止zip解压的方式：
- 改一个hex值之后，可能就需要密码打开了
- 改需要解压的版本号

### 沙箱逃逸&PPC

- 沙箱：做了某些限制的隔离环境
    - 例如 Docker，或一个沙箱程序，如 rbash
- Python 解释器也可以作为一个沙箱
    - 通过限制模块、限制函数、代码审计等方式
- 沙箱逃逸就是在沙箱中执行代码，获取到沙箱外的权限
    - Python 的 os 及 importlib 模块是常见的逃逸点