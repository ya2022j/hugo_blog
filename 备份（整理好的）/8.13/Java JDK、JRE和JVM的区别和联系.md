+++
title = "Java JDK、JRE和JVM的区别和联系"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java JDK、JRE和JVM的区别和联系



## 1\. JDK（java development kit）

JDK 是 Java 的开发工具包，是整个 Java 的核心。

JDK 提供了Java 的开发环境（javac等）和 运行环境（JVM和核心类库）。

JDK的安装目录下有六个文件夹，其中，真正在运行java程序时起作用的是四个文件夹：

  * bin： javac 编译器
  * include：Java 和 jvm交互用的头文件
  * lib： 类库
  * jre： 运行环境



## 2\. JRE（Java runtime environment）

JRE 即 java 运行环境，包括 java 虚拟机（JVM）、Java 平台核心类和支持文件，但是不包括开发工具（编译器、调试器等）。

JRE 面向 Java 程序的使用者。如果只安装 JRE，则系统只能运行 Java 程序。



## 3\. JVM（Java virtual machine）

JVM 即 Java 虚拟机，它是 Java 跨平台的核心。

JVM 的作用是解释由 JDK 生成的指令集（即字节码）给系统，从而运行 Java 应用程序。



## 4\. Java 程序编译原理

源程序由 JDK 的 javac 生成类文件 .class 文件，JVM 将 .class 文件解释给系统。

Java 程序的字节码文件可以放到任意装有 JRE 的计算机运行，再由不同 JRE 的将它们转化成相应的机器代码，这就实现了 Java 程序的可移植性。

传统的编译方法，先转化到字节码（ bytecode ）
这种特殊的中间形式，字节码再转换成机器码或系统调用。生成的机器代码就不可避免地跟特殊的操作系统和特殊的机器结构相关。



## 5\. 三者的联系与区别

JDK 包含 JRE，JRE 包含 JVM。



