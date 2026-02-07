当然，这很简单。我已经为您在每个代码块的前后都插入了一个空行，以提高可读性。

# JS ES6 特性

## 一、关键字

### 1.1 `let` 和 `var`

`let` 声明的变量不允许在同一个作用域内被重复声明。

> [!danger] `let` 不可重复声明
> 因此以下程序会报错：
>
> ```js
> let camper = "James";
> let camper = "David"; // 报错
> ```
>

`var` 的定义与其他语言类似。`let` 可以在一个表达式（expression）、块（block）或全局（globe）中定义。

> [!warning] `var` 在循环中的问题
> 在 `for` 循环中使用 `var` 定义的迭代变量，如果其被一个函数闭包引用，那么这个函数将始终引用该变量的最终值，而不是创建函数时的值。
>
> ```js
> var printNumTwo;
> for (var i = 0; i < 3; i++) {
>   if (i === 2) {
>     printNumTwo = function() {
>       return i;
>     };
>   }
> }
> console.log(printNumTwo());
> ```
>
> 这里控制台将显示值 `3`。因为函数返回的是全局变量 `i` 的最终值。
>
> `let` 解决了这个问题，因为它具有块级作用域：
>
> ```js
> let printNumTwo;
> for (let i = 0; i < 3; i++) {
>   if (i === 2) {
>     printNumTwo = function() {
>       return i;
>     };
>   }
> }
> console.log(printNumTwo());
> console.log(i);
> ```
>
> 这里控制台将显示值 `2`，并且因为 `i` 只在 `for` 循环内有效，所以会抛出一个错误 `i is not defined`。

### 1.2 `const`

`const` 用于声明一个只读的常量。

-   对于**原始类型**（数字、字符串、布尔值）：值不可被修改（read-only）。
-   对于**对象类型**（数组、对象、函数）：变量所指向的内存地址不能被改变，但对象内部的属性值可以被修改。

> [!example] `const` 与对象类型
>
> 重新给 `const` 声明的数组赋值会导致错误：
>
> ```js
> const s = [5, 6, 7];
> s = [1, 2, 3]; // 这会导致一个错误
> ```
>
> 但是修改数组内部的元素是允许的：
>
> ```js
> const s = [5, 6, 7];
> s[0] = 45; // 不会报错
> console.log(s); // 输出 [45, 6, 7]
> ```
>

## 二、语法糖

### 2.1 使用箭头函数编写简洁的匿名函数

在 JavaScript 中，我们经常创建内联函数（inline functions），特别是在将函数作为参数传递时。ES6 提供了**箭头函数**语法，使其更加简洁。

> [!note] 从普通函数到箭头函数
> **ES5 语法：**
>
> ```javascript
> const myFunc = function() {
>   const myVar = "value";
>   return myVar;
> };
> ```
>
> **ES6 箭头函数语法：**
>
> ```javascript
> const myFunc = () => {
>   const myVar = "value";
>   return myVar;
> };
> ```
>

> [!question] 花括号啥时候用
> 没有返回值或者不只是返回值的时候经常用`{}`！
> 例如：
> 
> ```js
> watch(count, function(newCount) {console.log('new count is: ${newCount}')})
> ```


> [!tip] 单行箭头函数
> 当函数体只有一个返回值时，可以省略 `return` 关键字和花括号 `{}`。
>
> ```javascript
> const myFunc = () => "value"; // 该函数会返回字符串 "value"
> ```
>

> [!info] 箭头函数与参数
>
> - **单个参数**：可以省略参数外围的括号。
>
> ```js
> const doubler = item => item * 2;
> doubler(4); // 返回 8
> ```
>
> - **多个参数**：需要使用括号。
>
> ```javascript
> const multiplier = (item, multi) => item * multi;
> multiplier(4, 2); // 返回 8
> ```
>
> - **默认参数**：可以为参数提供默认值。
>
> ```js
> const greeting = (name = "Anonymous") => "Hello " + name;
>
> console.log(greeting("John")); // 输出: Hello John
> console.log(greeting());       // 输出: Hello Anonymous
> ```
>
> - **常见写法**：在实际应用中，箭头函数非常普遍，如下面的 `filter` 方法。
>
> ```javascript
> // ES6 写法
> todos.value = todos.value.filter((t) => t !== todo)
>
> // 等同于 ES5 写法
> todos.value = todos.value.filter(function(t) { return t !== todo; });
> ```
>

### 2.2 Rest Parameters (剩余参数)

使用 `...` 语法，可以让函数接受可变数量的参数，这些参数会被收集到一个数组中。

```js
function howMany(...args) {
  return "You have passed " + args.length + " arguments.";
}

console.log(howMany(0, 1, 2)); // 输出: You have passed 3 arguments.
console.log(howMany("string", null, [1, 2, 3], {})); // 输出: You have passed 4 arguments.
```

### 2.3 Spread Operator (展开运算符)

展开运算符 `...` 可以将数组（或可迭代对象）展开为独立的元素。

> [!example] 使用展开运算符求数组最大值
> **ES5 写法**：
> `Math.max()` 不接受数组作为参数，因此需要使用 `apply()`。
>
> ```js
> var arr = [6, 89, 3, 45];
> var maximus = Math.max.apply(null, arr); // maximus 的值为 89
> ```
>
> **ES6 写法**：
> 语法更简洁易读。
>
> ```js
> const arr = [6, 89, 3, 45];
> const maximus = Math.max(...arr); // maximus 的值为 89
> ```
>

### 2.4 Destructuring Assignment (解构赋值)

解构赋值语法是一种可以从数组或对象中快速提取值的表达式。

> [!example] 对象解构
>
> **ES5 写法**：
>
> ```js
> const user = { name: 'John Doe', age: 34 };
>
> const name = user.name; // name 的值为 'John Doe'
> const age = user.age;   // age 的值为 34
> ```
>
> **ES6 写法**：
>
> ```js
> const { name, age } = user;
> ```
>
> **为解构的变量重命名**：
>
> ```js
> const user = { name: 'John Doe', age: 34 };
> const { name: userName, age: userAge } = user;
>
> console.log(userName); // 输出 'John Doe'
> console.log(userAge);  // 输出 34
> ```
>
> > [!abstract] 提示
> > 解构赋值还有很多技巧，可以查阅相关手册深入了解。


### 2.5 简写属性名和方法名

> [!tip] 简写属性名
> 当对象的键名与持有其值的变量名相同时，可以省略冒号和值。
>
> **常规写法**：
>
> ```js
> const getMousePosition = (x, y) => ({
>   x: x,
>   y: y
> });
> ```
>
> **ES6 简写**：
>
> ```js
> const getMousePosition = (x, y) => ({ x, y });
> ```
>

> [!tip] 简写方法名
> 在对象中定义方法时，可以省略 `: function`。
>
> **ES5 写法**：
>
> ```js
> const person = {
>   name: "Taylor",
>   sayHello: function() {
>     return `Hello! My name is ${this.name}.`;
>   }
> };
> ```
>
> **ES6 简写**：
>
> ```js
> const person = {
>   name: "Taylor",
>   sayHello() {
>     return `Hello! My name is ${this.name}.`;
>   }
> };
> ```
>

### 2.6 Class (类)

ES6 引入了 `class` 关键字作为创建对象的语法糖。

```js
// 带有显式构造函数 (constructor)
class SpaceShuttle {
  constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
  }
  takeOff() {
    console.log("To " + this.targetPlanet + "!");
  }
}

// 带有隐式构造函数
class Rocket {
  launch() {
    console.log("To the moon!");
  }
}

const zeus = new SpaceShuttle('Jupiter');
zeus.takeOff(); // 控制台输出: To Jupiter!

const atlas = new Rocket();
atlas.launch(); // 控制台输出: To the moon!
```

### 2.7 使用 Getter 和 Setter 控制对对象的访问

> [!info] Getter (取值器) 与 Setter (存值器)
> - **Getter**：用于获取对象私有变量值的函数。
> - **Setter**：用于修改对象私有变量值的函数，可以包含额外的逻辑。
>
> Getter 和 Setter 非常重要，因为它们**隐藏了内部的实现细节**。

> [!quote] 注意
> 在私有变量的名称前加上下划线（`_`）是一种约定俗成的规范。然而，这种做法本身并不会使变量真正变为私有。

```javascript
class Book {
  constructor(author) {
    this._author = author;
  }
  
  // getter (取值器)
  get writer() {
    return this._author;
  }
  
  // setter (存值器)
  set writer(updatedAuthor) {
    this._author = updatedAuthor;
  }
}

const novel = new Book('anonymous');
console.log(novel.writer); // 调用 getter，输出: anonymous

novel.writer = 'newAuthor'; // 调用 setter
console.log(novel.writer); // 再次调用 getter，输出: newAuthor
```

### 2.8 Modules (模块)

要在 HTML 中使用模块，script 标签需要设置 `type="module"`。

```html
<script type="module" src="filename.js"></script>
```

#### 2.8.1 `export` (命名导出)

你可以从一个文件中导出多个变量或函数，以便在其他文件中使用。

> [!example] 导出 `add` 函数
> 想象一个文件 `math_functions.js`：
>
> **行内导出**：
>
> ```javascript
> export const add = (x, y) => {
>   return x + y;
> };
> ```
>
> **在末尾集中导出**：
>
> ```javascript
> const add = (x, y) => {
>   return x + y;
> };
> export { add };
> ```
>
> **导出多个项**：
>
> ```javascript
> export { add, subtract };
> ```
>

#### 2.8.2 `import` (导入)
使用 `import` 关键字可以从其他模块中导入已导出的功能。

> [!example] 导入
>
> - **导入单个项**：
>
> ```js
> import { add } from './math_functions.js';
> ```
>
> - **导入多个项**：
>
> ```js
> import { add, subtract } from './math_functions.js';
> ```
>
> - **将模块所有导出项作为对象导入**：
>
> ```js
> import * as myMathModule from "./math_functions.js";
>
> myMathModule.add(2,3);
> myMathModule.subtract(5,3);
> ```
>

#### 2.8.3 `export default` (默认导出)

`export default` 用于指定一个文件的“后备”或主要导出项。

> [!info] 默认导出的特点
> - 通常在一个文件**只导出一个值**时使用。
> - 每个模块或文件中**只能有一个**默认导出。
> - 不能将 `export default` 与 `var`, `let`, 或 `const` 关键字连用（用于行内声明）。

```javascript
// 写法一：导出一个命名函数
export default function add(x, y) {
  return x + y;
}

// 写法二：导出一个匿名函数
export default function(x, y) {
  return x + y;
}
```

#### 2.8.4 `import` (导入默认导出)

导入默认导出时，不需要使用花括号 `{}`，并且可以为其指定任意名称。

```js
import add from "./math_functions.js";
```

> [!summary] `export` vs `export default` 的关键区别
> - **数量**:
>   - `export` (命名导出) 在一个文件中可以有**多个**。
>   - `export default` (默认导出) 在一个文件中**只能有一个**。
> - **导入方式**:
>   - 命名导出：导入时必须使用花括号 `{}`, 且名称必须**完全匹配**。
>     `import { add } from './file.js';`
>   - 默认导出：导入时**不使用**花括号 `{}`，并且可以给它**任意命名**。
>     `import myAddFunction from './file.js';`


### 2.9 Promise

> [!abstract] 什么是 Promise？
> Promise 是一个用于处理**异步**操作的对象。它代表一个最终可能完成（fulfilled）或失败（rejected）的操作及其结果值。
>
> `Promise` 是一个构造函数，它接受一个函数作为参数。这个函数又带有 `resolve` 和 `reject` 两个参数。
>
> ```javascript
> const myPromise = new Promise((resolve, reject) => {
>   // 异步操作代码
> });
> ```
>

#### 2.9.1 使用 `resolve` 和 `reject` 来完成一个 Promise

一个 Promise 有三种状态：
1.  **`pending`** (进行中)
2.  **`fulfilled`** (已成功)
3.  **`rejected`** (已失败)

`resolve` 和 `reject` 是用来改变 Promise 状态的函数。
- `resolve()`: 将 Promise 状态从 `pending` 变为 `fulfilled`。
- `reject()`: 将 Promise 状态从 `pending` 变为 `rejected`。

```javascript
const myPromise = new Promise((resolve, reject) => {
  if (/* 某个条件成立 */) {
    resolve("Promise 已成功履行！");
  } else {
    reject("Promise 已被拒绝！");
  }
});
```

#### 2.9.2 使用 `.then()` 处理一个已成功的 Promise

当 Promise 成功履行（resolved）时，`.then()` 方法注册的回调函数会被执行。

```javascript
myPromise.then(result => {
  // 处理成功的结果
});
```

这里的 `result` 参数，就是调用 `resolve` 时传递的值。

> [!example] `then()` 示例
>
> ```js
> const makeServerRequest = new Promise((resolve, reject) => {
>   let responseFromServer = true;
>     
>   if(responseFromServer) {
>     resolve("We got the data");
>   } else {  
>     reject("Data not received");
>   }
> });
>
> makeServerRequest.then(result => {
>   console.log(result); // 输出: We got the data
> });
> ```
>

#### 2.9.3 使用 `.catch()` 处理一个已失败的 Promise

当 Promise 被拒绝（rejected）时，`.catch()` 方法注册的回调函数会被执行。

```javascript
myPromise.catch(error => {
  // 处理失败的原因
});
```

这里的 `error` 参数，是调用 `reject` 时传递的值。