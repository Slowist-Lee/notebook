动态class绑定

```vue
<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
</script>

<template>
  <h1 :class="titleClass">Make me red</h1> <!-- 此处添加一个动态 class 绑定 -->
</template>

<style>
.title {
  color: red;
}
</style>
```

事件DOM监听 https://cn.vuejs.org/tutorial/#step-4

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
function increment(){
  count.value++
}
</script>

<template>
  <!-- 使此按钮生效 -->
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

DOM和文本双向绑定:`v-model` https://cn.vuejs.org/tutorial/#step-5

e.g. 上下程序等价

```vue
<script setup>
import { ref } from 'vue'

const text = ref('')

function onInput(e) {
  text.value = e.target.value
}
</script>

<template>
  <input :value="text" @input="onInput" placeholder="Type here">
  <p>{{ text }}</p>
</template>
```

```vue
<script setup>
import { ref } from 'vue'

const text = ref('')

// function onInput(e) {
//   text.value = e.target.value
// }
</script>

<template>
  <input v-model="text" placeholder="Type here">
  <p>{{ text }}</p>
</template>
```

![](Pasted%20image%2020260125122327.png)

模板中的表达式虽然方便，但也只能用来做简单的操作。如果在模板中写太多逻辑，会让模板变得臃肿，难以维护。比如说，我们有这样一个包含嵌套数组的对象：


```js
const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})
```

我们想根据 `author` 是否已有一些书籍来展示不同的信息：


```html
<p>Has published books:</p>
<span>{{ author.books.length > 0 ? 'Yes' : 'No' }}</span>
```

这里的模板看起来有些复杂。我们必须认真看好一会儿才能明白它的计算依赖于 `author.books`。更重要的是，如果在模板中需要不止一次这样的计算，我们可不想将这样的代码在模板里重复好多遍。

因此我们推荐使用**计算属性**来描述依赖响应式状态的复杂逻辑。这是重构后的示例：

```vue
<script setup>
import { reactive, computed } from 'vue'

const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

// 一个计算属性 ref
const publishedBooksMessage = computed(() => {
  return author.books.length > 0 ? 'Yes' : 'No'
})
</script>

<template>
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</template>
```


我们在这里定义了一个计算属性 `publishedBooksMessage`。`computed()` 方法期望接收一个 [getter 函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/get#description)，返回值为一个**计算属性 ref**。和其他一般的 ref 类似，你可以通过 `publishedBooksMessage.value` 访问计算结果。计算属性 ref 也会在模板中自动解包，因此在模板表达式中引用时无需添加 `.value`。

Vue 的计算属性会自动追踪响应式依赖。它会检测到 `publishedBooksMessage` 依赖于 `author.books`，所以当 `author.books` 改变时，任何依赖于 `publishedBooksMessage` 的绑定都会同时更新。

### 手动操作DOM：

创建模板引用：

给一个ref attribute，给一个名字。

```html
<!-- template -->
<p ref="pElementRef">hello</p>
```

*   **在 `<script setup>` (组合式 API) 中**：你需要创建一个同名的 `ref` 响应式变量来接收这个引用。
```javascript
// js
import { ref } from 'vue'

const pElementRef = ref(null)
```
**关键点**：这个 `ref` 变量的名称必须和模板中 `ref` attribute 的值（这里是 `pElementRef`）**完全一致**。Vue 会自动将 DOM 元素赋值给这个变量。

3.  **为什么初始值是 `null`？**
    *   图片中提到：“注意这个 ref 使用 `null` 值来初始化。”
    *   **原因**：当 `<script setup>` 中的代码执行时，组件的模板还没有被渲染成真实的 DOM。简单来说，JavaScript 代码先运行，然后 Vue 才去创建 `<p>` 元素。因此，在组件**挂载 (mounted)** 之前，`pElementRef` 这个变量是空的（即 `null`），因为它引用的 DOM 元素还不存在。

4.  **何时可以访问模板引用？**
    *   **时机**：只有在组件**挂载完成后**，DOM 元素才被创建，此时 Vue 才会将元素赋值给我们定义的 ref 变量。
    *   **方法**：为了确保在 DOM 元素存在时才执行代码，我们需要使用 `onMounted` 这个**生命周期钩子**。
	```javascript
	// js
	import { ref, onMounted } from 'vue'

	const pElementRef = ref(null)

	onMounted(() => {
	  // 此刻，组件已经挂载
	  // pElementRef.value 就指向了那个 <p> DOM 元素
	  console.log(pElementRef.value) // <p>hello</p>
	  pElementRef.value.textContent = 'world' // 可以直接操作它
	})
	```
*   **生命周期钩子**：像 `onMounted`、`onUpdated`（数据更新后调用）、`onUnmounted`（组件卸载时调用）这些函数，允许我们在组件生命周期的特定阶段执行代码，它们统称为生命周期钩子。

### 补充文字详解

2.  **引用的是 DOM 元素还是组件实例？**

* 如果 `ref` 用在**普通 HTML 元素**上（如 `<p>`, `<div>`, `<input>`），你获取到的是**真实的 DOM 元素**。
* 如果 `ref` 用在**子组件**上（如 `<MyComponent ref="comp">`），你获取到的是**子组件的实例**，可以让你调用子组件里通过 `defineExpose` 暴露出来的方法和属性。

3.  **Ref 接收一个函数**

* 这是一种更灵活、更底层的用法。你可以给 `ref` attribute 传递一个函数。
```html
<ChildComponent :ref="(el) => { child = el }" />
```
* 当 `ChildComponent` 挂载后，Vue 会调用这个函数，并将组件实例作为参数（`el`）传入。这样你就可以自己决定把这个引用存到哪里（比如存到一个普通的变量 `child` 中），而不是依赖 Vue 的自动匹配。

4.  **重要说明**

* **注册时机**：再次强调，无论是哪种 API，都**必须等到组件挂载后**才能访问 ref 引用。
* **`this.$refs` 是非响应式的**：在选项式 API 中，`this.$refs` 对象本身不是响应式的。这意味着你不能在模板里像这样用它：`{{ this.$refs.p.textContent }}`。如果你试图这样做，当 `textContent` 改变时，视图不会自动更新。`$refs` 主要是为了在 JavaScript 中进行一次性的、命令式的操作。

好的，我们来详细解释一下图片中的内容。这张图片介绍的是 Vue 中一个非常重要的概念：**侦听器 (Watcher)** 和 **副作用 (Side Effect)**。

### 1. 什么是“副作用” (Side Effect)？

在编程领域，特别是函数式编程中，“副作用”是一个核心概念。简单来说，一个函数的“主作用”是根据输入计算并返回一个值。而**“副作用”指的是函数在执行过程中，对函数外部的状态产生了可观察的改变**。

举一些常见的例子：

*   **修改一个全局变量或外部变量**
*   **向控制台输出日志**（正如图片中的 `console.log()`）
*   **发起网络请求**（比如 `fetch` 或 `axios`）
*   **直接操作 DOM**（比如修改元素的样式、内容）
*   **读写本地存储 (localStorage)**

这些操作都不属于“计算返回值”这个主作用，而是与外部环境进行了交互，因此被称为“副作用”。

在 Vue 的世界里，组件的主要任务是渲染视图。因此，任何**响应数据变化而执行的、与渲染视图无直接关系的操作**，都可以看作是副作用。

### 2. 为什么需要“响应性地执行”副作用？

图片中提到“有时我们需要响应性地执行一些‘副作用’”。这句话的意思是：我们希望**当某个数据发生变化时，自动地去执行一个副作用操作**。

例如：

*   当用户在搜索框输入的**关键词改变**时，我们想**发起一次新的网络请求**去获取搜索结果。
*   当一个**计数器 `count` 的值改变**时，我们想把这个新值**打印到控制台**（图片中的例子）。
*   当用户的**登录状态改变**时，我们想把新的状态信息**存入 `localStorage`**。

在这些场景下，我们不能简单地执行一次操作就完事了，而是需要一个机制来“监视”数据的变化，并在变化发生时触发相应的动作。

### 3. `watch` 侦听器：实现响应性副作用的工具

Vue 提供了 `watch` 函数，它就是专门用来实现上述需求的工具。`watch` 就像一个“侦探”，你告诉它要监视哪个数据，它就会一直盯着，一旦数据变了，它就立刻执行你指定的操作（那个副作用）。

我们来看图片中的代码：

```javascript
import { ref, watch } from 'vue'

// 1. 创建一个响应式数据 count，初始值为 0
const count = ref(0)

// 2. 使用 watch 侦听 count 的变化
watch(count, (newCount) => {
  // 这里的函数是“回调函数”，会在 count 变化时执行
  
  // 3. 执行副作用：在控制台打印日志
  //    这个操作本身不影响页面的渲染，是典型的副作用
  console.log(`new count is: ${newCount}`) 
})

// 当你在别处修改 count 的值，比如执行 count.value++ 时，
// 上面 watch 中的回调函数就会自动被调用，
// 控制台就会输出 "new count is: 1", "new count is: 2" ...
```

#### `watch` 函数的语法解析：

`watch` 函数通常接收两个主要参数：

1.  **要侦听的“源”**：你想要监视的响应式数据。在例子中，就是 `count` 这个 ref。
2.  **回调函数**：当“源”数据变化时要执行的函数。这个函数会接收到变化后的新值（在例子中是 `newCount`）。你也可以接收到旧的值，像这样：`(newValue, oldValue) => { ... }`。

### 总结

所以，图片的核心思想是：

> 当你需要**在某个响应式数据（如 `ref` 或 `reactive` 对象）发生变化时，去执行一些不直接关系到页面渲染的操作（即“副作用”）**时，你应该使用 `watch` 函数。

`watch` 函数为你提供了一个清晰、声明式的方式来处理因数据变化而引起的副作用，这是构建复杂前端应用时非常有用的一个功能。

vue的嵌套组件语法：

```vue
<script setup>
import ChildComp from './ChildComp.vue'
</script>

<template>
  <ChildComp />
</template>
```


当然，我们来详细解释一下图片中关于 **Props** 的概念。这是 Vue 组件化开发中最核心、最基础的知识点之一。

### 核心思想：什么是 Props？

想象一下你正在用积木搭建一个房子。你有很多不同类型的积木块（组件），比如“墙壁”积木、“窗户”积木、“门”积木。

现在，你希望你的“窗户”积木可以是不同颜色的，比如红色、蓝色或绿色。你总不能为每一种颜色都制作一种全新的“窗户”积木吧？最好的办法是，你只有一个通用的“窗户”积木，而在使用它的时候，你告诉它：“嘿，你这次应该是红色的。”

在 Vue 中：
*   **积木** 就是 **组件**。
*   你从外部告诉积木它应该是什么样子的**信息**（比如“红色”），就是 **Props** (Properties 的缩写，意为属性)。

**Props 的本质是：一种让父组件向子组件单向传递数据的机制。** 数据流是自上而下（父 -> 子）的。

---

### 图片内容详解

我们把整个流程分为两部分：**子组件如何接收数据** 和 **父组件如何传递数据**。

#### 1. 子组件：声明并接收 Props (`ChildComp.vue`)

子组件不能随便接收任何数据，它必须先**明确声明**自己“期望”接收哪些数据，以及这些数据应该是什么类型。这就像一个函数的参数列表，定义了函数需要哪些输入。

图片中的代码就是在做这件事：

```vue
// ChildComp.vue

<script setup>
// 使用 defineProps 宏来声明组件的 props
const props = defineProps({
  // 声明一个名为 "msg" 的 prop
  // "String" 表示我们期望这个 prop 的值是一个字符串类型
  msg: String 
})

// 现在，你可以通过 props.msg 在 <script> 中访问这个值
// console.log(props.msg) 
</script>

<template>
  <!-- 在模板中，你可以直接使用 prop 的名字 -->
  <h1>{{ msg }}</h1>
</template>
```

**关键点解释：**

*   `defineProps()`：这是一个**编译时宏 (Compiler Macro)**。
    *   **“宏”** 的意思是它不是一个普通的 JavaScript 函数，它会在代码被编译的时候进行处理。
    *   正因为如此，你**不需要**像 `import { ref } from 'vue'` 那样去 `import` 它，在 `<script setup>` 环境中可以直接使用。
*   `{ msg: String }`：这是一个对象，用来定义所有期望接收的 props。
    *   `msg` 是 prop 的名字。
    *   `String` 是期望的**类型**。这样做有两个好处：
        1.  代码更清晰，别人一看就知道该传什么类型的数据。
        2.  如果父组件传递了错误的类型（比如传了一个数字 `123`），Vue 会在浏览器的控制台给出警告，方便排查错误。
*   `const props = ...`：`defineProps` 会返回一个对象，这个对象里包含了所有从父组件接收到的 prop 值。在 `<script>` 部分，你需要通过 `props.msg` 来访问它。
*   **模板中的直接使用**：一个非常方便的特性是，在子组件的 `<template>` 里，你不需要写 `props.msg`，可以直接写 `{{ msg }}`。Vue 会自动帮你处理好。

#### 2. 父组件：传递 Props

现在子组件已经准备好接收一个名为 `msg` 的字符串了，父组件就可以在使用它的时候把数据传给它。

图片中展示了父组件的模板用法：

```html
<!-- 在父组件的 template 中 -->
<ChildComp :msg="greeting" />
```

**关键点解释：**

*   **看起来像 HTML Attribute**：向子组件传递 props 的语法，就像给普通的 HTML 标签设置 attribute 一样，非常直观。
*   **静态值 vs 动态值 (关键！)**
    *   **传递静态字符串**：如果你想传递一个固定的字符串，可以不用 `v-bind`（也就是冒号 `:`）。
        ```html
        <ChildComp msg="Hello, this is a static message" />
        ```
        这里 `msg` prop 接收到的值就是字符串 `"Hello, this is a static message"`。

    *   **传递动态值**：如果你想传递一个变量，或者一个 JavaScript 表达式的结果，**必须**使用 `v-bind` 指令，它的简写形式就是一个**冒号 `:`**。

```html
<ChildComp :msg="greeting" />
```        

这行代码告诉 Vue：“不要把 `greeting` 当作一个普通的字符串，请去父组件的 `<script>` 里找到一个叫做 `greeting` 的变量，把**它的值**传递给 `msg` prop。”

因此，父组件的 `<script>` 部分可能长这样：

```javascript
// ParentComponent.vue
import { ref } from 'vue'
const greeting = ref('这是一个来自父组件的动态问候！')
```

在这种情况下，`ChildComp` 接收到的 `msg` 值就是 `"这是一个来自父组件的动态问候！"`。如果 `greeting` 的值改变了，传递给子组件的 `msg` 也会自动更新。

### 总结

| 角色 | 任务 | 语法示例 |
| :--- | :--- | :--- |
| **子组件** | **接收方**：声明自己需要什么数据。 | `<script setup>` 中使用 `const props = defineProps({ propName: Type })` |
| **父组件** | **发送方**：在使用子组件时，把数据“喂”给它。 | `<ChildComponent :propName="parentDataVariable" />` (动态绑定) <br> `<ChildComponent propName="Static String" />` (静态绑定) |

**核心规则**：Props 是**单向**的。子组件应该**只读取** props 的值来使用，而**不应该去修改**它。如果子组件需要修改数据，应该通过触发事件（`emit`）的方式通知父组件来做修改，这是保证数据流清晰可控的关键。

这是一个非常好的问题，也是初学者经常会混淆的地方！

简单来说：这里的双引号 `""` **不是用来表示它是一个字符串**，而是 Vue 模板语法的一部分，**用来包裹一个 JavaScript 表达式**。

关键在于 `msg` 前面的那个**冒号 `:`**。

这个冒号是 `v-bind` 指令的缩写。一旦你看到了这个冒号，就意味着双引号 `""` 里面的内容会被当作 **JavaScript** 来执行，而不是一个普通的字符串。

让我们通过对比来彻底理解它：

---

### 情况一：没有冒号 `:` (静态传递)

```html
<ChildComp msg="greeting" />
```

*   **含义**：这和标准的 HTML attribute 行为一致。
*   **传递的内容**：你传递给 `msg` 这个 prop 的值就是**字面上的字符串 `"greeting"`**。
*   **子组件接收到的值**：`props.msg` 的值是 `"greeting"`。

---

### 情况二：有冒号 `:` (动态绑定)

```html
<ChildComp :msg="greeting" />
```

*   **含义**：告诉 Vue：“**不要把引号里的内容当作字符串！** 请把它当作一个 **JavaScript 表达式**来解析。”
*   **传递的内容**：Vue 会在父组件的 `<script>` 部分去寻找一个**名为 `greeting` 的变量**。然后，它会把这个**变量的值**传递给 `msg` prop。
*   **子组件接收到的值**：`props.msg` 的值是父组件中 `greeting` 变量的值。

#### 完整的父组件例子：

假设父组件是这样的：

```vue
<!-- ParentComponent.vue -->
<script setup>
import { ref } from 'vue'
import ChildComp from './ChildComp.vue'

// 我们在这里定义了一个 JavaScript 变量
const greeting = ref('Hello from parent component!') 
</script>

<template>
  <!-- 
    因为有冒号 : ，Vue 会去找 greeting 这个变量, 
    然后把它的值 "Hello from parent component!" 传递过去
  -->
  <ChildComp :msg="greeting" />
</template>
```

在这种情况下，`ChildComp` 接收到的 `msg` prop 的值就是字符串 `"Hello from parent component!"`。

### 总结与类比

你可以把 `v-bind:` 的双引号想象成一个“**JavaScript 执行环境**”或者一个“**魔法盒子**”。

*   **`msg="greeting"`**
    *   你把一个写着 "greeting" 的纸条放进普通的信封里。对方收到的是纸条本身。

*   **`:msg="greeting"`**
    *   你把一张写着“请告诉我 `greeting` 变量里装的是什么”的指令放进一个魔法盒子里。Vue（魔法师）打开盒子，看到指令，然后找到 `greeting` 变量，取出里面的东西（比如是 "Hello world"），再把 "Hello world" 交给子组件。

所以，规则非常简单：

| 语法 | `""` 内的内容被如何解析 | 传递的是什么 |
| :--- | :--- | :--- |
| `prop="value"` | **普通字符串** | 字符串 `"value"` |
| `:prop="value"` | **JavaScript 表达式** | 名为 `value` 的**变量的值** |

# Emits

除了接收 props，子组件还可以向父组件触发事件：


```vue
<script setup>
// 声明触发的事件
const emit = defineEmits(['response'])

// 带参数触发
emit('response', 'hello from child')
</script>
```

`emit()` 的第一个参数是事件的名称。其他所有参数都将传递给事件监听器。

父组件可以使用 `v-on` 监听子组件触发的事件——这里的处理函数接收了子组件触发事件时的额外参数并将它赋值给了本地状态：

```vue
<ChildComp @response="(msg) => childMsg = msg" />
```
