
+++
title = "再谈Java包"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:16"
categories = [
"Chinese",
]
+++


#  再谈Java包

    




在Java中，为了组织代码的方便，可以将功能相似的类放到一个文件夹内，这个文件夹，就叫做包。



  
包不但可以包含类，还可以包含接口和其他的包。  
  
目录以"\"来表示层级关系，例如 E:\Java\workspace\Demo\bin\p1\p2\Test.java。  
  
包以"."来表示层级关系，例如 p1.p2.Test 表示的目录为 \p1\p2\Test.class。

##  如何实现包

通过 package 关键字可以声明一个包，例如：  
package p1.p2;  
必须将 package 语句放在所有语句的前面，例如：

    
    

```java
          1. package p1.p2;
      2. public class Test {
      3.     public Test(){
      4.         System.out.println("我是Test类的构造方法");
      5.     }
      6. }
    
    
    
    
    package p1.p2;
    public class Test {
        public Test(){
            System.out.println("我是Test类的构造方法");
        }
    }

```
表明 Test 类位于 p1.p2 包中。

##  包的调用

在Java中，调用其他包中的类共有两种方式。  

####  1) 在每个类名前面加上完整的包名

程序举例：

    

```java
          1. public class Demo {
      2.     public static void main(String[] args) {
      3.         java.util.Date today=new java.util.Date();
      4.         System.out.println(today);
      5.     }
      6. }
    
    
    
    
    public class Demo {
        public static void main(String[] args) {
            java.util.Date today=new java.util.Date();
            System.out.println(today);
        }
    }


```

运行结果：  
Wed Dec 03 11:20:13 CST 2014

####  2) 通过 import 语句引入包中的类

程序举例：

    

```java
    
          1. import java.util.Date;
      2. // 也可以引入 java.util 包中的所有类
      3. // import java.util.*;
      4.  
      5. public class Demo {
      6.     public static void main(String[] args) {
      7.         Date today=new Date();
      8.         System.out.println(today);
      9.     }
      10. }
    
    
    
    
    import java.util.Date;
    // 也可以引入 java.util 包中的所有类
    // import java.util.*;
    
    public class Demo {
        public static void main(String[] args) {
            Date today=new Date();
            System.out.println(today);
        }
    }

```

运行结果与上面相同。  
  
实际编程中，没有必要把要引入的类写的那么详细，可以直接引入特定包中所有的类，例如 import java.util.*;。

##  类的路径

Java 在导入类时，必须要知道类的绝对路径。  
  
首先在 E:\Java\workspace\Demo\src\p0\ 目录（E:\Java\workspace\Demo\src\
是项目源文件的根目录）下创建 Demo.java，输入如下代码：


```java
    
          1. package p0;
      2. import p1.p2.Test;
      3.  
      4. public class Demo{
      5.     public static void main(String[] args){
      6.         Test obj = new Test();
      7.     }
      8. }
    
    
    
    
    package p0;
    import p1.p2.Test;
    
    public class Demo{
        public static void main(String[] args){
            Test obj = new Test();
        }
    }


```

再在 E:\Java\workspace\Demo\src\p1\p2 目录下创建 Test.java，输入如下代码：

```java
    
    


    
          1. package p1.p2;
      2.  
      3. public class Test {
      4.     public Test(){
      5.         System.out.println("我是Test类的构造方法");
      6.     }
      7. }
    
    
    
    
    package p1.p2;
    
    public class Test {
        public Test(){
            System.out.println("我是Test类的构造方法");
        }
    }

  
```

假设我们将 classpath 环境变量设置为 .;D:\Program Files\jdk1.7.0_71\lib，源文件 Demo.java 开头有
import p1.p2.Test; 语句，那么编译器会先检查 E:\Java\workspace\Demo\src\p0\p1\p2\ 目录下是否存在
Test.java 或 Test.class 文件，如果不存在，会继续检索 D:\Program Files\jdk1.7.0_71\lib\p1\p2\
目录，两个目录下都不存在就会报错。显然，Test.java 位于 E:\Java\workspace\Demo\src\p1\p2\
目录，编译器找不到，会报错，怎么办呢？  
  
可以通过 javac 命令的 classpath 选项来指定类路径。  
  


  
注意 java 命令与 javac 命令的区别，执行 javac 命令需要进入当前目录，而执行 java
命令需要进入当前目录的上级目录，并且类名前面要带上包名。  
  
可以这样来理解，javac是一个平台命令，它对具体的平台文件进行操作，要指明被编译的文件路径。而java是一个虚拟机命令，它对类操作，即对类的描述要用点分的描述形式，并且不能加扩展名，还要注意类名的大小写。  
  
这些命令比较繁杂，实际开发都需要借助 Eclipse，在Eclipse下管理包、编译运行程序都非常方便。Eclipse 实际上也是执行这些命令。

##  包的访问权限

被声明为 public 的类、方法或成员变量，可以被任何包下的任何类使用，而声明为 private 的类、方法或成员变量，只能被本类使用。  
  
没有任何修饰符的类、方法和成员变量，只能被本包中的所有类访问，在包以外任何类都无法访问它。
