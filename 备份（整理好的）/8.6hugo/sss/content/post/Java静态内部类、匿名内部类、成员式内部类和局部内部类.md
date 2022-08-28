

+++
title = "Java静态内部类、匿名内部类、成员式内部类和局部内部类"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:12"
categories = [
"Chinese",
]
+++

# Java静态内部类、匿名内部类、成员式内部类和局部内部类




内部类可以是静态(static)的，可以使用 public、protected 和 private 访问控制符，而外部类只能使用 public，或者默认。




##  成员式内部类

在外部类内部直接定义（不在方法内部或代码块内部）的类就是成员式内部类，它可以直接使用外部类的所有变量和方法，即使是 private
的。外部类要想访问内部类的成员变量和方法，则需要通过内部类的对象来获取。  
  
请看下面的代码：


    
```java
    
    public class Outer{
        private int size;
        public class Inner {
            public void dostuff() {
                size++;
            }
        }
        public void testTheInner() {
            Inner in = new Inner();
            in.dostuff();
        }
    }
    
```
成员式内部类如同外部类的一个普通成员。  
  
成员式内部类可以使用各种修饰符，包括 public、protected、private、static、final 和 abstract，也可以不写。  
  
若有 static 修饰符，就为类级，否则为对象级。类级可以通过外部类直接访问，对象级需要先生成外部的对象后才能访问。  
  
非静态内部类中不能声明任何 static 成员。  
  
内部类可以相互调用，例如：
    
```java
    
    
    class A {
        // B、C 间可以互相调用
        class B {}
        class C {}
    }
    
```

####  成员式内部类的访问

内部类的对象以成员变量的方式记录其所依赖的外层类对象的引用，因而可以找到该外层类对象并访问其成员。该成员变量是系统自动为非 static
的内部类添加的，名称约定为"outClassName.this"。  
  
1)
使用内部类中定义的非静态变量和方法时，要先创建外部类的对象，再由"outObjectName.new"操作符创建内部类的对象，再调用内部类的方法，如下所示：
    
```java
    
    
    public class Demo{
        public static void main(String[] args) {
            Outer outer = new Outer();
            Outer.Inner inner = outer.new Inner();
            inner.dostuff();
        }
    }
    class Outer{
        private int size;
        class Inner{
            public void dostuff() {
                size++;
            }
        }
    }

      
```

2) static 内部类相当于其外部类的 static 成员，它的对象与外部类对象间不存在依赖关系，因此可直接创建。示例如下：

     
```java   
    
    public class Demo{
        public static void main(String[] args) {
            Outer.Inner inner = new Outer.Inner();
            inner.dostuff();
        }
    }

class Outer{ private static int size; static class Inner { public void
dostuff() { size++; System.out.println("size=" \+ size); } } }

    
```


运行结果：  
size=1  
  
3) 由于内部类可以直接访问其外部类的成分，因此当内部类与其外部类中存在同名属性或方法时，也将导致命名冲突。所以在多层调用时要指明，如下所示：

    
```java
    
    public class Outer{
        private int size;
        public class Inner{
            private int size;
            public void dostuff(int size){
                size++;  // 局部变量 size;
                this.size;  // 内部类的 size
                Outer.this.size++;  // 外部类的 size
            }
        }
    }
    
```

##  局部内部类

局部内部类(Local class)是定义在代码块中的类。它们只在定义它们的代码块中是可见的。  
  
局部类有几个重要特性：

  1. 仅在定义了它们的代码块中是可见的；
  2. 可以使用定义它们的代码块中的任何局部 final 变量；
  3. 局部类不可以是 static 的，里边也不能定义 static 成员；
  4. 局部类不可以用 public、private、protected 修饰，只能使用缺省的；
  5. 局部类可以是 abstract 的。

  
请看下面的代码：
    
```java
    
    public class Outer {
        public static final int TOTAL_NUMBER = 5;
        public int id = 123;
        public void func() {
            final int age = 15;
            String str = "http://www.itbenkyou.net";
            class Inner {
                public void innerTest() {
                    System.out.println(TOTAL_NUMBER);
                    System.out.println(id);
                    // System.out.println(str);不合法，只能访问本地方法的final变量
                    System.out.println(age);
                }
            }
            new Inner().innerTest();
        }
        public static void main(String[] args) {
            Outer outer = new Outer();
            outer.func();
        }
    }
    
```

运行结果：  
5  
123  
15  

##  匿名内部类

匿名内部类是局部内部类的一种特殊形式，也就是没有变量名指向这个类的实例，而且具体的类实现会写在这个内部类里面。  
  
注意：匿名类必须继承一个父类或实现一个接口。  
  
不使用匿名内部类来实现抽象方法：

    
```java
    
    abstract class Person {
        public abstract void eat();
    }

class Child extends Person { public void eat() { System.out.println("eat
something"); } }

public class Demo { public static void main(String[] args) { Person p = new
Child(); p.eat(); } }



    
```

 
 
 运行结果：  
eat something  
  
可以看到，我们用Child继承了Person类，然后实现了Child的一个实例，将其向上转型为Person类的引用。但是，如果此处的Child类只使用一次，那么将其编写为独立的一个类岂不是很麻烦？  
  
这个时候就引入了匿名内部类。使用匿名内部类实现：
    
```java
    
    abstract class Person {
        public abstract void eat();
    }

public class Demo { public static void main(String[] args){

    
    
        // 继承 Person 类
        new Person() {
            public void eat() {
                System.out.println("eat something");
            }
        }.eat();
    }
    

}

    
```




可以看到，匿名类继承了 Person 类并在大括号中实现了抽象类的方法。  
  
内部类的语法比较复杂，实际开发中也较少用到，本教程不打算进行深入讲解，各位读者也不应该将内部类作为学习Java的重点。
