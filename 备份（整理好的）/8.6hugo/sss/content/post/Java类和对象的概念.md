
+++
title = "Java类和对象的概念"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:11"
categories = [
"Chinese",
]
+++

#  Java类和对象的概念

    



Java是一门面向对象的编程语言，理解Java，首先要理解类与对象这两个概念。


    

  
Java中的类可以看做C语言中结构体的升级版。结构体是一种构造数据类型，可以包含不同的成员（变量），每个成员的数据类型可以不一样；可以通过结构体来定义结构体变量，每个变量拥有相同的性质。例如：

    
    



```commandline
    
          1. #include <stdio.h>
      2. int main(){
      3.     // 定义结构体 Student
      4.     struct Student{
      5.         // 结构体包含的变量
      6.         char *name;
      7.         int age;
      8.         float score;
      9.     };
      10.  
      11.     // 通过结构体来定义变量
      12.     struct Student stu1;
      13.     // 操作结构体的成员
      14.     stu1.name = "小明";
      15.     stu1.age = 15;
      16.     stu1.score = 92.5;
      17.   
      18.     printf("%s的年龄是 %d，成绩是 %f\n", stu1.name, stu1.age, stu1.score);
      19.  
      20.     return 0;
      21. }
    
    

```
```

    
    #include <stdio.h>
    int main(){
        // 定义结构体 Student
        struct Student{
            // 结构体包含的变量
            char *name;
            int age;
            float score;
        };
    
        // 通过结构体来定义变量
        struct Student stu1;
        // 操作结构体的成员
        stu1.name = "小明";
        stu1.age = 15;
        stu1.score = 92.5;
    
        printf("%s的年龄是 %d，成绩是 %f\n", stu1.name, stu1.age, stu1.score);
    
        return 0;
    }
```
运行结果：  
小明的年龄是 15，成绩是 92.500000  
  
Java中的类也是一种构造数据类型，但是进行了一些扩展，类的成员不但可以是变量，还可以是函数；通过类定义出来的变量也有特定的称呼，叫做"对象"。例如：

```commandline
          1. public class Demo {
      2.     public static void main(String[] args){
      3.         // 定义类Student
      4.         class Student{  // 通过class关键字类定义类
      5.             // 类包含的变量
      6.             String name;
      7.             int age;
      8.             float score;
      9.  
      10.             // 类包含的函数
      11.             void say(){
      12.                 System.out.println( name + "的年龄是 " + age + "，成绩是 " + score );
      13.             }
      14.         }
      15.  
      16.         // 通过类来定义变量，即创建对象
      17.         Student stu1 = new Student();  // 必须使用new关键字
      18.         // 操作类的成员
      19.         stu1.name = "小明";
      20.         stu1.age = 15;
      21.         stu1.score = 92.5f;
      22.         stu1.say();
      23.     }
      24. }
    
    
    
    
    public class Demo {
        public static void main(String[] args){
            // 定义类Student
            class Student{  // 通过class关键字类定义类
                // 类包含的变量
                String name;
                int age;
                float score;
    
                // 类包含的函数
                void say(){
                    System.out.println( name + "的年龄是 " + age + "，成绩是 " + score );
                }
            }
    
            // 通过类来定义变量，即创建对象
            Student stu1 = new Student();  // 必须使用new关键字
            // 操作类的成员
            stu1.name = "小明";
            stu1.age = 15;
            stu1.score = 92.5f;
            stu1.say();
        }
    }
```

运行结果：  
小明的年龄是 15，成绩是 92.5  
  
在C语言中，通过结构体名称就可以完成结构体变量的定义，并分配内存空间；但是在Java中，仅仅通过类来定义变量不会分配内存空间，必须使用new关键字来完成内存空间的分配。  
  
可以将类比喻成图纸，对象比喻成零件，图纸说明了零件的参数及其承担的任务；一张图纸可以生产出具有相同性质的零件，不同图纸可以生产不同类型的零件。  
  
在Java中，使用new关键字，就可以通过类来创建对象，即将图纸生产成零件，这个过程叫做类的实例化，因此也称对象是类的一个实例。  
  
注意：类只是一张图纸，起到说明的作用，不占用内存空间；对象才是具体的零件，要有地方来存放，才会占用内存空间。  
  
类所包含的变量和函数都有特定的称呼，变量被称为属性（通常也称成员变量），函数被称为方法，属性和方法统称为类的成员。

##  面向对象编程(Object Oriented Programming, OOP)

类是一个通用的概念，Java、C++、C#、PHP等很多编程语言中都有类，都可以通过类创建对象。可以将类看做是结构体的升级版，C语言的晚辈们看到了C语言的不足，尝试加以改善，继承了结构体的思想，并进行了升级，让程序员在开发或扩展大中型项目时更加容易。  
  
因为Java、C++等语言都支持类和对象，所以使用这些语言编写程序也被称为面向对象编程，这些语言也被称为面向对象的编程语言。C语言因为不支持类和对象的概念，被称为面向过程的编程语言。  
  
实际上，面向对象只是面向过程的升级。  
  
在C语言中，可以将完成某个功能的重复使用的代码块定义为函数，将具有一类功能的函数声明在一个头文件中，不同类型的函数声明在不同的头文件，以便对函数进行更好的管理，方便编写和调用。  
  
在Java中，可以将完成某个功能的代码块定义为方法，将具有相似功能的方法定义在一个类中，也就是定义在一个源文件中（因为一个源文件只能包含一个公共的类），多个源文件可以位于一个文件夹，这个文件夹有特定的称呼，叫做包。  


