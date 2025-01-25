---
password: cc98
---

# Exercise -- 编排版

## Ex.1

```asm
comment @---------------------------------------------------------------------
遍历并输出字符串 s 的每个字符，直到遇到字符串的结束符
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========


data segment  
a db "ABC"  
s db "Hello$world!", 0Dh, 0Ah, 0  
data ends  
code segment  
assume cs:code, ds:data  

main:
   mov ax, seg s
   mov ds, ax
; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
; 按逆序输出 s 中的字符
; #1_begin--------------------------------------

; #1_end========================================

exit:
   mov ah, 4Ch
   mov al, 0
   int 21h
code ends
end main
```

??? tip "答案"
    ```asm
    comment @---------------------------------------------------------------------
    遍历并输出字符串 s 的每个字符，直到遇到字符串的结束符
    ------------------------------------------------------------------------------@

    ;==========请把以下代码保存到src\main.asm==============================
    ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========

    data segment  
    a db "ABC"  
    s db "Hello$world!", 0Dh, 0Ah, 0  
    data ends  
    code segment  
    assume cs:code, ds:data  

    main:
    mov ax, seg s
    mov ds, ax
    ; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
    ; 按逆序输出 s 中的字符
    ; #1_begin--------------------------------------
    mov bx, offset s
    output:
    mov dx,[bx]
    cmp dx,0
    je exit
    mov ah, 02h
    int 21h
    add bx,1
    jmp output
    ; #1_end========================================

    exit:
    mov ah, 4Ch
    mov al, 0
    int 21h
    code ends
    end main
    ```

注意点：  
- `[]`内只能是`bx,si,di,bp`  
- `mov ax, seg s`的意思：`ax`是`s`的段地址！  


## Ex.2

```asm
comment @---------------------------------------------------------------------

将一个16位的二进制数（存储在abc中）转换为它的十六进制字符串表示，并打印出来

示例输入输出：
输入：abc dw 32767（十六进制的7FFF）
输出：7FFF（因为32767的十六进制表示就是7FFF，所以直接打印出来）

注意：这段代码没有提供输入功能，它只是将预定义的值32767转换为十六进制字符串并打印。在实际的DOS环境中，这段代码会直接打印出7FFF。
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========

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
; 请在 #1_begin 和 #1_end 之间补充代码实现功能：
; 将一个16位的二进制数（存储在abc中）转换为它的十六进制字符串表示，并打印
; #1_begin--------------------------------------

; #1_end========================================
;end:
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```

这道题删减的好像有点过头了，难度实在太大了……  
我只能看懂上课的代码重写一遍了…

关键的方法：

1. 我们知道，由于`x86asm`中只有四个寄存器，然后我们又没法定义变量，导致这样全局变量的个数真的相当有限……但是这道题，相当于是一个4*4二重嵌套的循环，所以我们可以配合`push cx`，由于大的这套循环用不上这个计数器，我们就先用栈暂存一下

2. 怎么一口气取后几位？这个是基操了居然不会www   
以这题为例，我们想取后四位：  
```asm
and ax, 0000000000001111B
```

3. 由此引申到`rol`的意义，我们不能为这四位分别设置四个不同的`and`,所以，我们就用`rol`命令让这四位依次到最后面进行一个相加，反正最后进行一个输出

4. 注意到这题其实给的很好,`s`数组是以`$`结尾的，所以记得要用`ah=09h`的调用!!!

5. 理论考知识点 —— 循环移位不可以用立即数！！！

6. 注意`masm`比较傻，只会用`rol ax,1`,否则必须放在`cl`中，所以只能再`push`一次了

??? tip "答案"
    ```
    comment @---------------------------------------------------------------------

    将一个16位的二进制数（存储在abc中）转换为它的十六进制字符串表示，并打印出来

    示例输入输出：
    输入：abc dw 32767（十六进制的7FFF）
    输出：7FFF（因为32767的十六进制表示就是7FFF，所以直接打印出来）

    注意：这段代码没有提供输入功能，它只是将预定义的值32767转换为十六进制字符串并打印。在实际的DOS环境中，这段代码会直接打印出7FFF。
    ------------------------------------------------------------------------------@

    ;==========请把以下代码保存到src\main.asm==============================
    ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========

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
    ; 请在 #1_begin 和 #1_end 之间补充代码实现功能：
    ; 将一个16位的二进制数（存储在abc中）转换为它的十六进制字符串表示，并打印
    ; #1_begin--------------------------------------
    add di,3
    again:
    push cx
    push ax
    and ax, 0000000000001111B
    cmp al,0Ah
    jge alpha
    digit:
    add al,'0'
    jmp done
    alpha:
    sub al,0Ah
    add al, 'A'
    jmp done
    done:
    mov s[di],al
    dec di
    pop ax
    mov cl,4
    ror ax, cl
    pop cx
    loop again
    output:
    xor dx,dx
    mov dx, offset s
    mov ah,09h
    int 21h
    ; #1_end========================================
    mov ah, 4Ch  
    int 21h  
    code ends  
    end main  
    ```

## Ex.3 

```asm
comment @---------------------------------------------------------------------

从用户那里接收一行输入，并将其存储在数据段中定义的数组a里，然后输出这行输入

输入：用户可以输入任何字符串，例如“Hello, World!”。
输出：程序会输出用户输入的字符串，然后加上一个回车和一个换行，例如“Hello, World!”后跟一个回车和换行。

------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========

data segment  
a db 100 dup(0)  
data ends  
code segment  
assume cs:code, ds:data  
main:  
   mov ax, data  
   mov ds, ax  
   mov bx, 0  
; 请在 #1_begin 和 #1_end 之间补充代码实现功能：
; 接受用户的输入（以换行符结尾）并输出换行符+输出+空行
; #1_begin--------------------------------------
   
; #1_end========================================
output_done:  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```

服了，刷这题让我深刻意识到我昨天【如背】
用最原始的方法写了一坨史山，感觉好像上课例子也没什么特别的

??? tip "答案"
   ```
   comment @---------------------------------------------------------------------

   从用户那里接收一行输入，并将其存储在数据段中定义的数组a里，然后输出这行输入

   输入：用户可以输入任何字符串，例如“Hello, World!”。
   输出：程序会输出用户输入的字符串，然后加上一个回车和一个换行，例如“Hello, World!”后跟一个回车和换行。

   ------------------------------------------------------------------------------@

   ;==========请把以下代码保存到src\main.asm==============================
   ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========

   data segment  
   a db 100 dup(0)  
   data ends  
   code segment  
   assume cs:code, ds:data  
   main:  
      mov ax, data  
      mov ds, ax  
      mov bx, 0  
   ; 请在 #1_begin 和 #1_end 之间补充代码实现功能：
   ; 接受用户的输入（以换行符结尾）并输出换行符+输出+空行
   ; #1_begin--------------------------------------
   mov si, offset a
   push si
   input:
      mov ah,01h
      int 21h
      cmp al, 0Dh
      je input_done
      mov [si], al
      inc si
      jmp input
   input_done:
      mov bl, 0Dh
      mov [si], bl
      inc si
      mov bl, 0Ah
      mov [si], bl
      inc si
      pop si

      mov dl, 0Dh
      mov ah,02h
      int 21h
      mov dl,0Ah
      mov ah,02h
      int 21h
   output:
      mov dl, [si]
      cmp al, 0
      je output_done
      mov ah, 02h
      int 21h
      inc si
      jmp output
   ; #1_end========================================
   output_done:  
      mov ah, 4Ch  
      int 21h  
   code ends  
   end main  
   ```

## Ex.4


```asm
comment @---------------------------------------------------------------------

实现功能：2000个'A'
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========
code segment  
assume cs:code  
main:  
; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
; 输出两千个'A'
; #1_begin--------------------------------------

; #1_end========================================

   mov ah, 1  
   int 21h; 键盘输入，起到等待敲键的作用  
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```

这道题没什么，单纯记显卡中断，但我也忘了，服了  
回头把这题背出来!

??? tip "答案"
   ```asm
   comment @---------------------------------------------------------------------
   实现功能：2000个'A'
   ------------------------------------------------------------------------------@
   ;==========请把以下代码保存到src\main.asm==============================
   ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========
   code segment  
   assume cs:code  
   main:  
   ; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
   ; 输出两千个'A'
   ; #1_begin--------------------------------------
      mov ax, 0B800h
      mov es, ax
      mov al, 'A'
      mov ah, 71h
      mov cx, 2000
      mov di,0
   again:
      mov word ptr es:[di], ax
      add di,2
      loop again
   ; #1_end========================================
      mov ah,1
      int 21h
      mov ah, 4Ch  
      int 21h  
   code ends  
   end main  
   ```
   需要用Dosbox运行，结果大概长这样：
   ![alt text](image-3.png)

## Ex.5.

又是一道显卡，但这道题的亮点在于先`mov bx, 200h`,再利用`sub bx,1`来延时，很巧妙

```asm
comment @---------------------------------------------------------------------

实现功能：移动的'A'
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========
code segment  
assume cs:code  
main:  
; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
; 'A'移动2000次
; #1_begin--------------------------------------

; #1_end========================================
   mov ah,1
   int 21h
   mov ah, 4Ch  
   int 21h  
code ends  
end main  
```


??? tip "answer"
   ```asm
   comment @---------------------------------------------------------------------

   实现功能：移动的'A'
   ------------------------------------------------------------------------------@

   ;==========请把以下代码保存到src\main.asm==============================
   ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========
   code segment  
   assume cs:code  
   main:  
   ; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
   ; 'A'移动2000次
   ; #1_begin--------------------------------------
      mov ax, 0B800h
      mov es, ax

      mov cx, 2000
      mov di,0
      mov dx,0FFFh
   again:
      mov al, 'A'
      mov ah, 71h
      mov word ptr es:[di], ax
   waiting:
      sub dx,1
      cmp dx,0
      jne waiting
      xor ah, ah
      mov word ptr es:[di], ax
      add di,2
      loop again
   ; #1_end========================================
      mov ah,1
      int 21h
      mov ah, 4Ch  
      int 21h  
   code ends  
   end main  
   ```
   这版答案由于循环次数不够，A移动飞快，可以用双重循环增加一下循环次数  

## Ex.6.

```asm
comment @---------------------------------------------------------------------
在DOS环境下的图形模式下绘制一个红色的矩形，并等待用户按键后退出到文本模式
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========
code segment  
assume cs:code; cs不需要赋值会自动等于code  
main:  
   jmp begin  
i  dw 0  
begin:  
; 请在 #1_begin 和 #1_end 之间补充代码实现功能
; #1_begin--------------------------------------
   
; #1_end========================================
   mov ah,0  
   int 16h;bios键盘输入,类似int 21h的01h功能  
   mov ax, 0003h  
   int 10h; 切换到80*25文本模式  
   mov ah, 4Ch  
   int 21h  
code ends
```

又是显卡模式，背不出来一点……

这题直接抄答案了, 赌他不考显卡……几道显卡看看就可以了, 详见上一个文档    

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
## Ex.7.

嘿嘿这道我做出来了，只能说，三个栈一起真的……好！

```asm
comment @---------------------------------------------------------------------
将一个32位整数（x）的每一位数字转换为对应的十六进制字符，并显示在屏幕上
------------------------------------------------------------------------------@

;==========请把以下代码保存到src\main.asm==============================
;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========


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
; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
; #1_begin--------------------------------------

; #1_end========================================
   mov ah, 4Ch
   int 21h
code ends  
end main 
```

??? tip "答案"
   ```asm
   comment @---------------------------------------------------------------------
   将一个32位整数（x）的每一位数字转换为对应的十六进制字符，并输出
   ------------------------------------------------------------------------------@

   ;==========请把以下代码保存到src\main.asm==============================
   ;==========选中main.sh及src文件夹->右键->压缩成submit.zip提交==========


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
   ; 请在 #1_begin 和 #1_end 之间补充代码实现以下功能：
   ; #1_begin--------------------------------------
      xor ax,ax
      xor edx, edx
      mov cx,8
      mov edx, x
   pushin:
      push cx
      push edx
      and edx, 0000000Fh
      mov al,dl
      xlat 
      mov cl,4
      pop edx
      ror edx, cl
      pop cx
      push ax
      loop pushin
      mov cx,8
   popout:
      pop ax
      mov dl,al
      mov ah,02h
      int 21h
      loop popout
   ; #1_end========================================
      mov ah, 4Ch
      int 21h
   code ends  
   end main 
   ```

另一道`xlat`的题，感觉大同小异，就不写了

有些题感觉本身没什么意思，只是为了解释指令，就都跳过了

## Ex.8. 浮点数相关

死了，背吧

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

中断相关赌他不考了，平时作业里没有应该不会实验考，直接背好了

Lec9写一些hint:  

- 自我移动的代码：这个是讲解`cs`,`es`这些寄存器的赋值，所以要`td`才能看的出效果
- 短跳近跳远跳这个写的还蛮显然的  

## 作业题重做

!!! warning
   由于保密要求，只给相关的hint  
   我打算只做1、2、3、6  
   4、5给C代码了说明比较难，有空再写  

T1: 一道比较简单的栈，把例题刷完了基本很快就做完了

T2: 
