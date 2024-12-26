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