# Verilog 笔记

Verilog -- 硬件描述语言
## 1. 基本操作符

```verilog
module example(
input a,
input b,
input c,
output y);

assign y= ~a & ~b & ~c | a & ~b & ~c | a & ~b & c;
endmodule
```

`module` / `endmodule`
表征模块的开始与结束。
`example`
模块名可由用户指定，可包含字母、数字及下划线，需以字母开头，区分大小写
`assign`
赋值操作关键字，该关键字后可跟一个赋值表达式，该关键字是实现组合逻辑操作的一种主要描述方式。
`input` / `output`
表征该信号的方向，除输入、输出外还有一种 `inout`（输入输出）型。


- 注释方式：
	- `//` 
	- `/*` `*/`
- 标识符：
	- 和C一样，字母、数字、`$`,`_`
	- 区分大小写


## 2. 电平逻辑

- 0：逻辑 0 或 "假"
- 1：逻辑 1 或 "真"
- x 或 X：未知
- z 或 Z：高阻

- 数值表示：前面可以指明位宽
	- 4bit: `4'b1011`
	- 32bit: `32'h3022_c0de`

也可以不指明位宽：

```verilog
counter = 'd100 ; //一般会根据编译器自动分频位宽，常见的为32bit
counter = 100 ;
counter = 32'h64 ;
```

字符串表示方法：verilog 将字符看作一系列单字节ASCII字符队列

```verilog
reg [0: 14*8-1]       str ;
initial begin
    str = "www.runoob.com";
end
```
## 3. 数据类型

### 3.1 `wire`

实际意义：wire 类型表示硬件单元之间的物理连线，由其连接的器件输出端连续驱动

以这个为例，可以内部用`wire`变量存储中间结果：

```verilog
module top_module (
    input wire p1a, p1b, p1c, p1d,  // 输入线 p1
    input wire p2a, p2b, p2c, p2d,  // 输入线 p2
    output wire p1y, p2y           // 输出线 p1y 和 p2y
);

wire p1c_out, p1b_out, p1f_out, p1e_out, p1d_out;
wire p2y_out;

// 第一组 XOR 门
assign p1c_out = p1a ^ p2a;
assign p1b_out = p1b ^ p2b;
assign p1f_out = p1c ^ p2c;
assign p1e_out = p1d ^ p2d;

// 第二组 XOR 门
assign p1d_out = p1c_out ^ p1b_out;
assign p2y_out = p1f_out ^ p1e_out;

// 输出逻辑
assign p1y = p1d_out ^ p2y_out;

endmodule
```

### 3.2 `reg` -- 寄存器

性质：持数据原有的值，直到被改写

```verilog
reg    clk_temp;
reg    flag1, flag2 ;
```

### 3.3 `vector`

当位宽大于 1 时，wire 或 reg 即可声明为向量的形式。

格式：`type [upper:lower] vector_name;`

```verilog
reg [3:0]      counter ;    //声明4bit位宽的寄存器counter  
wire [32-1:0]  gpio_data;   //声明32bit位宽的线型变量gpio_data  
wire [8:2]     addr ;       //声明7bit位宽的线型变量addr，位宽范围为8:2  
reg [0:31]     data ;       //声明32bit位宽的寄存器变量data, 最高有效位为0  
```


对于上面的向量，我们可以指定某一位或若干相邻位，作为其他逻辑使用。例如：

```verilog
wire [9:0]  data_low = data[0:9] ;  
addr_temp[3:2] = addr[8:7] + 1'b1 ;
```

**Verilog 还支持指定 bit 位后固定位宽的向量域选择访问。**

- `[bit+: width]` : 从起始 bit 位开始递增，位宽为 width。
- `[bit-: width]` : 从起始 bit 位开始递减，位宽为 width。

e.g.

```verilog
//下面 2 种赋值是等效的  
A = data1[31-: 8] ;  
A = data1[31:24] ;  
  
//下面 2 种赋值是等效的  
B = data1[0+ : 8] ;  
B = data1[0:7] ;
```

整数：`integer j`
实数：
```verilog
real        data1 ;  
integer     temp ;  
initial begin  
    data1 = 2e3 ;  
    data1 = 3.75 ;  
end  
   
initial begin  
    temp = data1 ; //temp 值的大小为3  
end
```

**时间（time）**

Verilog 使用特殊的时间寄存器 time 型变量，对仿真时间进行保存。其宽度一般为 64 bit，通过调用系统函数 $time 获取当前仿真时间。例如：

e.g.

```verilog
time       current_time ;  
initial begin  
       #100 ;  
       current_time = $time ; //current_time 的大小为 100  
end
```

数组：

```verilog
integer          flag [7:0] ; //8个整数组成的数组
reg  [3:0]       counter [3:0] ; //由4个4bit计数器组成的数组
wire [7:0]       addr_bus [3:0] ; //由4个8bit wire型变量组成的数组
wire             data_bit[7:0][5:0] ; //声明1bit wire型变量的二维数组
reg [31:0]       data_4d[11:0][3:0][3:0][255:0] ; //声明4维的32bit数据变量数组
```

- Vector取位的时候必须按原来定义的方向取

**存储器**: 存储器变量就是一种寄存器数组，可用来描述 RAM 或 ROM 的行为

```verilog
reg               membit[0:255] ;  //256bit的1bit存储器
reg  [7:0]        mem[0:1023] ;    //1Kbyte存储器，位宽8bit
mem[511] = 8'b0 ;                  //令第512个8bit的存储单元值为0
```

> Packed Array, 见 3.5

参数用来表示常量，用关键字 parameter 声明，只能赋值一次。例如：
```verilog
parameter      data_width = 10'd32 ;  
parameter      i=1, j=2, k=3 ;  
parameter      mem_size = data_width * 10 ;
```

字符串：

```verilog
reg [0: 14*8-1]       str ;
initial begin
    str = "run.runoob.com"; 
end
```

### 3.4 隐式网络

例如：

```verilog
wire [2:0] a, c;  // a 和 c 是 3 位向量
assign a = 3'b101; // a = 101
assign b = a;      // b 是隐式创建的 1 位 wire，实际值为 a[0] = 1
assign c = b;      // c 会得到 001（高位补 0），但开发者可能期望的是 101！
```

这个时候，`b`并没有得到过声明，如果写`assign b = a`, 会默认`b`是一个`1 bit`的`wire`.

可以使用【禁用隐式网络声明】：

```verilog
`default_nettype none
assign b = a; // 编译错误！b 未声明
```

### 3.5 Packed Array

```verilog
reg [7:0] mem [255:0];   // 256 unpacked elements, each of which is a 8-bit packed vector of reg.
reg mem2 [28:0];         // 29 unpacked elements, each of which is a 1-bit reg.
```

## 4. 表达式/操作符

Reference: https://www.runoob.com/w3cnote/verilog-expression.html

记一些常用的+写到过的内容。

`~`按位取反、`&` 按位与、`|` 按位或。

常用操作符及其优先级：

![](image/Pasted%20image%2020250114212906.png)


三输入与门：

```verilog
assign y = a & b & c; // 三输入与门
```

> HDLBits - Vectorgates

**逻辑或（Logical OR）** 的定义：`a ≠ 0` **或** `b ≠ 0` → `1`。

```verilog
module top_module(
	input [2:0] a, 
	input [2:0] b, 
	output [2:0] out_or_bitwise,
	output out_or_logical,
	output [5:0] out_not
);
	assign out_or_bitwise = a | b;
	assign out_or_logical = a || b;
	assign out_not[2:0] = ~a;	// Part-select on left side is o.
	assign out_not[5:3] = ~b;	//Assigning to [5:3] does not conflict with [2:0]
endmodule
```


### 拼接操作符`{a,b,c}`

例如：

```verilog
A = 4'b1010 ;
B = 1'b1 ;
Y1 = {B, A[3:2], A[0], 4'h3 };  //结果为Y1='b1100_0011
Y2 = {4{B}, 3'd4};  //结果为 Y2=7'b111_1100
Y3 = {32{1'b0}};  //结果为 Y3=32h0，常用作寄存器初始化时匹配位宽的赋初值
```


```verilog
{3'b111, 3'b000} => 6'b111000
{1'b1, 1'b0, 3'b101} => 5'b10101
{4'ha, 4'd10} => 8'b10101010     // 4'ha and 4'd10 are both 4'b1010 in binary
```

```verilog
input [15:0] in;
output [23:0] out;
assign {out[7:0], out[15:8]} = in;         // Swap two bytes. Right side and left side are both 16-bit vectors.
assign out[15:0] = {in[7:0], in[15:8]};    // This is the same thing.
assign out = {in[7:0], in[15:8]};       // This is different. The 16-bit vector on the right is extended to
                                        // match the 24-bit vector on the left, so out[23:16] are zero.
                                        // In the first two examples, out[23:16] are not assigned.
```



例如这道题：

>给定几个输入向量，将它们连接在一起，然后将它们拆分成几个输出向量。有六个 5 位输入向量：a、b、c、d、e 和 f，总共 30 位输入。有四个 8 位输出向量：w、x、y 和 z，总共 32 位输出。输出应该是输入向量的连接，后面跟着两个 1 位.

![](image/Pasted%20image%2020250202231354.png)

```verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );//

    // assign { ... } = { ... };
    assign {w[7:0],x[7:0],y[7:0],z[7:0]}={a[4:0],b[4:0],c[4:0],d[4:0],e[4:0],f[4:0],2'b11};
endmodule
```

例题2：逆向：

答案：

```verilog
module top_module (
	input [7:0] in,
	output [7:0] out
);
	
	assign {out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7]} = in;
endmodule
```

### 复制拼接运算符

`{num{vector}}`

```verilog
{5{1'b1}}           // 5'b11111 (or 5'd31 or 5'h1f)
{2{a,b,c}}          // The same as {a,b,c,a,b,c}
{3'd5, {2{3'd6}}}   // 9'b101_110_110. It's a concatenation of 101 with
                    // the second vector, which is two copies of 3'b110.
```

## 5. Verilog 模块与端口

定义：

```verilog
module module_name 
#(parameter_list)
(port_list) ; //端口列表
              Declarations_and_Statements ;
endmodule
```

![](image/Pasted%20image%2020250203122130.png)

- 如果和外部环境没有交互，则可以不用声明端口列表
- 端口类型有 3 种： 输入（input），输出（output）和双向端口（inout）

```verilog
//端口类型声明
input        DIN, OEN ;
input [1:0]  PULL ;  //(00,01-dispull, 11-pullup, 10-pulldown)
inout        PAD ;   //pad value
output       DOUT ;  //pad load when pad configured as input

//端口数据类型声明
wire         DIN, OEN ;
wire  [1:0]  PULL ;
wire         PAD ;
reg          DOUT ;
```


`mod_a`已经写好了之后:

```verilog
module mod_a ( input in1, input in2, output out );
    // Module body
endmodule
```

之后可以创造`mod_a`示例，并给新的名字，比如`inst1`

示例：

示意图：

![](image/Pasted%20image%2020250203124350.png)


by name
```verilog
module top_module ( input a, input b, output out );
    mod_a inst1(.in1(a),.in2(b),.out(out));
endmodule
```

或者：
by position

```verilog
module top_module ( input a, input b, output out );
    mod_a inst1(a,b,out);
endmodule
```

## 6. Verilog 结构语句

### 6.1 `initial`

格式：

```verilog
initial
	begin
	语句1;
	语句2;
	语句3;
	...
	语句n;
end
```

例1：进行初始化

```verilog
initial
	begin
		areg=0; //初始化寄存器areg
		for(index=0;index<size;index=index+1)
			memory[index]=0; //初始化一个memory
end
```

例2：用`initial`语句生成激励波形作为电路的测试仿真信号

### 6.2 `always`

always通过@来控制执⾏时机:
```verilog
always @(*) // 在任何情况下都执⾏always块，常⽤于书写组合逻辑 
always @(a) // 当a的值发⽣改变的时候，执⾏ 
always @(a or b) // 当a或b的值发⽣改变的时候，执⾏ 
always @(posedge a or negedge b) // 当遇到a的正边沿或b的负边沿时，执⾏ always // 不带@，执⾏完⼀次块内内容后，就再执⾏⼀次，常⽤于tesebench的clk信号改变
```

正边沿：信号从low到high 
负边沿：信号从high到low

- 数字电路是由导线连接的逻辑门组成，因此任何电路都可以表示为module和assign语句的某种组合
- 过程块中可以使用更丰富的语句(比如if-then,case)，但不能包含连续赋值

#### 对比：`assign`和`always`

1. `assign out1 = a & b | c ^ d;`

- **类型**: 这是一个连续赋值语句。
- **行为**: `out1`会**持续**根据`a`, `b`, `c`, `d`的值更新。只要`a`, `b`, `c`, `d`中的任何一个发生变化，`out1`会立即重新计算并更新。 
- **用途**: 通常用于描述简单的组合逻辑，适合用于单个信号的赋值。

2. `always @(*) out2 = a & b | c ^ d;`

- **类型**: 这是一个过程赋值语句，放在`always`块中。
- **行为**: `always @(*)`表示每当块内的敏感信号（即`a`, `b`, `c`, `d`）发生变化时，块内的代码会执行。`out2`会在这些信号变化时重新计算并更新。
- **用途**: 通常用于描述更复杂的组合逻辑或时序逻辑。`always @(*)`可以包含多条语句，适合用于需要多个操作或条件判断的情况。

对于硬件综合来说，存在两种always块：

```verilog
组合逻辑：always @(*)
时序逻辑：always @(posedge clk)
```

时序always块也会像组合always块一样生成一系列的组合电路，但同时在组合逻辑的输出生成了一组触发器(或寄存器)。该输出**在下一个时钟上升沿(posedge clk)后可见，而不是之前的立即可见。**

**阻塞性赋值和非阻塞性赋值**

在Verilog中有以下三种赋值方法：

```verilog
连续赋值(assign x=y;)：不能在过程块内使用；
过程阻塞性赋值(x=y;)：只能在过程块中使用；
过程非阻塞性复制(x<=y)：只能在过程块内使用。
```

在组合always块中，使用阻塞性赋值。在时序always块中，使用非阻塞性赋值。具体为什么对设计硬件用处不大，还需要理解Verilog模拟器如何跟踪事件(译者注：的确是这样，记住**组合用阻塞性，时序用非阻塞性**就可以了)。不遵循此规则会导致极难发现非确定性错误，并且在仿真和综合出来的硬件之间存在差异。

练习：

![](image/Pasted%20image%2020250207103230.png)

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff   );
    assign out_assign = a ^ b;
    always @(*) out_always_comb = a ^ b;
    always @(posedge clk) out_always_ff = a ^ b;
endmodule
```

波形：

![](image/Pasted%20image%2020250207103820.png)

#### 多路选择器：

- `if`: if语句通常对应一个二选一多路复用器，如果条件为真，则选择其中一个输入作为输出；反之如果条件为假，则选择另一个输入所谓输出。if语句必须在过程块内使用。

一般格式（下列两个组合逻辑电路等价）：

```verilog
always @(*) begin
    if (condition) begin
        out = x;
    end
    else begin
        out = y;
    end
end
```

```verilog
assign out = (condition) ? x : y;
```

**常见的错误来源：如何避免引入锁存器**

在设计电路时，必须首先具体考虑电路：

1、我想实现一个逻辑门；

2、我想实现一个具有输入并产生输出的组合逻辑块；

3、我想实现一组组合逻辑，紧接着一组触发器。

不要上来就写代码，这样往往与你想象的电路相差很远。

![](https://pic4.zhimg.com/v2-642f210c8d559b9f6d8b312c35068d6f_1440w.jpg)

```verilog
if (cpu_overheated) then shut_off_computer = 1;
if (~arrived) then keep_driving = ~gas_tank_empty;
```

除了你指定的情况以外，会发生些什么，答案是什么也不会发生，输出保持不变。而这往往就导致了电路的错误，所以说语法正确的代码不一定能产生合理的电路(组合逻辑+触发器)。

输出保持不变，这就意味着电路需要记住当前状态，从而产生锁存器。组合逻辑(比如逻辑门)不能记住任何状态。

```tcl
Warning (10240): ... inferring latch(es)
```

上述这类警告通常情况下代表错误，除非锁存器是故意生成的。组合电路输出必须在所有输入的情况下都有值。这意味着必须需要[else子句](https://zhida.zhihu.com/search?content_id=101607417&content_type=Article&match_order=1&q=else%E5%AD%90%E5%8F%A5&zhida_source=entity)或着输出默认值。

casez的用途：它在比较中将具有值z的位视为无关项(即输入01都会匹配到)。

例如：下面的代码就是上一个联系中的4输入优先编码器：

```verilog
always @(*) begin
    casez (in[3:0])
        4'bzzz1: out = 0;   // in[3:1]输入什么都可以
        4'bzz1z: out = 1;
        4'bz1zz: out = 2;
        4'b1zzz: out = 3;
        default: out = 0;
    endcase
end
```

case项是按顺序检查的(实际上，它更像是生成一个巨大的真值表然后生成超大的门)。注意有输入(例如，4'b1111)匹配多个case项。选择第一个匹配(因此4'b1111匹配第一个case项，out = 0)。

还有一个类似的casex，将输入的x和z都视为无关。不认为casex比casez有什么特别的好处。(作者个人感觉没必要用casex，z和x状态的问题涉及电路的基本知识)

符号"?" 是z的同义词，所以2'bz0与2'b?0相同。

#### 设置默认值

为避免生成了不必要的锁存器，必须在所有条件下为所有的输出赋值(参见**Problem 31: If statement latches(Always if2)**)。这可能会多打很多字，使你的代码变得冗长。 一个简单的方法是在case语句之前为输出分配一个“默认值”：

```verilog
always @(*) begin
    up = 1'b0; down = 1'b0; left = 1'b0; right = 1'b0;
    case (scancode)
        ... // Set to 1 as necessary.
    endcase
end
```

除非case语句覆盖赋值，否则这种代码样式可确保在所有可能的情况下输出0。 这也意味着case的default项变得不必要。

## Verilog Language Features

### 1. 三元运算符

基本用法：

```verilog
condition ? if_true : if_false
```

可以在一行代码上实现一个MUX：

```verilog
(0 ? 3 : 5)     // 输出是5，因为条件"0"始终是false的
(sel ? b : a)   // 一个二选一MUX，通过sel的值选择a或者b

always @(posedge clk)         // 一个T触发器
  q <= toggle ? ~q : q;

always @(*)                   // 一输入的状态转换逻辑
    A: next = w ? B : A;
    B: next = w ? A : B;
  endcase

assign out = ena ? q : 1'bz;  // 三态缓冲器

((sel[1:0] == 2'h0) ? a :     // 一个三选一MUX
 (sel[1:0] == 2'h1) ? b :
                      c )
```

### 2. 归约运算符

归约运算符(Reduction Operators)可以对向量的每一位位进行AND，OR和XOR，产生一位输出：

```text
&a [3：0] // AND:a[3]&a[2]&a[1]&a [0]相当于(a[3：0]== 4'hf)
|b [3：0] // OR: b[3]|b[2]|b[1]|b [0]相当于(b[3：0]!= 4'h0)
^c [2：0] // XOR:c[2]^c[1]^c[0]
```

这些是只有一个操作数的一元运算符(类似于NOT运算符!和~)。也可以将这些本节课的运算符的输出反相以创建NAND，NOR和XNOR门，例如(`~&d[7:0]`)。

奇偶校验器，数字电路的初学者来说，对教材上给出的奇偶检验器的计算方式可能有些迷惑，什么是奇校验，什么是偶校验。

奇偶校验是检验传输数据中1的个数，当然有奇数有偶数，，这时候就需要用我们的校验位了，通过检验位将传输1的个数变成奇数就是奇校验，变成偶数就是偶校验

### 3. `for`循环在`always`语句中的使用

```verilog
module top_module(
    input [99:0] in,
    output [99:0] out
);
    integer i;
    always @(*) begin
        for(i=0;i<100;i=i+1)
            out[i]=in[99-i];
    end
endmodule
```

```verilog
module top_module( 
    input [254:0] in,
    output [7:0] out );
    integer i;  
    always @(*) begin
        out = {8{1'b0}}; 
        for(i=0;i<255;i=i+1)begin
            if (in[i]==1)
                out = out + 1'b1;
            else
                out = out + 1'b0;
        end
    end
endmodule
```

踩的坑：

1. 向量的加法不需要写加法器。写`out=out+1'b1`就可以了。
2. `assign`和`always`，组合用阻塞性，时序用非阻塞性，两个之间是不互通的。如果在`always`的外面写`assign out = {8{1'b0}}`的话，是没法进去，还是有latches.
3. 注意latches. `else`这一支别漏。

### 4. 好多实例化 —— 利用`generate`来实例化 | 实例化数组

题目要求：

>通过实例化100个全加器来实现一个100bit的二进制加法器。该加法器有两个100bit的输入和cin，输出为sum与cout。为了鼓励大家使用实例化来完成电路设计，我们同时需要输出每个全加器的cout。 故cout[99]标志着全加器的最终进位。

