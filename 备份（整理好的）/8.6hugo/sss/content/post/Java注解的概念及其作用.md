

+++
title = "Java注解的概念及其作用"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:11"
categories = [
"Chinese",
]
+++

# Java注解的概念及其作用
    



Java 5 以及更高版本允许我们在源码中插入一些补充信息，用来在编译期间给编译器发出提示/警告，或者在运行期间读取字节码文件信息，这种补充信息就称为<strong>注解（Annotation






注解均以<code>@</code>符号开头的，例如
[@Override](view/fl0yt9.html)、[@Deprecated](view/obty18.html)、[@SuppressWarnings](view/5tb54h.html)、[@SafeVarargs](view/otty5v.html)
和 [@FunctionalInterface](view/ilty98.html)，这些都是 Java 中的基本注解。  

> Annotation
> 可以翻译为"注解"或"注释"，一般翻译为"注解"，因为"注释"一词已经用于说明"//"、"/**...*/"和"/*...*/"等符号了，这里的"注释"是英文
> Comment 翻译。

注解可以元数据这个词来描述，即一种描述数据的数据。所以可以说注解就是源代码的元数据。例如以下代码：  


```java
    
    
    @Override
    public String toString() {
        return "www.itbenkyou.com是一个分享编程知识的网站。";
    }
```

上面的代码重写了 Object 类的 toString() 方法并使用了 @Override 注解。如果不使用 @Override
注解标记代码，程序也能够正常执行。那么这么写有什么好处吗？  
  
事实上，使用 @Override
注解就相当于告诉编译器这个方法是一个重写方法，如果父类中不存在该方法，编译器便会报错，提示该方法没有重写父类中的方法。这样可以防止不小心拼写错误造成麻烦。  
  
例如，在没有使用 @Override 注解的情况下，将 toString() 写成了
toStrring()，这时程序依然能编译运行，但运行结果会和所期望的结果大不相同。  
  
注解常见的作用有以下几种：

  * 生成帮助文档。这是最常见的，也是 Java 最早提供的注解。常用的有 @see、@param 和 @return 等；
  * 跟踪代码依赖性，实现替代配置文件功能。比较常见的是 Spring 2.5 开始的基于注解配置。作用就是减少配置。现在的框架基本都使用了这种配置来减少配置文件的数量；
  * 在编译时进行格式检查。如把 @Override 注解放在方法前，如果这个方法并不是重写了父类方法，则编译时就能检查出。

  
无论是哪一种注解，本质上都一种数据类型，是一种接口类型。到 Java 8 为止 Java SE 提供了 11 个内置注解。其中有 5
个是基本注解，它们来自于 java.lang 包。有 6 个是元注解，它们来自于 java.lang.annotation 包，自定义注解会用到元注解。  
  
[Java 元注解](view/1b0c2g.html)用来给其它的注解添加注解，就像C语言中的二级指针，是一个用来指向其它指针的指针。  

