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
操作符
`~`按位取反、`&` 按位与、`|` 按位或。

常用操作符及其优先级：

![](Pasted%20image%2020250114212906.png)


三输入与门：

```verilog
assign y = a & b & c; // 三输入与门
```

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
wire [9:0]     data_low = data[0:9] ;  
addr_temp[3:2] = addr[8:7] + 1'b1 ;
```
