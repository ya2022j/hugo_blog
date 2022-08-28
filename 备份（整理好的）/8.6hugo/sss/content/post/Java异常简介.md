
+++
title = "Java异常简介"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:10"
categories = [
"Chinese",
]
+++
    
# Java异常简介




程序的错误可能发生在编译期间，也可以发生在运行期间，发生在运行期间的错误称为异常（Exception）。编译期间的错误可以由编译器发现并报错，运行期间的错误需要我们编写代码，借助异常处理机制来捕获。<br>
    

  
目前的主流编程语言（例如 Java、C++、c#、Ruby、Python 等）都提供了异常处理机制，用来捕获程序运行期间产生的错误，提高程序健壮性。

##  异常简介

Java
中的异常又称为例外，是一个在程序执行期间发生的事件，它中断正在执行程序的正常指令流。为了能够及时有效地处理程序中的运行错误，必须使用异常类，这可以让程序具有极好的容错性且更加健壮。  
  
在 Java 中一个异常的产生，主要有如下三种原因：

  * Java 内部错误发生异常，Java 虚拟机产生的异常。
  * 编写的程序代码中的错误所产生的异常，例如空指针异常、数组越界异常等。
  * 通过 throw 语句手动生成的异常，一般用来告知该方法的调用者一些必要信息。

  
Java
通过面向对象的方法来处理异常。在一个方法的运行过程中，如果发生了异常，则这个方法会产生代表该异常的一个对象，并把它交给运行时的系统，运行时系统寻找相应的代码来处理这一异常。  
  
我们把生成异常对象，并把它提交给运行时系统的过程称为拋出（throw）异常。运行时系统在方法的调用栈中查找，直到找到能够处理该类型异常的对象，这一个过程称为捕获（catch）异常。  

####  示例 1

为了更好地理解什么是异常，下面来看一段非常简单的 Java 程序。下面的示例代码实现了允许用户输入 1~3 以内的整数，其他情况提示输入错误。

    



##  异常类型

为了能够及时有效地处理程序中的运行错误，Java 专门引入了异常类。在 Java 中所有异常类型都是内置类 java.lang.Throwable
类的子类，即 Throwable 位于异常类层次结构的顶层。Throwable 类下有两个异常分支 Exception 和 Error，



Throwable 类是所有异常和错误的超类，下面有 Error 和 Exception 两个子类分别表示错误和异常：  

  * Exception 类用于用户程序可能出现的异常情况，它也是用来创建自定义异常类型类的类；
  * Error 定义了在通常环境下不希望被程序捕获的异常，一般指的是 JVM 错误，如堆栈溢出。

本节只讨论 Exception 类型的异常处理，不讨论关于 Error 类型的异常处理，因为 Error 通常是灾难性的致命错误，不是程序可以控制的。

异常类 Exception 又分为运行时异常和非运行时异常，这两种异常有很大的区别，也称为不检查异常（Unchecked
Exception）和检查异常（Checked Exception）。

####  1) 运行时异常

运行时异常都是 RuntimeException 类及其子类异常，如
NullPointerException、IndexOutOfBoundsException
等，这些异常是不检查异常，程序中可以选择捕获处理，也可以不处理。这些异常一般由程序逻辑错误引起，程序应该从逻辑角度尽可能避免这类异常的发生。

####  2) 非运行时异常

非运行时异常是指 RuntimeException 以外的异常，类型上都属于 Exception
类及其子类。从程序语法角度讲是必须进行处理的异常，如果不处理，程序就不能编译通过。如 IOException、ClassNotFoundException
等以及用户自定义的 Exception 异常（一般情况下不自定义检查异常）。  
  
表 1 和表 2 分别列出了 java.lang 中定义的运行时异常和非运行时异常的类型及作用。  
  
表 1 Java中常见运行时异常 异常类型 |  说明  
---|---  
ArithmeticException |  算术错误异常，如以零做除数  
ArraylndexOutOfBoundException |  数组索引越界  
ArrayStoreException |  向类型不兼容的数组元素赋值  
ClassCastException |  类型转换异常  
IllegalArgumentException |  使用非法实参调用方法  
lIIegalStateException |  环境或应用程序处于不正确的状态  
lIIegalThreadStateException |  被请求的操作与当前线程状态不兼容  
IndexOutOfBoundsException |  某种类型的索引越界  
NullPointerException |  尝试访问 null 对象成员，空指针异常  
NegativeArraySizeException |  再负数范围内创建的数组  
NumberFormatException |  数字转化格式异常，比如字符串到 float 型数字的转换无效  
TypeNotPresentException |  类型未找到  
  
表 2 Java常见非运行时异常 异常类型 |  说明  
---|---  
ClassNotFoundException |  没有找到类  
IllegalAccessException |  访问类被拒绝  
InstantiationException |  试图创建抽象类或接口的对象  
InterruptedException |  线程被另一个线程中断  
NoSuchFieldException |  请求的域不存在  
NoSuchMethodException |  请求的方法不存在  
ReflectiveOperationException |  与反射有关的异常的超类  
  
##  Error 和 Exception 的区别

Error（错误）和 Exception（异常）都是 java.lang.Throwable 类的子类，在 Java 代码中只有继承了 Throwable
类的实例才能被 throw 或者 catch。  
  
Exception 和 Error 体现了 Java 平台设计者对不同异常情况的分类，Exception
是程序正常运行过程中可以预料到的意外情况，并且应该被开发者捕获，进行相应的处理。Error 是指正常情况下不大可能出现的情况，绝大部分的 Error
都会导致程序处于非正常、不可恢复状态。所以不需要被开发者捕获。  
  
Error 错误是任何处理技术都无法恢复的情况，肯定会导致程序非正常终止。并且 Error 错误属于未检查类型，大多数发生在运行时。Exception
又分为可检查（checked）异常和不检查（unchecked）异常，可检查异常在源码里必须显示的进行捕获处理，这里是编译期检查的一部分。不检查异常就是所谓的运行时异常，通常是可以编码避免的逻辑错误，具体根据需要来判断是否需要捕获，并不会在编译器强制要求。  
  
如下是常见的 Error 和 Exception：  
  
1) 运行时异常（RuntimeException）：

  * NullPropagation：空指针异常；
  * ClassCastException：类型强制转换异常
  * IllegalArgumentException：传递非法参数异常
  * IndexOutOfBoundsException：下标越界异常
  * NumberFormatException：数字格式异常

  
2) 非运行时异常：

  * ClassNotFoundException：找不到指定 class 的异常
  * IOException：IO 操作异常

  
3) 错误（Error）：

  * NoClassDefFoundError：找不到 class 定义异常
  * StackOverflowError：深递归导致栈被耗尽而抛出的异常
  * OutOfMemoryError：内存溢出异常

####  示例 2

下面代码会导致 Java 堆栈溢出错误。

    

```java
    
    // 通过无限递归演示堆栈溢出错误
    class StackOverflow {
        public static void test(int i) {
            if (i == 0) {
                return;
            } else {
                test(i++);
            }
        }
    }
    
    public class Demo{
        public static void main(String[] args) {
            // 执行StackOverflow方法
            StackOverflow.test(5);
        }
    }
```
运行输出为：

Exception in thread "main" java.lang.StackOverflowError  
at StackOverflow.test(Demo.java:7)  
at StackOverflow.test(Demo.java:7)  
at StackOverflow.test(Demo.java:7)  
at StackOverflow.test(Demo.java:7)

上面代码通过无限递归调用最终引发了 java.lang.StackOverflowError 错误，这是一种栈溢出错误，无法再次恢复程序运行。

每个线程的栈内存都是非常受限的，通常都是几兆，如果使用的内存超出了最大值，就会导致栈溢出错误。

