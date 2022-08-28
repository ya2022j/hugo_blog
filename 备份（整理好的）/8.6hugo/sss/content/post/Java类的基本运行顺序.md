
+++
title = "Java类的基本运行顺序"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:11"
categories = [
"Chinese",
]
+++

# Java类的基本运行顺序

    




我们以下面的类来说明一个基本的 Java 类的运行顺序：
    
    

```java

    
    public class Demo{
        private String name;
        private int age;
    
    
    public Demo(){
        name = "itbenkyou";
        age = 3;
    }
    public static void main(String[] args){
        Demo obj = new Demo();
        System.out.println(obj.name + "的年龄是" + obj.age);
    }
    

}
 ```


 
 基本运行顺序是：

  1. 先运行到第 9 行，这是程序的入口。
  2. 然后运行到第 10 行，这里要 new 一个Demo，就要调用 Demo 的构造方法。
  3. 就运行到第 5 行，注意：可能很多人觉得接下来就应该运行第 6 行了，错！初始化一个类，必须先初始化它的属性。
  4. 因此运行到第 2 行，然后是第 3 行。
  5. 属性初始化完过后，才回到构造方法，执行里面的代码，也就是第 6 行、第 7 行。
  6. 然后是第8行，表示 new 一个Demo实例完成。
  7. 然后回到 main 方法中执行第 11 行。
  8. 然后是第 12 行，main方法执行完毕。

  
作为程序员，应该清楚程序的基本运行过程，否则糊里糊涂的，不利于编写代码，也不利于技术上的发展
