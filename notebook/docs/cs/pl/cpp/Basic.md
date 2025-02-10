# C++ 语法基础

案例程序：

```cpp
#include <iostream>    // Needed to perform IO operations
using namespace std;
 
int main() {                        // Program entry point
   cout << "hello, world" << endl;  // Say Hello
   return 0;                        // Terminate main()
}                                   // End of main function
```

编译：(Linux)

```bash
g++ -o hello hello.cpp
$ ./hello
```

输出：

在 C++ 中，输出到显示控制台是通过“`cout`”和流插入（或 put-to）运算符`<<`完成的。
可以通过使用`<<`运算符链接项目，将任意数量的项目打印到`cout`中。
特殊符号 endl（END-of-Line）来生成换行符

```cpp
cout << "hello" << " world, " << "again!" << endl;
cout << "hello," << endl << "one more time. " << endl << 5 << 4 << 3 << " " << 2.2 << " " << 1.1 << endl;
```

```text
hello world, again!
hello,
one more time.
543 2.2 1.1
_
```
