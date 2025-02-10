# 时序电路

1. D触发器：

![](Pasted%20image%2020250208203707.png)

功能介绍：

D 触发器是一个电路，存储 1bit 数据，并定期地根据触发器的输入(d)更新这 1 bit 数据，更新通常发生在时钟上升沿(clk)。存储的数据会通过输出管脚(q)输出。

t1时刻: d -> 0
t2时刻: clk->1 上升沿到来,触发器存储的数据变成 0，输出 q 保持为存储的值：0，直到下一个时钟上升沿到来。
t3时刻: d -> 1（d:我变了），q 仍保持 0 不动摇（时钟沿还没来呢）
t4时刻: clk->1 上升沿到来，q->1(q：时钟沿来了，我该变身了)
绝大多数时候，我们不会在 Verilog 代码中显示例化一个触发器（作者没这么做过，但应该是可以做的），我们在时钟敏感的 always 块中的语句一般都会被综合工具转换为相应的触发器。
D 触发器可以认为是一个触发器和一段最简单的组合逻辑块（blob :想表达逻辑块的时候用我，别用 block）的组合。其中组合逻辑块仅仅是一段 wire。（q 直接输出了触发器的存储值）

- clk=0,读取d
- clk=1,写入d

注意时序的一些语法：

1. always:
```verilog
always @(*) // 在任何情况下都执⾏always块，常⽤于书写组合逻辑 
always @(a) // 当a的值发⽣改变的时候，执⾏ 
always @(a or b) // 当a或b的值发⽣改变的时候，执⾏ 
always @(posedge a or negedge b) // 当遇到a的正边沿或b的负边沿时，执⾏ always // 不带@，执⾏完⼀次块内内容后，就再执⾏⼀次，常⽤于tesebench的clk信号改变
```

其中：
- 正边沿：信号从low到high 
- 负边沿：信号从high到low

2. **阻塞性赋值和非阻塞性赋值**

在Verilog中有以下三种赋值方法：

```verilog
连续赋值(assign x=y;)：不能在过程块内使用；
过程阻塞性赋值(x=y;)：只能在过程块中使用；
过程非阻塞性复制(x<=y)：只能在过程块内使用。
```

- 在组合always块中，使用阻塞性赋值。在时序always块中，使用非阻塞性赋值。

8位触发器的实现：

```verilog
module top_module (
    input clk,
    input [7:0] d,
    output [7:0] q
);
    always @(posedge clk)
        q<=d;
endmodule
```

给触发器配上同步复位端口(同步复位：当时钟上升沿到来时，如果同步复位端有效（本题中复位高电平有效，即 reset），那么任凭你触发器此前输出或者输入的是 0，是 1，输出一律变为 0):

```verilog
module top_module (
    input clk,
    input reset,            // Synchronous reset
    input [7:0] d,
    output [7:0] q
);
    always@(posedge clk)begin
        if(reset)
            q <= 8'b0;
        else
            q <= d;
    end
endmodule
```


![|325](Pasted%20image%2020250208210740.png)

引入**异步复位**：

- 对于同步复位系统来说，当同步复位事件发生时，等到下一个时钟上升沿才会得到响应，响应的速度比较慢。
- 与之相对的异步复位的响应就很快，因为在异步复位有效的时刻，复位响应就会发生，好像戳破气球一般。

简而言之：就是让areset的变化早于下一个clk上升沿被发现！

我写了一个同步复位，和异步进行了对比：

![|625](Pasted%20image%2020250208211343.png)

代码：（抄的ww）

```verilog
module top_module (
    input clk,
    input areset,   // active high asynchronous reset
    input [7:0] d,
    output [7:0] q
);
    always @(posedge clk or posedge areset)begin
        if(areset)
            q<=8'b0;
        else
            q<=d;
    end
endmodule
```


锁存器：D-latches:

```verilog
module top_module (
    input d,
    input ena,
    output q);
    always @(*)begin
        if(ena)
            q<=d;
    end
endmodule
```


其中，`ena`是使能端

触发器和门电路的综合：

![|500](Pasted%20image%2020250209165043.png)

```verilog
module top_module (
    input clk,
    input x,
    output z
); 

    reg q1 = 0;
    reg q2 = 0;
    reg q3 = 0;

    always @ (posedge clk)
        begin
            q1 <= x ^ q1; 
        end

    always @ (posedge clk)
        begin
            q2 <= x & (~q2);
        end

    always @ (posedge clk)
        begin
            q3 <= x | (~q3);
        end

    assign z = ~(q1 | q2 | q3); 

endmodule
```


多变量，用case的巧妙写法：

```verilog
module top_module (
    input clk,
    input j,
    input k,
    output Q); 

    always @ (posedge clk)
        begin
            case ({j, k})
                2'b00: Q <= Q;
                2'b01: Q <= 1'b0;
                2'b10: Q <= 1'b1;
                2'b11: Q <= ~Q;
            endcase
        end

endmodule
```