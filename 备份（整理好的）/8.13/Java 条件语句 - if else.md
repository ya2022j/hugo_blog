+++
title = "Java 条件语句 - if else"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java 条件语句 - if else

一个 if 语句包含一个布尔表达式和一条或多条语句。



## 1\. if 语句

如果布尔表达式的值为 true，则执行 if 语句中的代码块，否则执行 if 语句块后面的代码。

### 1）if 语句的语法

    
    
    if(布尔表达式)
    {
       //如果布尔表达式为true将执行的语句
    }
    

### 2）if 语句的范例

    
    
    public class Test {
     
       public static void main(String args[]){
          int x = 10;
     
          if( x < 20 ){
             System.out.print("这是 if 语句");
          }
       }
    }
    

以上代码编译运行结果如下：

    
    
    这是 if 语句
    



## 2\. if...else 语句

if 语句后面可以跟 else 语句，当 if 语句的布尔表达式值为 false 时，else 语句块会被执行。

### 1）if...else 语句的语法

    
    
    if(布尔表达式){
       //如果布尔表达式的值为true
    }else{
       //如果布尔表达式的值为false
    }
    

### 2）if...else 语句的范例

    
    
    public class Test {
     
       public static void main(String args[]){
          int x = 30;
     
          if( x < 20 ){
             System.out.print("这是 if 语句");
          }else{
             System.out.print("这是 else 语句");
          }
       }
    }
    

以上代码编译运行结果如下：

    
    
    这是 else 语句
    



## 3\. if...else if...else 语句

if 语句后面可以跟 else if...else 语句，这种语句可以检测到多种可能的情况。

使用 if，else if，else 语句的时候，需要注意下面几点：

  * if 语句至多有 1 个 else 语句，else 语句在所有的 else if 语句之后。
  * if 语句可以有若干个 else if 语句，它们必须在 else 语句之前。
  * 一旦其中一个 else if 语句检测为 true，其他的 else if 以及 else 语句都将跳过执行。

### 1）if...else if...else 语句的语法

    
    
    if(布尔表达式 1){
       //如果布尔表达式 1的值为true执行代码
    }else if(布尔表达式 2){
       //如果布尔表达式 2的值为true执行代码
    }else if(布尔表达式 3){
       //如果布尔表达式 3的值为true执行代码
    }else {
       //如果以上布尔表达式都不为true执行代码
    }
    

### 2）if...else if...else 语句的范例

    
    
    public class Test {
       public static void main(String args[]){
          int x = 30;
     
          if( x == 10 ){
             System.out.print("Value of X is 10");
          }else if( x == 20 ){
             System.out.print("Value of X is 20");
          }else if( x == 30 ){
             System.out.print("Value of X is 30");
          }else{
             System.out.print("这是 else 语句");
          }
       }
    }
    

以上代码编译运行结果如下：

    
    
    Value of X is 30
    



## 4\. 嵌套的 if…else 语句

使用嵌套的 if…else 语句是合法的。也就是说你可以在另一个 if 或者 else if 语句中使用 if 或者 else if 语句。

### 1）嵌套 if…else 语句的语法

    
    
    if(布尔表达式 1){
       ////如果布尔表达式 1的值为true执行代码
       if(布尔表达式 2){
          ////如果布尔表达式 2的值为true执行代码
       }
    }
    

你可以像 if 语句一样嵌套 else if...else。

### 2）嵌套 if…else 语句的范例

    
    
    public class Test {
     
       public static void main(String args[]){
          int x = 30;
          int y = 10;
     
          if( x == 30 ){
             if( y == 10 ){
                 System.out.print("X = 30 and Y = 10");
              }
           }
        }
    }
    

以上代码编译运行结果如下：

    
    
    X = 30 and Y = 10
    

