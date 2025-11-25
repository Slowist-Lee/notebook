# C++ 速通

> [!abstract]
> 感觉平时用的到的主要就是面向对象的一些知识还有STL了，简单看一下至少能手敲出一篇能跑的代码。
> 本文档只是 cheatsheet，用来让 Slow 翻一下代码该怎么写（x）

## 一、语法

```cpp
#include <iostream>    // Needed to perform IO operations
using namespace std;
 
int main() {                        // Program entry point
   cout << "hello, world" << endl;  // Say Hello
   return 0;                        // Terminate main()
}                                   // End of main function
```

## 二、面向对象

### 2.1 语法

类的成员函数可以在类内直接给出定义，也可以在类内只声明，在类外给出定义。

```cpp
class Foo {
    int x = 0;
    void foo(int v) { x += v; }
    void bar(int v);
};

void Foo::bar(int v) { x += v; }

int main() {
    Foo f;
    f.bar(1);  // Error: 'bar' is a private member of 'Foo'
}
```
### 2.2 访问控制

- C++ 里 class 里面默认 private, struct 默认 public。

声明方式：

```cpp
struct User {
private:
    int id, age;
    char* password;
public:
    bool checkPassword(char* pw); // check if pw == password
    void setAge(int v) {
        if (v >= 0)
            age = v;
    }
    int getAge() { return age; }
    // ...
};
```

### 2.3 继承和多态

```cpp
class Circle : public Shape {   // Circle 继承 Shape
public:
    int radius;     // 独有的成员变量

    void do_draw() {
        // 画圆！
    }
};

class Rectangle : public Shape { // Rectangle 继承 Shape
public:
    int width, height; // 独有的成员函数

    void do_draw() {
        // 画长方形！
    }
};
```

### 2.4 内联 inline

考虑编译器优化的时候需要考虑这个！[Tutorial](https://xuan-insr.github.io/cpp/cpp_restart/4_class_1/#-inline-%E5%87%BD%E6%95%B0)

### 2.5 构造函数

函数名和类名相同，会在创建对象的时候执行。**构造函数并没有名字，因此永远无法被用名字找到**。

![](Pasted%20image%2020251118193011.png)

可以传递参数：

```cpp
class Container {
    elem* val;
    // ...
public:
    Container(unsigned size = 512) { // 默认参数：512！
        val = (elem*)malloc(sizeof(elem) * size);
        // ...
    }
    // ...
};
```

调用的时候可以直接写： `Container c2(64);`。

**函数重载**：

```cpp
class Container {
    elem* val;
    // ...
public:
    Container() { val = nullptr; }
    Container(unsigned size) {
        val = (elem*)malloc(sizeof(elem) * size);
    }
    Container(unsigned size, elem initVal) {
        val = (elem*)malloc(sizeof(elem) * size);
        for (unsigned i = 0; i < size; i++) {    
            val[i] = initVal;
        }
    }
};
```

此时：使用 `Container c1, c2(4), c3(6, 2);` 定义三个对象时，会分别使用无参、一个参数和两个参数的构造函数。

Tips：独立函数也可以重载，重载规则比较复杂，具体需要查阅；

```cpp
double abs(double);
int abs(int);

abs(1);             // calls abs(int);
abs(1.0);           // calls abs(double);
```
### 2.6 New/Delete

1. `new` 表达式干的事情是申请内存 + 调用构造函数，返回一个指针；而 `delete` 表达式干的事情是调用析构函数 + 释放内存。

![](Pasted%20image%2020251118193254.png)

2. 如果 `p` 在 `new` 的时候创建的是单个对象，则应该用 `delete p;` 的形式 (single-object delete expression) 回收；如果 `p` 在 `new` 的时候创建的是数组，则应该用 `delete[] p;`

### 2.7 空指针

```cpp
void f(int *);
void f(int);

f(nullptr);   // f(int *) is called
```

