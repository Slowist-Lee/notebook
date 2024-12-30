# Ch8 String
!!! abstract "说明"
    由于自学过，所以这里主要是查漏补缺。

## 一、 `<string.h>`相关函数

- `strncpy`：  
    - `strncpy(目标字符串,开始位置,复制长度)`
示例：
```c
for(int i=0;i<=slen-tlen+1;i++){
        strncpy(result,s+i,tlen);
        result[tlen]='\0';
        if(strcmp(result,t)==0){
            return &s[i];
        }
    }
```

## 二、字符串输入

!!! example "PTA-hw9-Ex7-4"
    Q: 如何将输入一行"Programming in C" 赋值给`books[i].name`?
    A: 善用`scanf("\n")`以及`scanf("%d\n)`
        ```c
        for(int i=0;i<n;i++){
            gets(books[i].name);
            scanf("%lf",&books[i].price);
            if(i!=n-1)
                scanf("\n");
        }
        ```


## 三、C程序中的字符串切片

利用指针取相应的字符串！(有空会整理的ww)

!!! example "例题 PTA 6-4 指定位置输出字符串"
    本题要求实现一个函数，对给定的一个字符串和两个字符，打印出给定字符串中从与第一个字符匹配的位置开始到与第二个字符匹配的位置之间的所有字符。  
    函数接口定义：`char *match( char *s, char ch1, char ch2 );`
    函数`match`应打印`s`中从`ch1`到`ch2`之间的所有字符，并且返回ch1的地址。  
    裁判测试程序样例：  
    ```c
    #include <stdio.h>
    #define MAXS 10
    char *match( char *s, char ch1, char ch2 );
    int main()
    {
        char str[MAXS], ch_start, ch_end, *p;
        
        scanf("%s\n", str);
        scanf("%c %c", &ch_start, &ch_end);
        p = match(str, ch_start, ch_end);
        printf("%s\n", p);
        return 0;
    }
    /* 你的代码将被嵌在这里 */
    ```
    
    输入样例1：
    ```
    program
    r g
    ```
    输出样例1：
    ```
    rog
    rogram
    ```
    输入样例2：
    ```
    program
    z o
    ```
    输出样例2：
    ```
    (空行)
    (空行)
    ```
    输入样例3：
    ```
    program
    g z
    ```
    输出样例3：
    ```
    gram
    gram
    ```


??? info "Answer"
    ```c
    #include<string.h>
    char *match( char *s, char ch1, char ch2 ){
        int len=strlen(s);
        int begin=0;
        int index=-1;
        for(int i=0;i<len;i++){
            if(begin==0 && s[i]==ch1){
                index=i;
                begin=1;
            }
            if(begin==1 && s[i]==ch2){
                printf("%c",ch2);
                break;
            }
            if(begin==1){
                printf("%c",s[i]);
            }
        }
        char *sub = &s[index];
        printf("\n");
        if(index==-1){
            return "\0";
        }
        else{
            return sub;
        }
    }
    ```