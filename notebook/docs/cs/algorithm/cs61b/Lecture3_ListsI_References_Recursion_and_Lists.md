# Lec3 ListsI-References Recursion and Lists
- Java understand bits using types.
- for e.g.
	- both 72 & H are stored as `01001000`, but they can be interpreted symboled as `char` or `int`
- In Java, there are 8 primitive types: byte, short, int, long, float, double, boolean, and char
	- with the exception of short and float, which you'll likely never use

### 1 How do Java Declare a Variable?

#### 1.1 Setting aside Memory

Java will find a block to store the argument with exactly enough bits to hold

#### 1.2 create an entry in an internal table 

Java creates an entry in an internal table that maps each variable name to the location of the first bit in the box.

For example, if you declared `int x` and `double y`, then Java might decide to use bits 352 through 384 of your computer's memory to store x, and bits 20800 through 20864 to store y. The interpreter will then **record that int x starts at bit 352 and y starts at bit 20800.**

when we declare a variable of any reference type, whether `Dog` (a class) we created or `int` we have it initially, Java allocates a box of `64 bits`

#### 1.3 GRoE

When you write `y = x`, you are telling the Java interpreter to copy the bits from x into y
everything is the same. for e.g. if a is a notation which points to a Walrus, `b = a`, then b will be a notation points to a Walrus too.

#### 1.4 Parameter Passing

GRoE also applies to parameter passing in function.
That is,
When you pass parameters to a function, you are also simply copying the bits

parameter restores a series of bits, which represents its location consisting of `0100...`

so when you pass a parameter, you pass its location as well

e.g.

```java
Walrus a = new Walrus(1000, 8.3);
Walrus b;
b = a;
```
#### Difference between parameter and value

examples of passing by value

```java
public static double average(double a, double b) {
    return (a + b) / 2;
}
public static void main(String[] args) {
    double x = 5.5;
    double y = 10.5;
    double avg = average(x, y);
}
```

in this example👇
```java
public class PassByValueFigure {
    public static void main(String[] args) {
           Walrus walrus = new Walrus(3500, 10.5);
           int x = 9;

           doStuff(walrus, x);
           System.out.println(walrus);
           System.out.println(x);
    }

    public static void doStuff(Walrus W, int x) {
           W.weight = W.weight - 100;
           x = x - 5;
    }
}
```

`doStuff` doesn't affect `x`; but it makes sense to `W`

### 2 Instantiation of Arrays

Instantiating an array is very similar to instantiating an object!

```java
int[] x;
Planet[] planets;
```

Both of these declarations create memory boxes of 64 bits. `x` can only hold the address of an `int` array, and `planets` can only hold the address of a `Planet` array.

```
x = new int[]{0, 1, 2, 95, 4};
```

- the `new` keyword creates 5 boxes of 32 bits each and returns the address of the overall object for assignment to x
- if you lose the address, the whole object may be lost. So if you want to throw away the object, simply throw away its address is an option :

### 3 IntLists

take linked list for example:

```java
public class IntList {
    public int first;
    public IntList rest;  
    //for an object, things after it must be a linked list as well. so we define `rest` as an IntList   

    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }
}
```

since we have `object`,we can write→

```java
IntList L = new IntList(5, null);
L.rest = new IntList(10, null);
L.rest.rest = new IntList(15, null);
```

Alternately, we could build our list backwards, yielding slightly nicer but harder to understand code:


```java
IntList L = new IntList(15, null);
L = new IntList(10, L);
L = new IntList(5, L);
```

Exercise: `size method` / `iterative size method`

```ad-warning
title: Attention
this requires `method`.
That means: do not write size in your defining program!!!!!
Anyway, size doesn't need to be a property of 
```


```java
public class IntList {
    public int first;
    public IntList rest; 
    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }
    public int size(){
        if (rest == null){
            return 1;
        }
        else{
	        return this.rest.size()+1;
        }
    }
}
```

I recommend that when you write iterative data structure code that you use the name `p` to remind yourself that the variable is holding a pointer. You need that pointer because you can't reassign "this" in Java.


So the following is wrong...

```java
    public int IterativeSize(){
	    int result = 0;
	    while this.rest != null{
		    result +=1;
		    this = this.rest
	    }
	    return result;
    }
```

corrected:

```java
    public int IterativeSize(){
	    int result = 0;
	    IntList p = this; //!!!
	    while p != null{ 
		    result +=1;
		    p = p.rest;
	    }
	    return result;
    }
```

Exercise: Write a method `get(int i)` that returns the ith item of the list. For example, if `L` is 5 -> 10 -> 15, then `L.get(0)` should return 5, `L.get(1)` should return 10, and `L.get(2)` should return 15. It doesn't matter how your code behaves for invalid `i`, either too big or too small.

```java
public int get(int i){
	int cnt = 0;
	IntList p = this;
	while (cnt<i){
		p=p.rest;
		cnt+=1;
	}
	return p.first;
}
```