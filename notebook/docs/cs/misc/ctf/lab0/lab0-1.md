# javascript 如何使用Promise



```js
const fetchPromise = fetch(
  "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
);

console.log(fetchPromise);

fetchPromise.then((response) => {
  console.log(`已收到响应：${response.status}`);
});

console.log("已发送请求……");

```

复制到控制台，结果：

```text
Promise { <state>: "pending" }
已发送请求……
已收到响应：200
```

[`fetch()`](https://developer.mozilla.org/zh-CN/docs/Web/API/fetch "fetch()") API，一个现代的、基于 Promise 的、用于替代 `XMLHttpRequest` 的方法。

### .then(res => res.text())

这一行代码分为两个部分：`.then`方法和箭头函数。

1. **`.then`方法**:
    
    - `.then`是一个Promise对象的方法，用于定义在Promise成功（resolved）时要执行的操作。
    - `.then`方法接受一个回调函数作为参数，这个回调函数会在Promise解决时被调用。
2. **箭头函数 `res => res.text()`**:
    
    - 这是一个箭头函数（Arrow Function），它是ES6引入的一种简洁的定义函数的方式。
    - `res` 是箭头函数的参数，表示前一个Promise解决时传递的值（在这个例子中是一个Response对象）。
    - `res.text()` 是Response对象的方法，用于读取响应体并返回一个解析为文本的Promise。

综合起来，这行代码的意思是：

- 当fetch请求成功时，`then`会调用一个回调函数。
- 这个回调函数接受一个Response对象作为参数，并调用它的`text()`方法。
- `text()`方法返回一个Promise，该Promise解析为响应的文本。

### .then(res => alert(res))

这行代码的结构与上一行类似，也是由`.then`方法和箭头函数组成。

1. **`.then`方法**:
    - 与上面一样，`.then`定义在Promise成功时要执行的操作。
2. **箭头函数 `res => alert(res)`**:
    
    - 这是另一个箭头函数。
    - 这里的`res`是上一个Promise解决时传递的值（在这个例子中是解析后的文本字符串）。
    - `alert(res)` 调用浏览器的`alert`函数，弹出一个警告框显示`res`的值。

综合起来，这行代码的意思是：

- 当上一个Promise（由`res.text()`返回的Promise）成功解析为文本时，`then`会调用一个回调函数。
- 这个回调函数接受解析后的文本作为参数，并用`alert`函数在浏览器中弹出一个警告框显示该文本。

# request库里的session

请求会话
        使用requests.Session对象可以在多个请求之间保持会话，其HTTP请求方法与requests的请求方法一致。

requests.Session类
        提供一种持久性的会话，允许在多个请求之间保持cookie、header和连接池等配置参数的共享，这样可以重用同一连接，而不是为每个请求创建一个新的连接。

例1：基本用法

import requests

# 创建一个 Session 对象

session = requests.Session()

# 设置共享的 headers

session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

# 发送多个请求

url = 'https://www.example.com'

response1 = session.get(url)

response2 = session.post(url, data={'key': 'value'})

# 关闭 Session（可选）

session.close()

# 正则表达式

Python 的正则表达式是通过 `re` 模块实现的。使用正则表达式可以方便地处理字符串查找、匹配和替换等操作。下面是一些常用的正则表达式函数及示例：

1. **导入 `re` 模块**:
    ```python
    import re
    ```

2. **匹配**：
    - `re.match(pattern, string)`：从字符串的起始位置匹配一个模式。
    - `re.search(pattern, string)`：搜索整个字符串，找到第一个匹配的模式。
    - `re.findall(pattern, string)`：搜索整个字符串，返回所有非重叠的匹配模式。
    - `re.finditer(pattern, string)`：搜索整个字符串，返回一个迭代器，包含所有的匹配对象。

3. **替换**：
    - `re.sub(pattern, repl, string)`：在字符串中替换匹配的模式。

4. **编译**：
    - `re.compile(pattern)`：编译一个正则表达式模式，生成一个正则表达式对象，可以提高多次使用时的效率。

5. **常用模式**：
    - `.`：匹配除换行符外的任意字符。
    - `^`：匹配字符串的开头。
    - `$`：匹配字符串的结尾。
    - `*`：匹配前一个字符零次或多次。
    - `+`：匹配前一个字符一次或多次。
    - `?`：匹配前一个字符零次或一次。
    - `{m,n}`：匹配前一个字符至少 m 次，至多 n 次。
    - `[]`：匹配括号内的任意一个字符。
    - `\d`：匹配一个数字字符。
    - `\w`：匹配一个字母或数字字符。
    - `\s`：匹配一个空白字符。

下面是一些示例代码：

```python
import re

# 示例字符串
text = "Hello, my email is example@example.com and my website is https://www.example.com."

# 匹配电子邮件
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# 匹配URL
url_pattern = r'https?://[A-Za-z0-9./-]+'
urls = re.findall(url_pattern, text)
print("URLs found:", urls)

# 替换电子邮件
replaced_text = re.sub(email_pattern, '[EMAIL]', text)
print("Replaced text:", replaced_text)

# 使用 compile 进行多次匹配
compiled_pattern = re.compile(email_pattern)
match = compiled_pattern.search(text)
if match:
    print("First email found:", match.group())
```

上述代码展示了如何使用正则表达式匹配电子邮件和URL，以及如何替换文本中的匹配项。



这段代码 `r = re.findall(r"token=(.*)'", content)` 的作用是从 `content` 字符串中查找所有匹配 `token=` 后面跟随任意字符直到单引号 `'` 的子字符串，并将这些匹配的子字符串作为列表返回。

具体解释如下：

1. **`re.findall()`**：这是 `re` 模块中的一个函数，用于返回字符串中所有非重叠的匹配项。

2. **正则表达式模式 `r"token=(.*)'"`**：
    - `r""`：前缀 `r` 表示原始字符串，使得反斜杠不需要被转义。
    - `token=`：匹配字面字符串 `token=`。
    - `(.*)`：括号内的 `.*` 表示匹配任意字符（除换行符外）0次或多次，括号用于捕获分组，这意味着 `.*` 匹配到的内容会被提取出来。
    - `'`：匹配字面单引号 `'`。

3. **`content`**：这是一个包含要被搜索的文本的字符串变量。

综上所述，正则表达式 `r"token=(.*)'"` 用于匹配 `content` 中所有形如 `token=某些字符'` 的子字符串，并返回 `某些字符` 的部分作为列表。以下是一个具体示例：

```python
import re

content = "Here is a token=abc123' and another token=xyz789' in the text."
r = re.findall(r"token=(.*)'", content)
print(r)  # 输出: ['abc123', 'xyz789']
```

在这个示例中，`re.findall()` 查找所有 `token=` 后面跟随任意字符直到单引号 `'` 的子字符串，并返回匹配到的内容 `['abc123', 'xyz789']`。

反汇编结果

这个反汇编代码定义了一个 `verify` 函数，用于验证传入的密码是否符合特定规则。下面是对这个函数的详细解释：

```cpp
__int64 __fastcall verify(char *passwd)
{
  int v2; // ecx
  int v3; // r8d
  int v4; // r9d
  char v5; // [rsp+0h] [rbp-F0h]
  int i; // [rsp+18h] [rbp-D8h]
  char *table[14]; // [rsp+20h] [rbp-D0h]
  char tmp[64]; // [rsp+90h] [rbp-60h] BYREF
  unsigned __int64 v9; // [rsp+D8h] [rbp-18h]

  // 保存返回地址
  v9 = __readfsqword(0x28u);

  // 定义对比表
  table[0] = "1040";
  table[1] = "1040";
  table[2] = "1040";
  table[3] = "1968";
  table[4] = "1152";
  table[5] = "1680";
  table[6] = "1312";
  table[7] = "1616";
  table[8] = "1888";
  table[9] = "1616";
  table[10] = "1824";
  table[11] = "1840";
  table[12] = "1616";
  table[13] = "2000";

  // 如果密码长度不等于14，则返回1
  if ( j_strlen_ifunc(passwd) != 14 )
    return 1LL;

  // 初始化tmp数组
  memset(tmp, 0, sizeof(tmp));

  // 遍历每个字符
  for ( i = 0; i < (unsigned __int64)j_strlen_ifunc(passwd); ++i )
  {
    // 把当前字符的ASCII码乘以16，然后转换成字符串格式保存到tmp中
    sprintf((unsigned int)tmp, (unsigned int)"%d", 16 * passwd[i], v2, v3, v4, v5);

    // 如果tmp和table中的对应项不匹配，则返回1
    if ( (unsigned int)j_strcmp_ifunc(tmp, table[i]) )
      return 1LL;
  }

  // 如果所有字符都符合条件，则返回0
  return 0LL;
}
```

```c

__int64 __fastcall verify(char *passwd)
{
  int v2; // ecx
  int v3; // r8d
  int v4; // r9d
  char v5; // [rsp+0h] [rbp-F0h]
  int i; // [rsp+18h] [rbp-D8h]
  char *table[14]; // [rsp+20h] [rbp-D0h]
  char tmp[64]; // [rsp+90h] [rbp-60h] BYREF
  unsigned __int64 v9; // [rsp+D8h] [rbp-18h]

  v9 = __readfsqword(0x28u);
  table[0] = "1040";
  table[1] = "1040";
  table[2] = "1040";
  table[3] = "1968";
  table[4] = "1152";
  table[5] = "1680";
  table[6] = "1312";
  table[7] = "1616";
  table[8] = "1888";
  table[9] = "1616";
  table[10] = "1824";
  table[11] = "1840";
  table[12] = "1616";
  table[13] = "2000";
  if ( j_strlen_ifunc(passwd) != 14 )
    return 1LL;
  memset(tmp, 0, sizeof(tmp));
  for ( i = 0; i < (unsigned __int64)j_strlen_ifunc(passwd); ++i )
  {
    sprintf((unsigned int)tmp, (unsigned int)"%d", 16 * passwd[i], v2, v3, v4, v5);
    if ( (unsigned int)j_strcmp_ifunc(tmp, table[i]) )
      return 1LL;
  }
  return 0LL;
}
```



### 解释

1. **变量声明**：
   - `v2, v3, v4, v5`: 临时变量，可能用于保存某些寄存器的值。
   - `i`: 循环变量。
   - `table[14]`: 存储14个字符串的数组，每个字符串表示一个预期的值。
   - `tmp[64]`: 临时字符串数组，用于保存当前字符处理后的结果。
   - `v9`: 用于保存栈保护值，以防止栈溢出攻击。

2. **栈保护**：
   - `v9 = __readfsqword(0x28u);` 用于读取当前线程的栈保护值，以防止栈溢出攻击。

3. **初始化对比表**：
   - `table` 数组存储了一组预期的字符串值，这些值将用于与计算出的值进行对比。

4. **密码长度检查**：
   - `if ( j_strlen_ifunc(passwd) != 14 )`：如果输入密码的长度不是14，则返回1，表示验证失败。

5. **初始化临时数组**：
   - `memset(tmp, 0, sizeof(tmp));`：将`tmp`数组初始化为全零。

6. **字符处理和对比**：
   - 遍历密码的每个字符，将其ASCII码乘以16，然后转换为字符串格式，存储在`tmp`中。
   - `sprintf((unsigned int)tmp, (unsigned int)"%d", 16 * passwd[i], v2, v3, v4, v5);`：计算并格式化当前字符的值。
   - `if ( (unsigned int)j_strcmp_ifunc(tmp, table[i]) )`：如果`tmp`与`table`中的对应值不相等，返回1，表示验证失败。

7. **成功验证**：
   - 如果所有字符都通过验证，返回0，表示验证成功。

### 总结

该函数用于验证输入密码是否符合特定规则：长度为14，每个字符的ASCII码乘以16后的结果必须与预定义的字符串表中的值相匹配。如果不匹配，则返回1（验证失败）；如果匹配，则返回0（验证成功）。

![[Pasted image 20240703103006.png]]


![[Pasted image 20240703103120.png]]65 65 65 123  72 105 82 101  118 101 114 115 101 125

![[Pasted image 20240703103813.png]]
```bash
PS C:\Users\leexi> wsl cp /mnt/d/Desktop/crackme /home/slowist/
```

```bash
This message is shown once a day. To disable it please create the
/root/.hushlogin file.
root@Slowist:~# cd /home/slowist/
root@Slowist:/home/slowist# chmod +x crackme
root@Slowist:/home/slowist# ./crackme
Enter Password (or q to quit): AAA{HiReverse}
Access Granted
root@Slowist:/home/slowist#
```

![[Pasted image 20240703103800.png]]

[RSA算法](https://blog.csdn.net/qq_16763983/article/details/128101681?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171997634016800227459149%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171997634016800227459149&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-128101681-null-null.142^v100^pc_search_result_base8&utm_term=RSA%E5%8A%A0%E5%AF%86&spm=1018.2226.3001.4187)

# `Crypto.Util.number`:

`long_to_bytes` 是 `Crypto.Util.number` 模块中的一个函数，用于将一个长整数（long integer）转换为字节串（bytes）。这个函数通常用于加密和解密操作中，将数值形式的密文或明文转换为字节形式，以便进行进一步处理或传输。

举个例子，当你在处理RSA加密算法时，通常会涉及到大整数的运算。在一些情况下，你需要将这些大整数转换为字节串来进行处理或传输。`long_to_bytes` 就能派上用场。

以下是一个简单的示例：

```python
from Crypto.Util.number import long_to_bytes

# 假设我们有一个长整数
long_int = 12345678901234567890

# 使用 long_to_bytes 将其转换为字节串
byte_str = long_to_bytes(long_int)

print(byte_str)
```

这个代码会将长整数 `12345678901234567890` 转换为相应的字节串，并打印出来。这个字节串可以用于加密、解密或其他需要字节形式数据的操作。

总的来说，`long_to_bytes` 是一个在处理加密算法和大整数运算时非常有用的工具。

