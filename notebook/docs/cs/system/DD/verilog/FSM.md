# 状态机
## 1. 时序逻辑电路知识

### 1.1 同步时序逻辑电路分析

![](image/Pasted%20image%2020250209210111.png)

前置知识：触发器的特性方程：

![](image/Pasted%20image%2020250209210308.png)

例子：

![](image/Pasted%20image%2020250209210349.png)

- CLK统一：同步时序逻辑电路

1. 驱动方程：

![](image/image/Pasted%20image%2020250209210527.png)

下面进行描述：

1. 状态转换表和状态转换图

![](image/Pasted%20image%2020250209210900.png)

需要标出时钟信号的顺序，上面的一行的Q1\* 正好是上面的Q1

n个触发器正好有$2^n$个

![](image/Pasted%20image%2020250209211449.png)

![](image/Pasted%20image%2020250209212219.png)

![](image/Pasted%20image%2020250209212232.png)

$Q_2 Q_1$ 在A的条件下，看Y

$2^n$ 个 圆圈， $2^{n+m}$个箭头

## 设计方法

Step 1 逻辑抽象
![](image/Pasted%20image%2020250209230445.png)


![](image/Pasted%20image%2020250209230750.png)

![](image/Pasted%20image%2020250209231258.png)

![](image/Pasted%20image%2020250209231340.png)

例题：设计带有进位输出端的十三进制计数器

1. 逻辑抽象：
	- 13进制：13个状态
	- 需要进位输出信号
	- 默认加法计数器，是Moore型，不需要输入信号
2. 十三个状态，4个触发器；
	- 自然二进制的0000~1100，0-12来表实状态

![](image/Pasted%20image%2020250209231638.png)

1. 状态转换图转换为基本方程组 -- 列成卡诺图的形式

![](image/Pasted%20image%2020250209231736.png)

理解：输出变量Q\* 由输入变量Q和X决定

![](image/Pasted%20image%2020250209232149.png)

![](image/Pasted%20image%2020250209232223.png)

![](image/Pasted%20image%2020250209232317.png)

## Verilog 写 FSM

教程： https://www.runoob.com/w3cnote/verilog-fsm.html
**Problem 118 Simple FSM1 / Fsm1**

**牛刀小试**

![](image/https://pic2.zhimg.com/v2-f6d79d3a401ea64802b2d149dc4bc467_1440w.jpg)

图中是一个有两个状态的摩尔型状态机。有一个输入信号与一个输出信号。本题中需要实现图中的状态机，注意复位后状态为 B，复位采用[异步复位](https://zhida.zhihu.com/search?content_id=104232083&content_type=Article&match_order=1&q=%E5%BC%82%E6%AD%A5%E5%A4%8D%E4%BD%8D&zhida_source=entity)。

**解答与分析**

```verilog
module top_module (
	input clk,
	input in,
	input areset,
	output out
);

        // -----实现状态机
endmodule
```

这里我们学习标准答案中的表示，采用三段式的写法来描述这个简单的状态机。[三段式状态机](https://zhida.zhihu.com/search?content_id=104232083&content_type=Article&match_order=1&q=%E4%B8%89%E6%AE%B5%E5%BC%8F%E7%8A%B6%E6%80%81%E6%9C%BA&zhida_source=entity)虽然代码会长一些，但能够更方便地修改，并更清晰地表达状态机的跳变与输出规则。

使用参数来表示每个状态。

```verilog
	// Give state names and assignments. I'm lazy, so I like to use decimal numbers.
	// It doesn't really matter what assignment is used, as long as they're unique.
	parameter A=0, B=1;
	reg state;		// Ensure state and next are big enough to hold the state encoding.
	reg next;

    // A finite state machine is usually coded in three parts:
    //   State transition logic
    //   State flip-flops
    //   Output logic
    // It is sometimes possible to combine one or more of these blobs of code
    // together, but be careful: Some blobs are combinational circuits, while some
    // are clocked (DFFs).
```

三段式分别指

- 状态跳转逻辑
- 状态触发器实现
- 输出逻辑

状态跳转逻辑，根据输入信号以及当前状态确定状态的次态。

```verilog
    // Combinational always block for state transition logic. Given the current state and inputs,
    // what should be next state be?
    // Combinational always block: Use blocking assignments.
    always@(*) begin
	case (state)
		A: next = in ? A : B;
		B: next = in ? B : A;
	endcase
    end
```

状态触发器实现，在时钟边沿实现[状态寄存器](https://zhida.zhihu.com/search?content_id=104232083&content_type=Article&match_order=1&q=%E7%8A%B6%E6%80%81%E5%AF%84%E5%AD%98%E5%99%A8&zhida_source=entity)的跳变以及状态复位

```verilog
    // Edge-triggered always block (DFFs) for state flip-flops. Asynchronous reset.
    always @(posedge clk, posedge areset) begin
	if (areset) state <= B;		// Reset to state B
        else state <= next;			// Otherwise, cause the state to transition
    end	
```

输出逻辑，根据当前状态实现输出

```verilog
	// Combinational output logic. In this problem, an assign statement is the simplest.
	// In more complex circuits, a combinational always block may be more suitable.
	assign out = (state==B);
```