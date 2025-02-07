## Note:
- Java has `null` instead of `None` in python!
- In `new int[3]`, the `int` is the type in the array; and `3` is the length. With this syntax, all elements take on their "default value". For `int`, this is 0.
- Arrays do not print nicely, for reasons beyond the scope of HW 0. To print an array, you can call `Arrays.toString(array)`.
- Use `myArray.length` instead of `myArray.length()` to get the length of the array. Java doesn't have the method `length()`

### Foreach Loop / Enhanced For Loop
in python:
```python
lst = [1, 2, 3]
for i in lst:
    print(i)
```

in java:

```
int[] array = {1, 2, 3};
for (int i : array) {
    System.out.println(i);
}
```


- Notice the type declaration of the iterating variable, as well as the usage of `:` instead of `in`.
- We can also use this syntax on certain other types, such as `List`s and `Set`s.

### Lists (resizable)[​](https://www.learncs.site/docs/curriculum-resource/cs61b/homeworks/hw0/hw0b#lists-resizable "Direct link to Lists (resizable)")
python:
```
lst = []
lst.append("zero")
lst.append("one")
lst[0] = "zed"
print(l[0])
print(len(l))
if "one" in lst:
    print("one in lst")

for elem in lst:
    print(elem)

```

java:
```java
List<String> lst = new ArrayList<>();
lst.add("zero");
lst.add("one");
lst.set(0, "zed");
System.out.println(lst.get(0));
System.out.println(lst.size());
if (lst.contains("one")) {
    System.out.println("one in lst");
}
for (String elem : lst) {
    System.out.println(elem);
}
```

- Java has the `List` interface. We largely use the [`ArrayList`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayList.html) implementation.
- The `List` interface is _parameterized_ by the type it holds, using the angle brackets `<` and `>`.
- `List`s, again, do not support slicing or negative indexing.

### Sets
java:
```java
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(1);
set.add(2);
set.remove(2);
System.out.println(set.size());
if (set.contains(1)) {
    System.out.println("1 in set");
}
for (int elem : set) {
    System.out.println(elem);
}
```

Set->集合

- Java has the `Set` interface. There are two main implementations: [`TreeSet`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html), and [`HashSet`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashSet.html). `TreeSet` keeps its elements in "sorted" order, and is fast. In contrast, `HashSet` does not have a defined "order", but is (usually) really fast.
    - We will formalize these notions of "fast" later on in the course when we learn about asymptotic analysis.
- A `Set` cannot contain duplicate items. If we try to add an item already in the set, nothing happens.

### Dictionaries / Maps[​](https://www.learncs.site/docs/curriculum-resource/cs61b/homeworks/hw0/hw0b#dictionaries--maps "Direct link to Dictionaries / Maps")

```python
d = {}
d["hello"] = "hi"
d["hello"] = "goodbye"
print(d["hello"])
print(len(d))
if "hello" in d:
    print("\"hello\" in d")

for key in d.keys():
    print(key)

```

```java
Map<String, String> map = new HashMap<>();
map.put("hello", "hi");
map.put("hello", "goodbye");
System.out.println(map.get("hello"));
System.out.println(map.size());
if (map.containsKey("hello")) {
    System.out.println("\"hello\" in map");
}
for (String key : map.keySet()) {
    System.out.println(key);
}
```

- Java has the `Map` interface. There are two main implementations: [`TreeMap`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeMap.html), and [`HashMap`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html). Similarly to sets, `TreeMap` keeps its keys sorted and is fast; `HashMap` has no defined order and is (usually) really fast.
- A `Map` cannot contain duplicate keys. If we try to add a key already in the map, the value is overwritten.
- In the angle brackets, we have the "key type" first, followed by the "value type".
- `Map`s cannot directly be used with the `:` for loop. Typically, we call `keySet` to iterate over a set of the keys, and use those to retrieve the values. One may also iterate over the `entrySet` to get both the keys and values.

### Classes
### Main

## Knowledge Learned

- `List<Integer> lst = new ArrayList<>();` is correct
- `List<int>lst` is wrong!!!!!!!!!!

