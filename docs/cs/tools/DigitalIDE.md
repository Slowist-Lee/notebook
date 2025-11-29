# 面向信电的Digital IDE使用（简记）

> [!warning]
> 由于本人才刚刚开始熟悉这个插件，本文档更多是备忘性质的。以及本文档正在完善中……

## 一、什么是Digital IDE
 
 Digital IDE（[文档：https://nc-ai.cn/](https://nc-ai.cn/)） 是一个在Vscode开发Verilog等的插件，集成了语法高亮、显示Netlist、波形仿真，以及和第三方工具（Verilator/Vivado/Modelsim/iverilog）集成等功能。笔者有幸在刚刚接触verilog的时候就知道了这个插件，之后从来没有听过老师的话打开modelsim或者vivado或者notepad来写verilog代码……

 笔者认为Digital IDE最优秀的功能可能还是语法高亮，这里简单截一张图来展示一下（更多请查看原文档）：

 ![|375](Pasted%20image%2020251129161903.png)

 此外，Netlist和仿真的效果也还不错，虽然依赖于三方的iverilog。对于笔者这样的菜鸟来说，相比于信电实验课提供的**超卡**并且**License经常过期**的Modelsim，笔者在折腾了半天iverilog之后使用digital IDE有了非常棒的仿真体验，32位全加器的波形几乎是**立刻**生成的，至少在写写小工程的时候已经很不错了。

 网表效果如下图：

 ![](Pasted%20image%2020251129162543.png)

仿真：

![](Pasted%20image%2020251129162627.png)

其中鼠标选中的工具栏可以方便的切换时钟边沿，很适用于逐个时刻检查生成的信号是否正确（个人认为也比Modelsim正常多了（x

不过这个插件的文档感觉写的真的一般，所以笔者就写了这篇文章来备忘（
## 二、使用

> [!warning]
> 正如前文所说，我也刚刚掌握这个插件，所以有些具体细节还不太会用，之后会用了就会补上

### 2.1 安装

在Vscode插件市场搜索Digital IDE即可，安装就会有语法高亮，不用仿真和生成网表功能其实够用了。

### 2.2 生成网表

生成网表可能就需要简单的配置。

1. 先找到vivado的安装路径，通常为vivado/版本号/bin/ 。注意此时你可能会发现这里没有vivado.exe，但这就是对的，因为好像vivado是通过某个批处理文件`bat`去调用目录里面的exe

下面有两种方法可以设置
1. 将vivado安装路径添加到系统环境变量（Windows直接搜环境变量->打开->右下角环境变量小框->选中Path->编辑->新建->粘贴vivado的安装路径，之后一路点确定到底）

![|475](Pasted%20image%2020251129162944.png)

![|475](Pasted%20image%2020251129163237.png)


2. vscode settings -> 搜索栏搜索digital-ide vivado，将刚刚得到的路径复制进来

![](Pasted%20image%2020251129162826.png)

设置完之后，Digital IDE支持CodeLens功能，可以通过点击模块上方的Netlist得到网表，大概在这个位置：

![|375](Pasted%20image%2020251129163614.png)

> [!tip]
> 不过上面这个testbench其实是没法生成Netlist的，嘻嘻。

### 2.3 生成波形文件

#### 2.3.1 安装 iverilog

生成波形文件相对之前要更更复杂一点，为了使用digital-ide的Simulate，最好安装iverilog（可能有其他方案，但笔者还没探索过），文档：[https://steveicarus.github.io/iverilog/](https://steveicarus.github.io/iverilog/) 但很可惜，iverilog也是一个文档写的相当好品的软件，笔者翻了半天Installation Guide都没找到怎么在windows里安装 🤡

这里linux用户直接按照官方给的方案安装就可以，win用户记得不要用文档里提的minGW编译，原因也确实写在文档里，iverilog有好多win不支持的feature，折腾了半天make会报错。翻了一下这里有一个22年的安装包：[https://bleyer.org/icarus/](https://bleyer.org/icarus/) ，可以直接下载，**记住在勾选的时候要把MinGW和gtkwave都选上**，最后一步勾选添加到path，否则好像装的iverilog没法正常仿真（鬼知道为什么）。

#### 2.3.2 建立Digital IDE 工程

Digital IDE这个插件本身似乎有一套默认的工程，但是由于伟大的信电学院倡导**工程管理**，我们需要对此进行一些“勤奋乐观”的改造。不过这里还是提一嘴，我觉得把code和testbench分在两个文件夹是合理的，至于最后交上去会不会因此扣分就不晓得了。

首先先在根目录Ctrl+Shift+P创立工程，

![|475](Pasted%20image%2020251129164551.png)

默认会在根目录有一个.vscode/property.json文件。根据信电学院实验课的要求，大家需要把代码放在`src/`下，Modelsim仿真文件放在`sim/`下，vivado放在`vivado`下，这和默认还是略有差别。因此我们进行改造：

```json
{
    "toolChain": "xilinx",
    "toolVersion" : "2017.4",
    "prjName": {
        "PL": "Test",
        "PS": "template"
    },
    "arch" : {
        "structure" : "custom",
        "prjPath" : "",
        "hardware" : {
            "src"  : "src/code/",
            "sim"  : "src/testbench/",
            "data" : ""
        },
        "software" : {
            "src"  : "",
            "data" : ""
        }
    },
    "IP_REPO" : [],
	"soc": {
		"core": "none"
	},
    "device": "none"
}
```

大致要点如下：

1. `structure` 要改成custom，否则就会按照默认的工程配置，导致无法识别你的文件
2. 初学硬件编程时文件大多数放在`hardware`下面，`software`可以为空。其中`"src"  : "src/code/"`意味着你的模块文件都放在`src/code/`下面，`src/testbench/`意味着你的tb文件都放在testbench下面


在设置后reload window或者利用Digital IDE的refresh（control+shift+p之后查找命令），并将文件放入对应位置。文件目录应该大致如下（我还没进行过modelsim和vivado仿真，所以还没建sim目录）：


![|450](Pasted%20image%2020251129165149.png)

![|211](Pasted%20image%2020251129165217.png)

#### 2.3.3 仿真

最后还有一个小Tip，在testbench的initial begin之后需要添加两句

```verilog
initial begin
$dumpfile("./icarus/adder_32bits_tb.vcd"); // 1. 设置波形文件的名称
$dumpvars(0, adder_32bits_tb);   // 2. 指定要记录的信号范围
//...existing code...
```

以确保信号都被加入到波形仿真中。

启动仿真有两种方法，第一种还是通过我们之前说的Codelense, 

![|229](Pasted%20image%2020251129165458.png)

第二种就是点开插件的界面，此时sim下会有你写的各个testbench，此时点瓢虫（是吗x）图案也可以开始仿真，如图：

![|325](Pasted%20image%2020251129165635.png)

## 三、在Digital IDE内建立vivado工程

看起来好烦，还没试过（略略略
## 四、打包上交

TODO. 
打算使用Git进行版本管理 & gitignore+git archieve 进行上交

现在根据目前的情况写了一版简单的gitignore，因为作业还没写完没有检查过可不可以（x

```gitignore
.vscode/
data/
icarus/
netlist/
*.vcd
*.view
```

