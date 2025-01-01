# 实验考复习 -- 上课案例  
!!! abstract    
    收录小白word文档的所有案例，考前会编成程序题然后更题目解析  

## Lec2  
### 2.1 把字符数组中的元素逐个取出并输出  
```asm  
data segment  
a db "ABC"  
s db "Hello$world!", 0Dh, 0Ah, 0  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov bx, 0  
next:  
   mov dl, s[bx]; 经过编译后变成mov dl, ds:[3+bx]  
   cmp dl, 0  
   je exit  
   mov ah, 2  
   int 21h  
   add bx, 1  
   jmp next  
exit:  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
- 可能有用的解释：  
源程序outs.asm中, 以下语句    
mov dl, s[bx]     
编译后, 变成:    
mov dl, [bx+0003]; 其中变量的段地址ds是隐含的    
这条机器语言指令其实等价于以下指令:    
mov dl, ds:[bx+0003]    
ds:[bx+0003]表示指针ds:bx+0003所指的对象,其中ds是变量的段地址, bx+0003是变量的偏移地址。    
根据上述分析，只要程序中引用了data段内的变量，则必须在程序一开始就把ds赋值为data，这样可以保证变量的段地址及偏移地址精确地指向该变量。  
## Lec 3  
### 3.1 验证小端规则的代码(C语言)  
```c  
main()  
{  
   unsigned short int a = 0x1234;  
   unsigned char *p;  
   p = (unsigned char *)&a;  
   printf("%X %X", p[0], p[1]);  
}  
main()  
{  
   unsigned char a[2]={0x12, 0x34};  
   unsigned short int *p;  
   p = (unsigned short int *)a;  
   printf("%X", *p);  
}  
```  
## Lec 4 -- 位运算  
### 4.1 运用rol指令把16位整数转化成16进制格式输出:  
```asm  
data segment  
abc dw 32767  
s db 4 dup(0),0Dh,0Ah,'$'  
;4 dup(0)相当于0,0,0,0  
;s[0]='7'; s[1]='F'; s[2]='F'; s[3]='F'  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov ax, abc  
   mov cx, 4  
   mov di, 0; 目标数组的下标,可以引用s[di]  
again:  
   push cx  
   mov cl, 4 ; 设ax的原值=7A9Dh  
   rol ax, cl; AX=A9D7, 9D7A, D7A9, 7A9D  
   push ax  
   and ax, 0000000000001111B; 000Fh  
   cmp ax, 10  
   jb is_digit  
is_alpha:  
   sub al, 10  
   add al, 'A'  
   jmp finish_4bits  
is_digit:  
   add al, '0'  
finish_4bits:  
   mov s[di], al  
   pop ax  
   pop cx  
   add di, 1  
   sub cx, 1  
   jnz again  
   mov ah, 9  
   mov dx, offset s  
   int 21h  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 4.2 运用rol指令把32位整数转化成16进制格式输出  
```asm  
.386  
data segment use16  
abc dd 2147483647  
data ends  
code segment use16  
assume cs:code, ds:data  
main:  
   mov ax, seg abc  
   mov ds, ax  
   mov eax, abc  
   mov cx, 8  
again:  
   rol eax, 4  
   push eax  
   and eax, 0Fh  
   cmp al, 10  
   jb is_digit  
is_alpha:  
   sub al, 10  
   add al, 'A'  
   jmp finish_4bits  
is_digit:  
   add al, '0'  
finish_4bits:  
   mov ah, 2  
   mov dl, al  
   int 21h  
   pop eax  
   sub cx, 1  
   jnz again  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
## Lec 5 -- 引用数组元素  
### 5.1 引用数组元素的例子  
```asm  
data segment  
abc db 1,2,3,4  
xyz dw 789Ah, 0BCDEh  
asd dd 12345678h, 56789ABCh; 首元素为asd[0]  
                           ; 末元素为asd[4]  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   ;形式(1)  
   mov ah, abc[1]; \编译后变成:  
   mov ah, [abc+1];/mov ah, ds:[1]; 直接地址  
   ;形式(2)  
   mov bx, offset abc  
   mov ah, [bx+1]; 间接地址  
   ;形式(3)  
   mov bx, 1  
   mov ah, abc[bx] ;\间接地址  
   mov ah, [abc+bx];/  
   ;形式(4)  
   mov bx, offset abc  
   mov si, 1  
   mov ah, [bx+si]  
   mov ax, xyz[2] ;\编译后变成:  
   mov ax, [xyz+2];/mov ax, ds:[6]  
     
   mov ah, abc; 等价于mov ah, abc[0]  
   mov ah, [abc]; 效果与上面这句等价  
                ;编译后变成mov ah, ds:[0]  
   mov ax, xyz  
   mov ax, [xyz]; 其完整形式是:  
                ; mov ax, word ptr ds:[xyz]  
                ; 编译后变成mov ax, ds:[4]  
     
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
程序解析：  
`mov ah, [abc]`中,   
`[abc]`可以理解成地址abc所指向的对象。  
`mov ah, [abc]`的完整形式其实是:  
`mov ah, byte ptr ds:[abc]`  
其中`ds`是变量`abc`的段地址  
`byte ptr`表示地址`abc`所指的对象是一个字节。  
若`[]`中不包含寄存器`bp`，则该变量默认的段地址一定是ds,故在源程序`addr.asm`中可以省略`ds`:。  
`byte ptr`有点类似于C语言中的`(char *)`, 其中`ptr`是单词pointer的缩写。  
`byte ptr ds:[abc]`表示地址`ds:abc`所指的对象是一个`byte`。相当于C语言的如下描述:  
`*(char *)(ds:abc)`  
汇编语言的语句中，如果源操作数或目标操作数的其中之一有明确的类型即宽度，则另外一方不需要指定类型。  
在本例中,由于ah是8位宽度，故可以省略源操作数的类型`byte ptr`。  
### 5.2 输入一个字符串再输出的例子  
```asm  
data segment  
a db 100 dup(0)  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov bx, 0  
input_next:  
   mov ah, 1  
   int 21h; AL=getchar()  
   cmp al, 0Dh; 判断是否回车符  
   je input_done  
   mov a[bx], al  
   add bx, 1  
   jmp input_next  
input_done:  
   mov a[bx], 0; 填充字符串结束标志  
   mov ah, 2  
   mov dl, 0Dh  
   int 21h; 输出回车  
   mov ah, 2  
   mov dl, 0Ah  
   int 21h; 输出换行  
   ;  
   mov bx, offset a  
   mov si, 0  
output_next:  
   mov dl, [bx+si]  
   cmp dl, 0  
   je output_done  
   mov ah, 2  
   int 21h; 输出DL中的字符  
   add si, 1  
   jmp output_next  
output_done:  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 5.3 显卡输出2000个'A'  
```asm  
code segment  
assume cs:code  
main:  
   mov ax, 0B800h  
   mov es, ax  
   mov di, 0  
   mov al, 'A'; mov al, 65;或 mov al,41h  
   mov ah, 71h; 白色背景，蓝色前景  
   mov cx, 2000  
again:  
   mov word ptr es:[di], ax; AX=1741h  
   ;mov byte ptr es:[di], al  
   ;mov byte ptr es:[di+1], ah  
   add di, 2  
   sub cx, 1  
   jnz again  
   mov ah, 1  
   int 21h; 键盘输入，起到等待敲键的作用  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 5.4 屏幕上移动的'A'的例子  
```asm  
code segment  
assume cs:code  
main:  
   mov ax, 0B800h  
   mov ds, ax  
   mov di, 0  
   mov al, 'A'  
   mov ah, 17h; 蓝色背景,白色前景  
   mov cx, 2000  
again:  
   mov ds:[di], ax  
   mov bx, 200h  
wait_wait:  
   mov dx, 0  
wait_a_while:  
   sub dx, 1  
   jnz wait_a_while  
   sub bx, 1  
   jnz wait_wait  
   mov word ptr ds:[di], 0020h  
   add di, 2  
   sub cx, 1  
   jnz again  
   mov ah, 1  
   int 21h; 相当于AL=getchar();  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
## Lec 6 -- ptr_assume_图形模式编程  
### 6.1 `assume`  
```asm  
data segment  
abc db 1,2,3,4  
data ends  
code segment  
assume cs:code, es:data  
;同一个段与多个段寄存器有关联时:ds > ss > es > cs  
main:  
   mov ax, data  
   mov es, ax  
   mov al, abc[1]; 编译后变成mov al, es:[0001]  
   ;先替换成mov al, data:[0001]  
   ;再替换成mov al, es:[0001]  
   ;在替换时编译器并不检查es与data是否相等  
   ;假定前面assume ds:data,则这句话就会替换成  
   ;mov al, ds:[0001]并简化成mov al, [0001]  
   ;因为[]中没有bp时，默认的段地址一定是ds且ds  
   ;可以省略。  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
作用：帮助编译器建立段寄存器与段的关联, 当源程序中引用了某个 段内的变量时，编译器会在编译出来的机器码中把变量的段地址替换成关联的段寄存器。  
### 6.2 显卡  
```asm  
code segment  
assume cs:code; cs不需要赋值会自动等于code  
main:  
   jmp begin  
i  dw 0  
begin:  
   mov ax, 0013h  
   int 10h  
   mov ax, 0A000h  
   mov es, ax  
   ;(320/2, 200/2)  
   mov di, (100-20)*320+(160-20); (160-20,100-20)  
   ;mov cx, 41; rows=41  
   mov i, 41  
next_row:  
   ;push cx  
   push di  
   mov al, 4; color=red  
   mov cx, 41; dots=41  
next_dot:  
   mov es:[di], al  
   add di, 1  
   sub cx, 1  
   jnz next_dot  
   pop di; 左上角(x,y)对应的地址  
   ;pop cx; cx=41  
   add di, 320; 下一行的起点的地址  
   ;sub cx, 1; 行数-1  
   sub i, 1  
   jnz next_row  
   mov ah,0  
   int 16h;bios键盘输入,类似int 21h的01h功能  
   mov ax, 0003h  
   int 10h; 切换到80*25文本模式  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 6.2 cn.asm  
```asm  
data segment  
hz db 04h,80h,0Eh,0A0h,78h,90h,08h,90h  
   db 08h,84h,0FFh,0FEh,08h,80h,08h,90h  
   db 0Ah,90h,0Ch,60h,18h,40h,68h,0A0h  
   db 09h,20h,0Ah,14h,28h,14h,10h,0Ch  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov ax, 0A000h  
   mov es, ax  
   mov di, 0  
   mov ax, 0013h  
   int 10h  
   mov dx, 16  
   mov si, 0  
next_row:  
   mov ah, hz[si]  
   mov al, hz[si+1]  
   add si, 2  
   mov cx, 16  
check_next_dot:  
   shl ax, 1; 刚移出的位会自动进入CF(进位标志)  
   jnc no_dot; 若没有进位即CF=0则跳到no_dot  
is_dot:  
   mov byte ptr es:[di], 0Ch  
no_dot:  
   add di, 1  
   sub cx, 1  
   jnz check_next_dot  
   sub di, 16  
   add di, 320  
   sub dx, 1  
   jnz next_row  
   mov ah, 1  
   int 21h  
   mov ax, 0003h  
   int 10h  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 6.3 cnt.asm  
```asm  
data segment  
hz db 04h,80h,0Eh,0A0h,78h,90h,08h,90h  
   db 08h,84h,0FFh,0FEh,08h,80h,08h,90h  
   db 0Ah,90h,0Ch,60h,18h,40h,68h,0A0h  
   db 09h,20h,0Ah,14h,28h,14h,10h,0Ch  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov ax, 0B800h  
   mov es, ax  
   mov ax, 0003h  
   int 10h  
   mov di, 0  
   mov dx, 16  
   mov si, 0  
next_row:  
   mov ah, hz[si]  
   mov al, hz[si+1]  
   add si, 2  
   mov cx, 16  
check_next_dot:  
   shl ax, 1  
   jnc no_dot  
is_dot:  
   mov byte ptr es:[di], '*'  
   mov byte ptr es:[di+1], 0Ch  
no_dot:  
   add di, 2  
   sub cx, 1  
   jnz check_next_dot  
   sub di, 32  
   add di, 160  
   sub dx, 1  
   jnz next_row  
   mov ah, 1  
   int 21h  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
## Lec 7 -- ss/es/fl  
### 7.1 堆栈段的定义及使用  
```asm  
data segment  
abc dw 1234h, 5678h  
data ends  
code segment  
assume cs:code, ds:data, ss:stk  
;ss和sp的值在程序开始运行时由操作系统自动设定,  
;程序员不需要手工对它们进行赋值。  
;正如cs:ip也是在程序开始运行时由操作系统进行赋值  
;一样。  
main:  
   mov ax, data  
   mov ds, ax  
   push abc[0]  
   pop abc[2]  
   mov ah, 4Ch  
   int 21h  
code ends  
stk segment stack  
db 200h dup(0); 或写成dw 100h dup(0)  
stk ends  
;堆栈空间是stk:0到stk:1FF  
;程序开始运行时,ss=stk,sp=1FF+1  
end main  
```  
### 7.2 `es`使用  
es: extra segment附加段，它跟ds类似，可以用来表示一个数据段的段址。  
```asm  
data1 segment  
abc db 1,2,3  
data1 ends  
data2 segment  
xyz db 4,5,6  
data2 ends  
code segment  
assume cs:code, ds:data1, es:data2  
main:  
   mov ax, data1  
   mov ds, ax  
   mov ax, data2  
   mov es, ax  
   mov ah, abc[1]; 编译后变成mov ah, ds:[1]  
   ;也可以写成mov ah, ds:abc[1]  
   mov xyz[1], ah; 编译后变成mov es:[1], ah  
   ;也可以写成mov es:xyz[1], ah  
   ;错误写法:mov abc[1], xyz[1]; 因两个对象不能都为内存变量  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
## Lec 8 -- 算术指令  
### 8.1 `xlat`指令  
在`xlat`执行前必须让`ds:bx`指向表, `al`必须赋值为  
数组的下标; 执行`xlat`后, `AL=ds:[bx+AL]`  
```asm  
char t[]="0123456789ABCDEF";  
char i;  
i = 10;  
i = t[i]; 最后`i='A'`  
```  
设`ds`=数组`t`的段地址  
```asm  
mov bx, offset t; BX=表的首地址  
mov al, 10; AL为下标  
xlat; 结果AL='A'  
```  
xlat指令要求DS:BX指向数组，AL=数组下标。  
执行指令后, AL=数组元素  
```asm  
.386 ; 表示程序中会用32位的寄存器  
data segment use16; use16表示偏移使用16位  
t db "0123456789ABCDEF"  
x dd 2147483647  
data ends  
code segment use16  
assume cs:code, ds:data  
main:  
   mov ax, data    ;\  
   mov ds, ax      ; / ds:bx->t[0]  
   mov bx, offset t;/  
   mov ecx, 8  
   mov eax, x  
next:  
   rol eax, 4  
   push eax  
   and eax, 0Fh  
   xlat  
   mov ah, 2  
   mov dl, al  
   int 21h  
   pop eax  
   sub ecx, 1  
   jnz next  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
还有一道……  
```asm  
.386 ; 表示程序中会用32位的寄存器  
data segment use16; use16表示偏移使用16位  
t db "0123456789ABCDEF"  
x dd 2147483647  
y dd 1234567890  
sx db 8 dup(0), 0Dh, 0Ah, '$'  
sy db 8 dup(0), 0Dh, 0Ah, '$'  
data ends  
code segment use16  
assume cs:code, ds:data  
main:  
   mov ax, data    ;\  
   mov ds, ax      ; / ds:bx->t[0]  
   mov eax, x  
   mov di, offset sx  
   call convert  
   mov eax, y  
   mov di, offset sy  
   call convert  
   mov dx, offset sx  
   call output  
   mov dx, offset sy  
   call output  
   mov ah, 4Ch  
   int 21h  
output:  
;input: dx->string to output  
   push ax  
   mov ah, 9  
   int 21h  
   pop ax  
   ret  
convert:  
;input: eax=32-bit number to be converted  
;       di->target array   
   push bx  
   push di  
   push eax  
   push ecx  
   mov bx, offset t  
   mov ecx, 8  
next:  
   rol eax, 4  
   push eax  
   and eax, 0Fh  
   xlat; AL=ds:[bx+AL]  
   mov [di], al  
   inc di  
   pop eax  
   sub ecx, 1  
   jnz next  
   pop ecx  
   pop eax  
   pop di  
   pop bx  
   ret  
code ends  
end main  
```  
### 8.2 `adc`指令  
add with carry,蛮好理解的指令，这是从word里扒下来的程序，不完整  
- 计算12345678h + 5678FFFFh  
```asm  
mov dx, 1234h  
mov ax, 5678h  
add ax, 0FFFFh; CF=1  
adc dx, 5678h; DX=DX+5678h+CF  
把x和y相加(x、y均为由100字节构成且用小端表示的大数)，结果保存到z中:  
x db 100 dup(88h)  
y db 100 dup(99h)  
z db 101 dup(0)  
;设ds已经赋值为上述数组的段地址  
mov cx, 100  
mov si, offset x  
mov di, offset y  
mov bx, offset z  
clc  
next:  
mov al, [si]  
adc al, [di]  
mov [bx], al  
inc si  
inc di  
inc bx  
dec cx  
jnz next  
adc z[100], 0; 或adc byte ptr [bx], 0  
```  
### 8.3 浮点数相关指令  
知识点不抄了，有点多  
[看看这个](https://slowist-lee.github.io/notebook/cs/pl/Asm/sum/#5522)  
```asm  
;Turbo Debugger跟踪时，  
;点菜单View->Numeric Processor查看小数堆栈  
data segment  
abc dd 3.14  
xyz dd 2.0  
result dd 0  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   fld abc; 把3.14载入到小数堆栈  
   fld xyz; 把2.0载入到小数堆栈  
   fmul st, st(1); 两数相乘  
   fstp result; 保存结果到result，并弹出  
   fstp st      ; 弹出小数堆栈中残余的值  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
### 8.4 除法相关  
```asm  
code segment  
assume cs:code  
old_00h dw 0, 0  
int_00h:  
   mov ch, 10h  
   iret  
main:  
   push cs  
   pop ds  
   xor ax, ax  
   mov es, ax  
   mov bx, 0  
   mov ax, es:[bx]  
   mov dx, es:[bx+2]  
   mov old_00h[0], ax  
   mov old_00h[2], dx  
   mov word ptr es:[bx], offset int_00h  
   mov es:[bx+2], cs  
   mov ax, 123h  
   mov ch, 1  
   div ch  
   mov ax, old_00h[0]  
   mov dx, old_00h[2]  
   mov es:[bx], ax  
   mov es:[bx+2], dx  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```  
小白的说明  
>不过,我们可以通过修改0:0处的远指针(即int 00h的目标函数地址或中断向量)把我们自己的函数如int_00h与int 00h中断进行绑定,从而使得int 00h发生时让cpu来执行我们自己定义的中断函数int_00h。以下代码通过自定义中断函数int_00h改变ch的值使其等于10h, 于是当cpu从中断函数返回并继续执行div ch时能正常执行除法而不发生溢出.  
### 8.5 字符串  
还是从word里扒的，不完整的段  
```asm  
;假定从地址1000:0000起存放以下字符串：  
;"###ABC"，现要求跳过前面的#，把后面剩余的  
;全部字符复制到2000:0000中。  
;假定es=1000h, di=0, cx=7, 则  
mov al, '#'  
cld  
repe scasb  
dec di; ES:DI->"ABC"  
inc cx; CX=4  
push es  
pop ds; DS=ES  
push di  
pop si; SI=DI  
mov ax, 2000h  
mov es, ax  
mov di, 0  
rep movsb  
```  
## Lec 9 jmp_loop_call  
### 9.1 自我移动的代码  
```asm  
code segment  
assume cs:code, ds:code, es:code  
main:  
   push cs  
   pop ds; DS=CS  
   push cs  
   pop es; ES=CS  
   cld  
   mov ah, 2  
   mov dl, 'A'  
   int 21h  
   mov si, offset begin_flag  
   mov di, 1000h  
   mov cx, offset end_flag-offset begin_flag  
   rep movsb  
   mov cx, offset end_flag - offset main  
   mov di, offset main  
   mov bx, 1000h  
   jmp bx  
begin_flag:  
   jmp next  
next:  
   mov al, 0  
   rep stosb  
   mov ah, 2  
   mov dl, 'B'  
   int 21h  
   mov ah, 4Ch  
   int 21h  
end_flag:  
code ends  
end main  
```  
### 9.2 修改printf让它做加法运算(C代码)  
```asm  
/* 用TC编译，菜单Options->Compiler->Model->Tiny  
    Compile->Compile to OBJ  
    Compile->Link EXE file  
    Run->Run  
    Run->User Screen  
 */  
extern int printf();  
int f(int a, int b)  
{  
   return a+b;  
}  
void zzz(void)  
{  
}  
main()  
{  
   char buf[100];  
   char *p = (char *)printf;  
   char *q = (char *)f;  
   int n = (char *)zzz - (char *)f;  
   int y;  
   memcpy(buf, p, n);  
   memcpy(p, q, n);  
   y = printf(10, 20);  
   memcpy(p, buf, n);  
   printf("y=%d\n", y);  
}  
```  
### 9.3 短跳、近跳、远跳  
```asm  
code segment  
assume cs:code  
main:  
   jmp next; jmp short next  
exit:  
   mov ah, 4Ch  
   int 21h  
next:  
   mov ah, 2  
   mov dl, 'A'  
   int 21h  
   jmp abc; jmp near ptr abc  
   db 200h dup(0)  
abc:  
   jmp far ptr away; jmp far ptr away  
code ends  
fff segment  
assume cs:fff  
away:  
   mov ah, 2  
   mov dl, 'F'  
   int 21h  
   jmp far ptr exit; jmp far ptr exit  
fff ends  
end main  
```  
### 9.4 参数个数可变的例子(C代码)  
```asm  
#include <stdio.h>  
double f(char *s, ...)  
{  double y=0;  
   char *p = (char *)&s; /* p = bp+4 */  
   p += sizeof(s); /* p = bp+6 */  
   while(*s != '\0')  
   {  
      if(*s == 'i')  
      {  
         y += *(int *)p;  
         p += sizeof(int);  
      }  
      else if(*s == 'l')  
      {  
         y += *(long*)p;  
         p += sizeof(long);  
      }  
      else if(*s == 'd')  
      {  
         y += *(double *)p;  
         p += sizeof(double);  
      }  
      s++;  
   }  
   return y;  
}  
main()  
{  
   double y;  
   y = f("ild", 10, 20L, 3.14);  
   printf("y=%lf\n", y);  
}  
```  
## Lec 10 --中断  
### 10.1 `int 80`  
```asm  
code segment  
assume cs:code  
old_80h dw 0, 0  
main:  
   xor ax, ax  
   mov es, ax  
   mov bx, 80h*4; mov bx, 200h  
   mov ax, es:[bx]  
   mov old_80h[0], ax  
   mov ax, es:[bx+2]  
   mov old_80h[2], ax  
   ;  
   mov word ptr es:[bx], offset int_80h  
   mov es:[bx+2], cs  
   ;  
   mov ah, 1  
   int 80h; AL=键盘输入的ASCII码  
next:  
   mov ah, 2  
   mov dl, al  
   int 80h  
   ;  
   mov ax, old_80h[0]  
   mov es:[bx], ax  
   mov ax, old_80h[2]  
   mov es:[bx+2], ax  
   ;  
   mov ah, 4Ch  
   int 21h  
int_80h: ; ISR(Interrupt Service Routine)  
         ; 中断服务函数  
   cmp ah, 1  
   je is_1  
is_2:  
   push es  
   push bx  
   push ax  
   mov bx, 0B800h  
   mov es, bx  
   mov byte ptr es:[160], dl  
   mov byte ptr es:[161], 17h  
   pop ax  
   pop bx  
   pop es  
   jmp done  
is_1:  
   int 21h  
done:  
   iret  
code ends  
end main  
```  
### 10.2 `int 00`  
```asm  
code segment  
assume cs:code  
old_00h dw 0, 0  
main:  
   xor ax, ax  
   mov es, ax  
   mov bx, 0  
   mov ax, es:[bx]  
   mov old_00h[0], ax  
   mov ax, es:[bx+2]  
   mov old_00h[2], ax  
   ;  
   mov word ptr es:[bx], offset int_00h  
   mov es:[bx+2], cs  
   ;  
   mov ax, 1234h  
   mov dh, 0  
;int 00h  
here:  
   div dh  
next:  
   mov ax, old_00h[0]  
   mov es:[bx], ax  
   mov ax, old_00h[2]  
   mov es:[bx+2], ax  
   ;  
   mov ah, 4Ch  
   int 21h  
msg db "Divided by 0!!!", 0Dh, 0Ah, '$'  
int_00h:  
   push bp  
   mov bp, sp  
   push ax  
   push dx  
   push ds  
   push cs  
   pop ds  
   mov ah, 9  
   mov dx, offset msg  
   int 21h  
   pop ds  
   pop dx  
   pop ax  
   mov word ptr [bp+2], offset next  
   pop bp  
   iret  
code ends  
end main  
```  
### 10.3 `int 8`  
```asm  
data segment  
s db '0',17h  
count db 0  
stop db 0  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   xor ax, ax  
   mov es, ax; ES=0  
   mov bx, 8h*4  
   push es:[bx]  
   pop cs:old8h[0]; old8h[0] = es:[bx]  
   push es:[bx+2]  
   pop cs:old8h[2]  
   cli; IF=0禁止中断  
   mov word ptr es:[bx], offset int8h  
   mov es:[bx+2], cs; 或seg int8h或code  
   sti; IF=1允许中断  
wait_a_while:  
   cmp stop, 1  
   jne wait_a_while  
   cli  
   mov ax,cs:old8h[0]  
   mov es:[bx], ax  
   mov ax,cs:old8h[2]  
   mov es:[bx+2],ax  
   sti  
   mov ah, 4Ch  
   int 21h  
int8h:    ; interrupt service routine  
   push ax  
   push cx  
   push si  
   push di  
   push ds  
   push es  
   mov ax, 0B800h  
   mov es, ax  
   mov di, 0  
   mov ax, data  
   mov ds, ax  
   inc count  
   cmp count, 18  
   jb skip  
   mov count, 0  
   mov si, offset s  
   mov cx, 2  
   cld  
   rep movsb  
   inc s[0]  
   cmp s[0], '9'  
   jbe skip  
   mov stop, 1  
skip:  
   pop es  
   pop ds  
   pop di  
   pop si  
   pop cx  
   pop ax  
   ;push ax  
   ;mov al, 20h  
   ;out 20h, al  
   ;pop ax  
   ;iret  
   jmp dword ptr cs:[old8h]  
old8h dw 1234h, 5678h  
;设原int 8h的中断向量为5678h:1234h  
code ends  
end main  
```  
### 10.4 `key.asm`  
```asm  
;---------------------------------------  
;PrtSc/SysRq: E0 2A E0 37 E0 B7 E0 AA  ;  
;Pause/Break: E1 1D 45 E1 9D C5        ;  
;---------------------------------------  
data segment  
old_9h dw 0, 0  
stop   db 0  
key    db 0; key=31h  
phead  dw 0  
key_extend  db 'KeyExtend=', 0  
key_up      db 'KeyUp=', 0  
key_down    db 'KeyDown=', 0  
key_code    db '00h ', 0  
hex_tbl     db '0123456789ABCDEF'  
cr          db  0Dh, 0Ah, 0  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   xor ax, ax  
   mov es, ax  
   mov bx, 9*4  
   push es:[bx]  
   pop old_9h[0]  
   push es:[bx+2]  
   pop old_9h[2]    ; 保存int 9h的中断向量  
   cli  
   mov word ptr es:[bx], offset int_9h  
   mov es:[bx+2], cs; 修改int 9h的中断向量  
   sti  
again:  
   cmp [stop], 1  
   jne again        ; 主程序在此循环等待  
   push old_9h[0]  
   pop es:[bx]  
   push old_9h[2]  
   pop es:[bx+2]    ; 恢复int 9h的中断向量  
   mov ah, 4Ch  
   int 21h  
int_9h:  
   push ax  
   push bx  
   push cx  
   push ds  
   mov ax, data  
   mov ds, ax       ; 这里设置DS是因为被中断的不一定是我们自己的程序  
   in al, 60h       ; AL=key code  
   mov [key], al  
   cmp al, 0E0h  
   je  extend  
   cmp al, 0E1h  
   jne up_or_down  
extend:  
   mov [phead], offset key_extend  
   call output  
   jmp check_esc  
up_or_down:  
   test al, 80h     ; 最高位==1时表示key up  
   jz down  
up:  
   mov [phead], offset key_up  
   call output  
   mov bx, offset cr  
   call display     ; 输出回车换行  
   jmp check_esc  
down:  
   mov [phead], offset key_down  
   call output  
check_esc:     
   cmp [key], 81h   ; Esc键的key up码  
   jne int_9h_iret  
   mov [stop], 1  
int_9h_iret:  
   mov al, 20h      ; 发EOI(End Of Interrupt)信号给中断控制器，  
   out 20h, al      ; 表示我们已处理当前的硬件中断(硬件中断处理最后都要这2条指令)。  
                    ; 因为我们没有跳转到的old_9h，所以必须自己发EOI信号。  
                    ; 如果跳到old_9h的话，则old_9h里面有这2条指令，这里就不要写。  
   pop ds  
   pop cx  
   pop bx  
   pop ax  
   iret             ; 中断返回指令。从堆栈中逐个弹出IP、CS、FL。  
output:  
   push ax  
   push bx  
   push cx  
   mov bx, offset hex_tbl  
   mov cl, 4  
   push ax   ; 设AL=31h=0011 0001  
   shr al, cl; AL=03h  
   xlat      ; AL = DS:[BX+AL] = '3'  
   mov key_code[0], al  
   pop ax  
   and al, 0Fh; AL=01h  
   xlat       ; AL='1'  
   mov key_code[1], al  
   mov bx, [phead]  
   call display     ; 输出提示信息  
   mov bx, offset key_code  
   call display     ; 输出键码  
   pop cx  
   pop bx  
   pop ax  
   ret  
     
display:  
   push ax  
   push bx  
   push si  
   mov si, bx  
   mov bx, 0007h    ; BL = color  
   cld  
display_next:  
   mov ah, 0Eh      ; AH=0Eh, BIOS int 10h的子功能，具体请查中断大全  
   lodsb  
   or al, al  
   jz display_done  
   int 10h          ; 每次输出一个字符  
   jmp display_next  
display_done:  
   pop si  
   pop bx  
   pop ax  
   ret  
code ends  
end main  
```  
