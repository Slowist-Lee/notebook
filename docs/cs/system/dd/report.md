# 数字系统设计实验

> [!summary]
> 实验课一共提交两次实验报告。lab5我相对写的比较潦草，lab12是大作业，写的还是相对认真的，可惜最后总评分不高，应该是我用了三段式而不是二段式的缘故吧。
> 
> 实验考允许带开卷考资料，下面是我打印的东西。

## lab5

<object data="lab5.pdf" type="application/pdf" width="100%" height="800">
    <embed src="../report/lab5.pdf" type="application/pdf" />
</object>

## lab12

<object data="lab12.pdf" type="application/pdf" width="100%" height="800">
    <embed src="../report/lab12.pdf" type="application/pdf" />
</object>

[代码Github. ](https://github.com/Slowist-Lee/DigitalSystem) 但注意我的状态机写的是三段式（而不是老师用的二段式），而且进位好像有点问题。

## 实验考复习

> 除下面内容外，还打印了软件的基本使用方法（课本).

### 状态机

```
module controller(
    input in,
    input clk,
    input reset,
    output reg count,
    output reg clr,
    output reg first
);
    //三段式
    //状态编码
    parameter RESET = 2'b00;
    parameter TIMING = 2'b01;
    parameter FIRST = 2'b10;
    parameter STOP = 2'b11;

    ///machine variable
    reg [1:0] st_next;//next state
    reg [1:0] st_cur;//current state

    //1. state transfer
    always @(posedge clk or posedge reset)begin
        if(reset)
            st_cur=RESET;
        else
            st_cur=st_next;
    end

    //2.state switch
    always @(*)begin
        case(st_cur)
            RESET:
                case(in)
                    1'b0: st_next=RESET;
                    1'b1: st_next=TIMING;
                endcase
            TIMING:
                case(in)
                    1'b0: st_next=TIMING;
                    1'b1: st_next=FIRST;
                endcase
            FIRST:
                case(in)
                    1'b0: st_next=FIRST;
                    1'b1: st_next=STOP;
                endcase
            STOP:
                case(in)
                    1'b1: st_next=RESET;
                    1'b0: st_next=STOP;
                endcase
        endcase
    end
    //3. output logic
    always @(posedge clk or posedge reset) begi
        //如果没开始，就不用计时，输出也是0
        else begin
            case(st_cur)
                RESET: begin
                    clr <= 1;
                    count <= 0;
                    first <=0;
                end
                TIMING: begin
                    clr <= 0;
                    count <= 1;
                    first <=0;
                end
                FIRST: begin
                    clr <= 0;
                    count <= 1;
                    first <=1;
                end
                STOP: begin
                    clr <= 0;
                    count <= 0;
                    first <=0;
                end
            endcase
        end
    end
endmodule
```

### 触发器

```
module dffre(d, en, r, clk, q);
parameter n = 1;
output [n-1:0]  q;
input d, en, r, clk;
reg[n-1:0] q;

always@(posedge clk)
begin
    if(r == 1'b1)begin
        q <= 0;
    end
    else begin
        if(en == 1'b1)begin
            q <= d;
        end
        else begin
            q <= q;
        end
    end
end
endmodule
```

### 计数器

```
module counter_n(clk,en,r,q,co);
  parameter  n=4; 
  parameter  counter_bits=2;
  input   clk,en,r ;
  output  co;
  output [counter_bits-1:0]  q;
  reg [counter_bits-1:0]  q=0;
  assign  co=(q==(n-1)) && en;
  always @(posedge clk) 
  begin
      if(r) q=0;
	    else if(en)  
	          begin	 
                if(q==(n-1))  q=0 ;
                else q=q+1;		 
            end
  end
endmodule
```

#### 计时器

```
module count_time #(
    parameter n = 10,              // 计时器的最大计数值
    parameter counter_bits = 4     // 计数器所需的位数
) (
    input clk,                     // 时钟信号
    input r,                       // 复位信号
    input en,                      // 使能信号
    output done                    // 计时完成信号
);
    reg [counter_bits-1:0] q;      // 计数器寄存器
    assign done = (q == n-1);      // 当计数器达到最大值时，done 信号置高

    always @(posedge clk) begin
        if (r) begin
            q <= 0;                // 复位信号有效时，将计数器清零
        end else if (en) begin
            q <= q + 1;            // 使能信号有效时，计数器递增
        end else begin
            q <= q;                // 其他情况下，保持计数器值不变
        end
    end
endmodule
```
### Testbench

```
module controller_tb;
parameter dely = 10;
reg in;
reg clk;
reg reset;
wire clr;
wire count;
//实例化

controller u_controller(
    .clk(clk),
    .in(in),
    .reset(reset),
    .count(count),
    .clr(clr)
);

initial begin
    clk = 0;
    forever #(dely) clk  = ~clk;
end

initial begin
    //初始化
    in=0;
    reset = 1;
    #(5*dely);
    reset=0;
    #(5*dely);
    in=0;
    #(5*dely);
    in=1;
    #(5*dely);
    in=0;
    #(5*dely);
    in=1;
    #(5*dely);
    in=0;
    #(5*dely);
    in=1;
    #(5*dely);
    $finish;
end

initial begin
    $monitor("Time = %0t, clk = %b, reset = %b, in = %b, clr = %b, count = %b", $time, clk, reset, in, clr, count);
end

endmodule
```

也有这种写法：

```
	//  clr
	initial 
	 begin
	   clk = 0;r=0;en = 0;
       #(51) r=1;
  	   #(100)r=0 ;
       repeat (620)  begin 
	     #(100*3)  en=1;
	     # 100  en=0; end
         #1000 $stop;
  end
```

### 一些框图：

同步器：

![|400](Pasted%20image%2020250526102954.png)

防颤电路：

![|375](Pasted%20image%2020250526103035.png)

