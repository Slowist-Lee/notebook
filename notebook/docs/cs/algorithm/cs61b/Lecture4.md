# Lecture 4

`IntList`: 裸递归

原先的链表：

```java
public class IntNode {
    public int item;
    public IntNode next;

    public IntNode(int i, IntNode n) {
        item = i;
        next = n;
    }
}
```

然后为这个列表创建一个单独的类，和用户交互：

```java
public class SLList {
    public IntNode first;

    public SLList(int x) {
        first = new IntNode(x, null);
    }
}
```

`SLList`能更好的封装链表. 在创建链表时，也可以感受出来 →

```java
IntList L1 = new IntList(5, null);
SLList L2  = new SLList(5);
```


