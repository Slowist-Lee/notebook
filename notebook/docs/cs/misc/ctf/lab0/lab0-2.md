

pwn 

Many settings in `pwntools` are controlled via the global variable [`context`](https://docs.pwntools.com/en/latest/context.html#pwnlib.context.context "pwnlib.context.context"), such as the selected target operating system, architecture, and bit-width.

In general, exploits will start with something like:
```python
from pwn import *
context.arch = 'amd64'
```

Which sets up everything in the exploit for exploiting a 64-bit Intel binary.

在pwntools中，“context”对象用于配置影响工具和函数行为的各种设置。这包括目标体系结构、操作系统、位宽等的设置。
当您在脚本中看到“context.arch='amd64'”时，它将架构设置为amd64（也称为x86_64），这是x86指令集架构的64位版本。这对于利用漏洞的正确工作至关重要，因为目标二进制文件很可能是为此体系结构编译的。

-------

在pwntools中，使用`context.binary`是一个推荐的方法，因为它可以自动设置所有相关的值。这意味着pwntools会自动根据提供的二进制文件来配置适当的环境参数，例如架构（`arch`）、操作系统（`os`）和位宽（`bits`）。这样可以减少手动配置的工作量，并且避免配置错误。

当你写：

```python
from pwn import *
context.binary = './challenge-binary'
```

这行代码的含义是：

1. **自动检测架构和位宽**：pwntools会解析提供的二进制文件（在这个例子中是`./challenge-binary`），并自动设置适当的架构（比如`i386`或`amd64`）和位宽（32位或64位）。这样可以确保后续的代码操作都基于正确的环境设置。
  
2. **简化配置过程**：你不再需要手动设置`context.arch`、`context.bits`和其他相关参数，因为pwntools会自动完成这些设置。这样可以减少出错的可能性，并且使代码更加简洁和易读。

3. **提高代码的可移植性**：通过使用`context.binary`，你的代码可以更容易地适应不同的二进制目标文件。你只需要更改二进制文件的路径，而无需调整其他配置参数。

具体示例如下：

```python
from pwn import *

# 设置目标二进制文件，这将自动配置架构、位宽等参数
context.binary = './challenge-binary'

# 后续的利用代码
# ...

# 例如，生成与目标二进制文件相匹配的shellcode
shellcode = asm(shellcraft.sh())
```

总结来说，使用`context.binary`的主要优点是自动化配置和减少人为错误，使得利用编写更加高效和可靠。

--------

# 使用pwn实现Sockets连接

## `remote()`:

一个很简单的示例
```python
r = remote('10.214.160.13',11002)
```


`remote()`函数的参数如下：
### 参数解释

以下是 `remote` 类的主要参数和它们的含义：

- `host (str)`：要连接的远程主机地址（例如域名或IP地址）。
- `port (int)`：要连接的端口号。
- `fam`：指定地址族，可以是字符串 "any"、"ipv4" 或 "ipv6"，也可以是传递给 `socket.getaddrinfo()` 的整数。
- `typ`：指定协议类型，可以是字符串 "tcp" 或 "udp"，也可以是传递给 `socket.getaddrinfo()` 的整数。
- `timeout`：指定连接超时时间，可以是一个正数，`None` 或字符串 "`default`"。
- `ssl (bool)`：如果为 `True`，则使用 SSL 来包装套接字。
- `ssl_context (ssl.SSLContext)`：指定用于包装套接字的 SSLContext。
- `sni`：根据主机参数设置 `ssl_args` 中的 `server_hostname`。
- `sock (socket.socket)`：如果提供了现有的套接字，则使用它而不是新建连接。
- `ssl_args (dict)`：传递给 `ssl.wrap_socket` 的命名参数字典。

# `listen()`

`pwnlib.tubes.listen.listen` 是 pwntools 中用于创建监听套接字的类。这个类可以创建 TCP 或 UDP 套接字来接收数据，并且支持 IPv4 和 IPv6。在使用监听套接字之前，需要调用 `wait_for_connection()` 方法来等待连接的到来。

### 参数解释

- `port (int)`：监听的端口号。默认值为 0，表示由操作系统自动选择一个端口。
- `bindaddr (str)`：绑定的地址。默认值为 `::`（所有 IPv6 地址）。也可以使用 `0.0.0.0` 来表示所有 IPv4 地址。
- `fam`：指定地址族，可以是字符串 "any"、"ipv4" 或 "ipv6"，也可以是传递给 `socket.getaddrinfo()` 的整数。
- `typ`：指定协议类型，可以是字符串 "tcp" 或 "udp"，也可以是传递给 `socket.getaddrinfo()` 的整数。

### 示例讲解

#### 示例 1：简单的本地监听和连接

```python
from pwn import *

# 在本地的 1234 端口上创建监听套接字
l = listen(1234)

# 创建一个到本地 1234 端口的远程连接
r = remote('localhost', l.lport)

# 等待连接的到来
_ = l.wait_for_connection()

# 通过监听套接字发送数据
l.sendline(b'Hello')

# 通过远程连接接收数据
response = r.recvline()
print(response)  # 输出：b'Hello\n'
```

在这个示例中：
1. `l = listen(1234)`：创建一个在本地 1234 端口监听的套接字。
2. `r = remote('localhost', l.lport)`：创建一个连接到本地 1234 端口的远程连接。
3. `_ = l.wait_for_connection()`：等待连接的到来。
4. `l.sendline(b'Hello')`：通过监听套接字发送数据。
5. `response = r.recvline()`：通过远程连接接收数据并输出。

#### 示例 2：监听并启动进程

```python
from pwn import *

# 创建一个监听套接字
l = listen()

# 启动一个 /bin/sh 进程，并将其 I/O 重定向到监听套接字
l.spawn_process('/bin/sh')

# 创建一个到监听端口的远程连接
r = remote('127.0.0.1', l.lport)

# 通过远程连接发送命令
r.sendline(b'echo Goodbye')

# 接收并打印命令输出
response = r.recvline()
print(response)  # 输出：b'Goodbye\n'
```

在这个示例中：
1. `l = listen()`：创建一个监听套接字（端口由操作系统自动选择）。
2. `l.spawn_process('/bin/sh')`：启动一个 `/bin/sh` 进程，并将其输入和输出重定向到监听套接字。
3. `r = remote('127.0.0.1', l.lport)`：创建一个连接到本地监听端口的远程连接。
4. `r.sendline(b'echo Goodbye')`：通过远程连接发送命令。
5. `response = r.recvline()`：接收并输出命令的结果。

#### 示例 3：使用 IPv6 进行通信

```python
from pwn import *

# 创建一个默认配置的监听套接字，支持 IPv6
l = listen()

# 创建一个到 IPv6 本地地址的远程连接
r = remote('::1', l.lport)

# 等待连接的到来
_ = l.wait_for_connection()

# 通过远程连接发送数据
r.sendline(b'Bye-bye')

# 通过监听套接字接收数据
response = l.recvline()
print(response)  # 输出：b'Bye-bye\n'
```

在这个示例中：
1. `l = listen()`：创建一个默认配置的监听套接字，支持 IPv6（端口由操作系统自动选择）。
2. `r = remote('::1', l.lport)`：创建一个连接到本地 IPv6 地址的远程连接。
3. `_ = l.wait_for_connection()`：等待连接的到来。
4. `r.sendline(b'Bye-bye')`：通过远程连接发送数据。
5. `response = l.recvline()`：通过监听套接字接收数据并输出。

### 总结

`pwnlib.tubes.listen.listen` 类提供了一种方便的方法来创建监听套接字，用于接受远程连接和数据。通过示例可以看出，它可以处理不同协议和地址族的连接，适用于多种网络通信场景。

-----------

# `recvlines()`函数


> 相应的 `recvline()`接受一个空行

`recvlines(numlines, keepends=False, timeout=default)` 是 pwntools 中一个用于接收多行数据的函数。这个函数会尝试接收最多 `numlines` 行数据，每行数据是由换行符（默认为 `\n`）分隔的字节序列。函数返回一个包含接收到的字节对象的列表。

### 参数解释

- `numlines (int)`：要接收的最大行数。
- `keepends (bool)`：是否保留每行末尾的换行符（默认为 `False`，即不保留）。
- `timeout (int)`：接收数据的最大超时时间（单位：秒）。如果在超时时间内未能满足请求，函数会将所有数据缓冲并返回空字符串 `''`。

### 异常处理

- 如果在请求满足之前连接关闭，会抛出 `EOFError` 异常。

### 返回值

- 返回一个包含从套接字接收到的字节对象的列表。如果在等待时发生超时，会返回空字符串 `''`。

### 使用示例

```python
from pwn import *

# 创建一个 tube 对象
t = tube()

# 模拟接收空行
t.recv_raw = lambda n: b'\n'
print(t.recvlines(3))  # 输出: [b'', b'', b'']

# 模拟接收实际数据行
t.recv_raw = lambda n: b'Foo\nBar\nBaz\n'
print(t.recvlines(3))  # 输出: [b'Foo', b'Bar', b'Baz']
print(t.recvlines(3, True))  # 输出: [b'Foo\n', b'Bar\n', b'Baz\n']
```

在这个示例中：
1. `t.recv_raw = lambda n: b'\n'`：模拟每次调用 `recv_raw` 时返回一个换行符。
2. `t.recvlines(3)`：接收三行数据，返回 `[b'', b'', b'']`，每行是一个空行。
3. `t.recv_raw = lambda n: b'Foo\nBar\nBaz\n'`：模拟每次调用 `recv_raw` 时返回包含三行数据的字节串。
4. `t.recvlines(3)`：接收三行数据，返回 `[b'Foo', b'Bar', b'Baz']`，不保留末尾的换行符。
5. `t.recvlines(3, True)`：接收三行数据，返回 `[b'Foo\n', b'Bar\n', b'Baz\n']`，保留末尾的换行符。

### 相关函数

- `recvlinesS(numlines, keepends=False, timeout=default)`：这个函数与 `recvlines()` 类似，但会将接收到的字节解码为字符串。使用时会调用 `context.encoding()` 方法进行解码。
  
  ```python
  t = tube()
  t.recv_raw = lambda n: b'\n'
  print(t.recvlinesS(3))  # 输出: ['', '', '']
  
  t.recv_raw = lambda n: b'Foo\nBar\nBaz\n'
  print(t.recvlinesS(3))  # 输出: ['Foo', 'Bar', 'Baz']
  ```

- `recvlinesb(numlines, keepends=False, timeout=default)`：这个函数与 `recvlines()` 类似，但返回 `bytearray` 对象的列表。

  ```python
  t = tube()
  t.recv_raw = lambda n: b'\n'
  print(t.recvlinesb(3))  # 输出: [bytearray(b''), bytearray(b''), bytearray(b'')]
  
  t.recv_raw = lambda n: b'Foo\nBar\nBaz\n'
  print(t.recvlinesb(3))  # 输出: [bytearray(b'Foo'), bytearray(b'Bar'), bytearray(b'Baz')]
  ```

### 总结

`recvlines()` 及其相关函数提供了便捷的方法从套接字中接收多行数据，无论是字节、字符串还是 `bytearray`，都可以通过这些函数来实现高效的数据接收和处理。


`p.recvlines(3)` 接受三个空行，不返回

# `recvuntil()`

在 pwntools 中，`recvuntil()` 方法用于从一个套接字或类似对象中接收数据，直到遇到指定的结束标记为止。这个方法常用于处理交互式的网络通信，比如从远程服务接收数据直到某个特定的字符串出现。

### 基本用法

```python
data = tube.recvuntil(delim, drop=False, timeout=default)
```

### 参数解释

- `delim`：要接收的终止标记，可以是一个字节串。
- `drop`：布尔值，是否丢弃终止标记（默认为 `False`，即保留终止标记）。
- `timeout`：超时时间（单位：秒）。如果在指定时间内未接收到终止标记，将引发超时。

### 返回值

返回从套接字接收到的数据（包括或不包括终止标记，取决于 `drop` 参数）。

### 异常处理

- 如果在超时时间内未接收到终止标记，会抛出 `TimeoutError` 异常。
- 如果连接在接收数据前关闭，会抛出 `EOFError` 异常。

### 示例代码

以下是一个使用 `recvuntil()` 的简单示例：

```python
from pwn import *

# 假设我们有一个本地的进程或远程服务
# 这里为了演示，使用一个本地进程
p = process('/bin/sh')

# 发送命令
p.sendline(b'echo Hello, World!')

# 接收直到遇到换行符
data = p.recvuntil(b'\n')
print(data)  # 输出: b'echo Hello, World!\n'

# 接收下一行数据
data = p.recvuntil(b'\n')
print(data)  # 输出: b'Hello, World!\n'
```

### 更复杂的示例

假设你在和一个远程服务通信，服务会在发送特定数据后返回一个提示符：

```python
from pwn import *

# 连接到远程服务
r = remote('example.com', 1337)

# 发送一些数据
r.sendline(b'GET /')

# 接收直到看到 HTTP 响应头的结束标记
response = r.recvuntil(b'\r\n\r\n')
print(response)

# 发送更多数据
r.sendline(b'Another request')

# 接收直到特定的提示符
prompt = r.recvuntil(b'prompt>')
print(prompt)

# 关闭连接
r.close()
```

在这个示例中：

1. `r = remote('example.com', 1337)`：连接到远程服务。
2. `r.sendline(b'GET /')`：发送 HTTP GET 请求。
3. `response = r.recvuntil(b'\r\n\r\n')`：接收到 HTTP 响应头的结束标记（空行）。
4. `r.sendline(b'Another request')`：发送另一个请求。
5. `prompt = r.recvuntil(b'prompt>')`：接收到特定的提示符。
6. `r.close()`：关闭连接。

### 小结

`recvuntil()` 是一个非常有用的函数，适合在需要等待特定标记的网络通信中使用。注意处理超时和连接关闭的异常，以确保程序的鲁棒性。

# 注意

在 Python 中，前面的 `b` 表示这是一个字节串（`bytes` 对象），而不是一个普通的字符串（`str` 对象）。在网络通信和许多系统级操作中，数据通常以字节形式发送和接收，因此使用字节串是很常见的做法。

### 字节串与普通字符串的区别

- **普通字符串（`str` 对象）**：
  - 用于表示文本数据，内部使用 Unicode 编码。
  - 可以直接使用普通引号 `'...'` 或双引号 `"..."` 表示。
  - 例如：`"Hello, World!"`

- **字节串（`bytes` 对象）**：
  - 用于表示二进制数据或特定编码的文本数据。
  - 需要在字符串前面加上 `b` 前缀。
  - 例如：`b"Hello, World!"`

### 为什么在网络通信中使用字节串

1. **协议要求**：许多网络协议（如 HTTP、TCP/IP 等）规定数据在传输时以字节形式编码，因此需要使用字节串。
2. **编码控制**：字节串允许你明确指定和控制数据的编码方式（如 UTF-8、ASCII 等），避免因默认编码不同而导致的问题。
3. **高效处理**：字节串在处理二进制数据时更高效，适用于处理图片、视频、文件等非文本数据。

### 示例

以下是一个简单的示例，演示了如何在 Python 中使用字节串进行网络通信：

```python
from pwn import *

# 连接到远程服务
r = remote('example.com', 1337)

# 发送字节串
r.sendline(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')

# 接收直到看到 HTTP 响应头的结束标记
response = r.recvuntil(b'\r\n\r\n')
print(response.decode('utf-8'))  # 解码并打印响应

# 关闭连接
r.close()
```

在这个示例中：

1. `r.sendline(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')`：发送一个 HTTP GET 请求，所有数据都以字节串形式发送。
2. `response = r.recvuntil(b'\r\n\r\n')`：接收数据直到遇到 HTTP 响应头的结束标记，所有接收到的数据也是字节串。
3. `print(response.decode('utf-8'))`：将接收到的字节串解码为字符串，以便打印和阅读。

### 总结

在使用 `pwntools` 或进行任何形式的网络通信时，处理的数据通常是字节串（`bytes` 对象）。在字符串前面加上 `b` 前缀可以明确表示这是一个字节串，确保在发送和接收数据时不会出现编码问题。

![[Pasted image 20240702211106.png]]

![[Pasted image 20240702211120.png]]

```text

recvuntil(_delims_, _drop=False_, _timeout=default_)→ [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.12)")[[source]](https://github.com/Gallopsled/pwntools/blob/a366e91038/pwnlib/tubes/tube.py#L281-L369)[](https://docs.pwntools.com/en/latest/tubes.html#pwnlib.tubes.tube.tube.recvuntil "Permalink to this definition")

Receive data until one of delims is encountered.

If the request is not satisfied before `timeout` seconds pass, all data is buffered and an empty string (`''`) is returned.

Parameters

- **delims** ([_bytes_](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.12)")_,_[_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.12)")) – Byte-string of delimiters characters, or list of delimiter byte-strings.
    
- **drop** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")) – Drop the ending. If `True` it is removed from the end of the return value.
    

Raises

**exceptions.EOFError** – The connection closed before the request could be satisfied

Returns

A string containing bytes received from the socket, or `''` if a timeout occurred while waiting.

Examples

>>> t = tube()
>>> t.recv_raw = lambda n: b"Hello World!"
>>> t.recvuntil(b' ')
b'Hello '
>>> _=t.clean(0)
>>> # Matches on 'o' in 'Hello'
>>> t.recvuntil((b' ',b'W',b'o',b'r'))
b'Hello'
>>> _=t.clean(0)
>>> # Matches expressly full string
>>> t.recvuntil(b' Wor')
b'Hello Wor'
>>> _=t.clean(0)
>>> # Matches on full string, drops match
>>> t.recvuntil(b' Wor', drop=True)
b'Hello'

>>> # Try with regex special characters
>>> t = tube()
>>> t.recv_raw = lambda n: b"Hello|World"
>>> t.recvuntil(b'|', drop=True)
b'Hello'

recvuntilS(_*a_, _**kw_)[[source]](https://github.com/Gallopsled/pwntools/blob/a366e91038/pwnlib/tubes/tube.py#L1497-L1498)[](https://docs.pwntools.com/en/latest/tubes.html#pwnlib.tubes.tube.tube.recvuntilS "Permalink to this definition")

Same as [`recvuntil()`](https://docs.pwntools.com/en/latest/tubes.html#pwnlib.tubes.tube.tube.recvuntil "pwnlib.tubes.tube.tube.recvuntil"), but returns a str, decoding the result using context.encoding. (note that the binary versions are way faster)

recvuntilb(_*a_, _**kw_)[[source]](https://github.com/Gallopsled/pwntools/blob/a366e91038/pwnlib/tubes/tube.py#L1495-L1496)[](https://docs.pwntools.com/en/latest/tubes.html#pwnlib.tubes.tube.tube.recvuntilb "Permalink to this definition")

Same as [`recvuntil()`](https://docs.pwntools.com/en/latest/tubes.html#pwnlib.tubes.tube.tube.recvuntil "pwnlib.tubes.tube.tube.recvuntil"), but returns a bytearray

```

# `Send()`函数

![[Pasted image 20240702211153.png]]
![[Pasted image 20240702211211.png]]

# `shutdown()`

![[Pasted image 20240702211222.png]]

# `interactive()`

![[Pasted image 20240702211305.png]]

# Basic使用

https://docs.pwntools.com/en/latest/commandline.html

`nc 10.214.160.13 11002`


# 定义一个字节串

b_str = b"Hello, World!"

# 将字节串解码为字符串（默认使用 UTF-8 编码）
decoded_str = b_str.decode()
print(decoded_str)  # 输出: Hello, World!

# 使用其他编码进行解码
b_str_utf16 = b"\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00\x00\x00"
decoded_str_utf16 = b_str_utf16.decode('utf-16')
print(decoded_str_utf16)  # 输出: Hello, World!

# 处理解码错误
b_str_error = b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00'
decoded_str_error = b_str_error.decode('utf-8', errors='ignore')
print(decoded_str_error)  # 输出: Hello, World!

# eval 使用

在 Python 中，`eval()` 函数用于执行一个字符串表达式，并返回表达式的结果。其基本用法如下：

```python
result = eval(expression, globals=None, locals=None)
```

### 参数解释

- `expression`：这是要计算的表达式，必须是一个字符串。
- `globals`：可选参数，表示全局命名空间。
- `locals`：可选参数，表示局部命名空间。

### 基本用法示例

```python
# 计算一个简单的数学表达式
expression = "2 + 3 * 4"
result = eval(expression)
print(result)  # 输出: 14

# 使用变量
x = 10
expression = "x + 20"
result = eval(expression)
print(result)  # 输出: 30

# 使用函数
def square(n):
    return n * n

expression = "square(5)"
result = eval(expression)
print(result)  # 输出: 25
```

### 使用 `globals` 和 `locals` 参数

`globals` 和 `locals` 参数允许你控制表达式的命名空间，可以用来限制表达式的访问范围，提高安全性。

```python
# 定义一个全局变量
a = 10
expression = "a + b"

# 只传递必要的全局变量
result = eval(expression, {"a": a, "b": 5})
print(result)  # 输出: 15

# 定义一个局部变量
def foo():
    x = 5
    expression = "x + 2"
    result = eval(expression, {}, {"x": x})
    print(result)  # 输出: 7

foo()
```

### 安全性注意事项

`eval()` 函数可以执行任意的字符串代码，这意味着如果使用不当，可能会带来安全风险。因此，在使用 `eval()` 时要非常小心，特别是当处理来自不可信源的数据时。为此，可以通过设置受限的 `globals` 和 `locals` 来减少潜在的危险。

```python
# 一个不安全的示例，来自用户的输入
user_input = "__import__('os').system('ls')"
# 不建议执行这种代码，因为它可能执行恶意操作
# result = eval(user_input)

# 一个更安全的做法
safe_globals = {"__builtins__": None}
safe_locals = {"x": 2, "y": 3}
user_input = "x + y"
result = eval(user_input, safe_globals, safe_locals)
print(result)  # 输出: 5
```

### 总结

`eval()` 是一个强大的函数，可以执行动态生成的代码，但由于其潜在的安全风险，必须谨慎使用。确保你完全信任并控制传递给 `eval()` 的表达式，或使用受限的命名空间来减少风险。


在 Python 中，`encode()` 函数用于将字符串（`str` 对象）编码为字节串（`bytes` 对象）。这个函数与 `decode()` 函数相对应，用于将字符串按照指定的编码方式转换为字节形式。

### 基本用法

```python
encoded_bytes = str_object.encode(encoding='utf-8', errors='strict')
```

### 参数解释

- `encoding`：要使用的编码格式，默认是 'utf-8'。常见的编码格式包括 'utf-8'、'ascii'、'latin-1' 等。
- `errors`：可选参数，指定如何处理编码错误。默认值是 'strict'，表示遇到错误时会抛出 `UnicodeEncodeError` 异常。其他常见选项包括 'ignore'（忽略错误）、'replace'（用替代字符替换错误）等。

### 返回值

返回一个字节串（`bytes` 对象），即编码后的数据。

### 示例

以下是一些使用 `encode()` 方法的示例：

#### 基本示例

```python
# 定义一个字符串
s = "Hello, World!"

# 使用 UTF-8 编码将字符串编码为字节串
encoded_s = s.encode('utf-8')
print(encoded_s)  # 输出: b'Hello, World!'

# 使用 ASCII 编码将字符串编码为字节串
encoded_s_ascii = s.encode('ascii')
print(encoded_s_ascii)  # 输出: b'Hello, World!'
```

#### 处理编码错误

```python
# 定义一个包含非 ASCII 字符的字符串
s = "Hello, 世界!"

# 使用 ASCII 编码会引发 UnicodeEncodeError
try:
    encoded_s_ascii = s.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Encoding error: {e}")

# 使用 'ignore' 参数忽略编码错误
encoded_s_ignore = s.encode('ascii', errors='ignore')
print(encoded_s_ignore)  # 输出: b'Hello, !'

# 使用 'replace' 参数用替代字符替换错误
encoded_s_replace = s.encode('ascii', errors='replace')
print(encoded_s_replace)  # 输出: b'Hello, ????!'
```

### 使用场景

1. **网络通信**：在网络编程中，数据通常以字节形式发送和接收，因此需要将字符串编码为字节串。
2. **文件处理**：在读写二进制文件时，可能需要将字符串编码为字节串。
3. **数据存储**：在某些数据库或数据存储系统中，可能需要以字节形式存储字符串数据。

### 示例应用：网络通信

以下是一个使用 `encode()` 和 `send()` 方法进行网络通信的示例：

```python
from pwn import *

# 连接到远程服务
r = remote('example.com', 1337)

# 定义一个要发送的字符串
message = "GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n"

# 将字符串编码为字节串
encoded_message = message.encode('utf-8')

# 发送字节串
r.send(encoded_message)

# 接收响应
response = r.recv()
print(response.decode('utf-8'))  # 解码并打印响应

# 关闭连接
r.close()
```

在这个示例中：

1. 将字符串 `message` 编码为 UTF-8 字节串。
2. 使用 `send()` 方法发送编码后的字节串。
3. 接收响应并解码为字符串以便打印和阅读。

### 总结

`encode()` 方法是将字符串转换为字节串的标准方法，在处理网络通信、文件读写和数据存储时非常有用。了解和使用编码和解码方法是处理文本和二进制数据的关键。

![[Pasted image 20240702220947.png]]

`AAA{gr3@t_J08!_let'5_P1@y_m1SC_TOG3Th3R}`

![[Pasted image 20240702234751.png]]


为什么我的curl只有这么点？

```bash
StatusCode        : 200
StatusDescription : OK
Content           :
                    <!DOCTYPE html>
                    <html>

                    <head>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist
                    /css/bootstrap.min.css" rel="stylesheet"
                            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1zt...
RawContent        : HTTP/1.1 200 OK
                    Pragma: no-cache
                    Vary: Accept-Encoding
                    Keep-Alive: timeout=5, max=100
                    Connection: Keep-Alive
                    Content-Length: 1907
                    Cache-Control: no-store, no-cache, must-revalidate
                    Content-Type...
Forms             : {}
Headers           : {[Pragma, no-cache], [Vary, Accept-Encoding], [Keep-Alive, timeou
                    t=5, max=100], [Connection, Keep-Alive]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 1907

```

![[Pasted image 20240703091059.png]]