# Pwn Note-1

!!! abstract
    第一讲笔记，都没听懂，细细碎碎的。

## Slide

### Basic

<object data="basic-1.pdf" type="application/pdf" width="100%" height="800">
    <embed src="basic-1.pdf" type="application/pdf" />
</object>

### Advance

<object data="advance-1.pdf" type="application/pdf" width="100%" height="800">
    <embed src="advance-1.pdf" type="application/pdf" />
</object>

## Note

- 注意：除数除0，位数溢出等等

漏洞：没有exit

from pwn import *
context-log_level="DEBUG"
context.arch="amd64"
p=process("./login_me")
print(p.recv())

system的地方

溢出函数/后门函数的地址
正常情况下储存在rbp+\\x08

checksec：（pwntools指令中的）
->软件开了什么级别的保护

若开启了EDA保护，函数会到随机位置