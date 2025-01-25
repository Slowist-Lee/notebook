# Chap3 Arithmetic for Computer

### 3.1 Introduction

- `word`：由计算机的最大位宽来决定，但是平时还是按照32 bits(4 bytes)来计算
- 会出现 **溢出**(overflow)、负数

数字会有不同的意义：

![](image/Pasted%20image%2020250118093437.png)

同理：$1001_2$ 我们也无法知道他具体的意义：
- Unsigned： $1001_2=9_{10}$
- Signed：$1001_2=-1_{10} \text{   or   } -7_{10}$ （看表示方式）

![](image/Pasted%20image%2020250118093649.png)

常用: Two's Complement

8 bits 范围：-128 - 127

#### 数的类型：

![](image/Pasted%20image%2020250118094538.png)

### 3.2 Overflow

Overflow 出现情况：
- 加法
    - 不会溢出：两个符号不同的操作数相加
    - 可能会溢出：两个正数 / 两个负数的相加
- 减法
    - 不会溢出：两个符号相同的操作数相减
    - 可能会溢出：正数 - 负数 -> 负数？ 负数 - 正数 -> 正数？

- 次高位向高位是否进位 `c1`
- 高位向再高位是否进位 `c2`
- 若`c1`和`c2`异或后为1，则`of=1`

![](image/Pasted%20image%2020250118100149.png)

- Ignore
- 汇报给OS
- 汇报给应用程序

处理程序：
- ALU：发现overflow
- 抛出[异常](https://note.noughtq.top/system/co/4.html#exceptions) (exception) 或中断 (interrupt)，SEPC存储器中存储当前指令位置
- OS处理：
	- 纠正程序
	- 返回错误代码
	- 终止程序

### 3.3 ALU

### 3.3.1 `AND` & `OR` 功能

实现如下，Select 代表多路选择器

![](image/Pasted%20image%2020250118100827.png)

### 3.3.2 加法功能及1位ALU

使用半加器/全加器构建，
Sum=$A \oplus B \oplus C_{in}$ ，其中$C_{in}$是上一位的进位
Carry=... 其实就是三个输入里至少两个是1

全加器如下：

![](image/Pasted%20image%2020250118101306.png)


组合之后得到最基本的1位ALU！

- 其中 $\boxed{+}$ 表示全加器

![](image/Pasted%20image%2020250118101341.png)

### 3.3 在1位ALU中实现减法

有下列两种方法来实现减法：
- 给 b 取反，如下图
- 将第一次全加器的进位(CarryIn)设作1(0->1,1->10,由此相当于给b取反了x)

我们采用第一种方法，如下图所示：

![](image/Pasted%20image%2020250118101704.png)

### 3.4 在1位ALU中实现比较(comparison)

提前介绍一下`slt`指令(Set less than)：
- 三个操作数： `rd`是目标，最终结果放在`rd`内，`rs`,`rt`是两个操作数，对这两个操作数进行比较：If `rs` < `rt`, `rd`=1, else `rd`=0
	- 即`rs-rt`，看符号位来判断大小关系
- 若`rs-rt`产生溢出，仅会发生在两数异号的时候【解释见下】，但异号不会用这种办法判断。
	- 特殊处理
	- 或判断两者是否同号

【为什么只有两数异号才会溢出？】：如果两数同号，则结果的绝对值必然小于A/B的绝对值，故无法溢出

返回到一位ALU中如下，其中
Most significant bit: 最高位，符号位，作为Set位
Last significant bit: 最低位

![](image/Pasted%20image%2020250118112737.png)

Caution: Most和Last不能接在一起，符号位不能作为最低位

若Overflow的结果是1，则说明结果的`Less`位颠倒了，这时候需要将其作为Set位，返回`Less`，下面完整的ALU中表示的更清楚。

### 3.4 完整的ALU

- Overflow: 如下图所示，可以关注到此时将Set位返回到了最初的Less.

![](image/Pasted%20image%2020250118112819.png)

- Zero Detector: 
- 功能：现在的结果是否是0 (用于判断i\==j类似的命令)

- 最简单粗暴的方法是用一个很大的或非门，获取每一位上 ALU 的减法结果，若这个或非门的输出结果为 1，表明减法的结果为 0，即两个数相等
$$Zero=\overline{(Result63+result62+⋯+Result1+Result0)}$$
- 也许各位读者早就发现：`Binvert`的值和`CarryIn`的值始终是一致的。所以可以将这两个输入并在一起，叫做`Bnegate`

![](image/Pasted%20image%2020250118113028.png)

对应 ALU 的功能表：

![](image/Pasted%20image%2020250118122004.png)

为了简化电路的描绘，一般会用下面这个符号代表 ALU：

![](image/Pasted%20image%2020250118122013.png)

Verilog代码：
```verilog
module alu(A, B, ALU_operation, res, zero, overflow );
    input [31:0] A, B;
    input [2:0] ALU_operation;
    output [31:0] res;
    output zero, overflow ;
    wire [31:0] res_and,res_or,res_add,res_sub,res_nor,res_slt;
    reg [31:0] res;
    parameter one = 32'h00000001, zero_0 = 32'h00000000;
   assign res_and = A&B;
   assign res_or = A|B;
   assign res_add = A+B;
   assign res_sub = A-B;
   assign res_slt =(A < B) ? one : zero_0;
   always @ (A or B or ALU_operation) //@: 敏感列表，等式右边，会导致输出结果变化的，都需要放在敏感列表里?
   //可以写 always @ *，所有会引起我变化的
	  case (ALU_operation)
	  3'b000: res=res_and; 
	  3'b001: res=res_or; 
	  3'b010: res=res_add; 
	  3'b110: res=res_sub; 
	  3'b100: res=~(A | B);
	  3'b111: res=res_slt;
	  default: res=32'hx;
	  endcase
   assign zero = (res==0)? 1: 0;
endmodule
```

思考：和下面代码的区别：

```verilog
always @ (A or B or ALU_operation)
  case (ALU_operation)
		  3'b000: res=A&B; 
		  3'b001: res=A|B; 
		  3'b010: res=A+B; 
		  3'b110: res=A-B; 
          3'b100: res=~(A | B);
 3'b111: res=(A < B) ? one : zero_0;
    default: res=32'hx;
endcase
```