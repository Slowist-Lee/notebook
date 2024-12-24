
we wrote like before→

```java
public class Dog {  
    public static void makenoise(){  
        System.out.println("Bark!");  
    }  
    public static void main(String[] args) {  
        makenoise();  
    }  
}
```

then we define another class:

```java
public class DogLauncher {  
    public static void main(String[] args) {  
        Dog.makenoise();  
    }  
}  
```

- Why `Dog.makenoise()`?
- dog actually doesn't live in the `DogLauncher Class`!
	- go to the dog class and to go to the makenoise function

every method should be in a class

```java
public class Dog {  
    public int weightInPounds;  
    public void makenoise(){  
        if (weightInPounds<10){  
            System.out.println("yip!");  
        }  
        else (weightInPounds<30){  
            System.out.println("rooooo!");  
        }  
        else {  
            System.out.println("bark!");  
        }  
    }  
    public static void main(String[] args) {  
        makenoise();  
    }  
}
```

pay attention to the usage of `else`

but warning! non-static field cannot be referenced from a static context
so delete the word `static`

but since `makenoise()` is non-static, it can't be quoted in the static function `main`

why?
our original codes are `Dog.makenoise()`
`Dog` are too general

so we need to make a new object like:
```java
Dog d = new Dog()
```

and codes like:

```java
d.weightInPounds = 20;
d.makeNoise();
```

so the whole script looks like:

in `Dog.java`, we wrote:

```java
public class Dog {  
    public int weightInPounds;  
    public Dog(int w){  
	    weightInPounds = w;  
	}
	// when we wrote a method which is not static, we need to create a instance
	public void makenoise(){  
        if (weightInPounds<10){  
            System.out.println("yip!");  
        }  
        else if (weightInPounds<30){  
            System.out.println("bark!");  
        }  
        else {  
            System.out.println("roooooooooooo!");  
        }  
    }  
}
```


and in `DogLauncher.java`, which contains the main function:

```java
public class DogLauncher {  
    public static void main(String[] args) {  
        Dog d = new Dog();  // Declaration of a Dog variable
        d.weightInPounds = 1;  
        d.makenoise();  
    }  
}
```

argument can also be filled when creating a new instance 

```java
public class DogLauncher {  
    public static void main(String[] args) {  
        Dog d = new Dog(1);  
        d.makenoise();  
    }  
}
```

to sum up, static method -> how do dogs make noise?
non-static method -> how does a specific dog make noise? e.g. how does Maya make noise

some method doesn't need to be intantiated. for example, math
```java
x=Math.round(5,6)
```

```java
public class Dog {  
    public int weightInPounds;  
    public static String binomen = "Cans";  
    //this name is the general name of every dog  
    public Dog(int w){  
        weightInPounds = w;  
    }  
    public void makenoise(){  
        if (weightInPounds<10){  
            System.out.println("yip!");  
        }  
        else if (weightInPounds<30){  
            System.out.println("bark!");  
        }  
        else {  
            System.out.println("roooooooooooo!");  
        }  
    }  
    public static Dog maxDog(Dog d1, Dog d2) {  
        if (d1.weightInPounds>d2.weightInPounds){  
            return d1;  
        }  
        else{  
            return d2;  
        }  
    }  
    public Dog MaxDog(Dog d2){  
        if (weightInPounds>d2.weightInPounds){  
            return this;  
        }else{  
            return d2;  
        }  
    }  
}
```


```java
public class DogLauncher {  
    public static void main(String[] args) {  
        Dog chester = new Dog(17);  
        Dog yusuf = new Dog(2);  
        Dog larger=Dog.maxDog(chester, yusuf);  
        larger.makenoise();  
        System.out.println(Dog.binomen);  //chester.binoman is also ok, just bit ugly
    }  
}  
// why? dog actually doesn't live in the DogLogic Class
```

### Interactive Debugging

debugging button
- set breaking point
- `step over` allows us to go on
- debugger will desplay the states of the arguments

- use `step into` to see what is in the function inside
- `resume program` -> run the program until it hits the break point
