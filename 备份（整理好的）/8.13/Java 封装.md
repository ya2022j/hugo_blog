+++
title = "Java 封装"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java 封装

在面向对象程式设计方法中，封装（Encapsulation）是指一种将接口的实现细节部分包装、隐藏起来的方法。要访问一个类的代码和数据，必须通过严格的接口控制。

封装最主要的功能在于我们能修改自己的实现代码，而不用修改那些调用我们代码的程序，从而把实现者和调用者解耦。

封装主要优点包括：

  * 1\. 良好的封装能够减少耦合。
  * 2\. 类内部的结构可以自由修改。
  * 3\. 可以对成员变量进行更精确的控制。
  * 4\. 隐藏信息，实现细节。



## 1\. 实现 Java 封装的步骤

1）修改属性的可见性来限制对属性的访问（一般限制为private），例如：

    
    
    public class Person {
        private String name;
        private int age;
    }
    

这段代码中，将 **name** 和 **age** 属性设置为私有的，只能本类才能访问，其他类都访问不了，如此就对信息进行了隐藏。

2）对每个值属性提供对外的公共方法访问，也就是创建一对赋取值方法，用于对私有属性的访问，例如：

    
    
    public class Person{
        private String name;
        private int age;
    ​
        public int getAge(){
            return age;
        }
    ​
        public String getName(){
            return name;
        }
    ​
        public void setAge(int age){
            this.age = age;
        }
    ​
        public void setName(String name){
            this.name = name;
        }
    }
    

采用 **this** 关键字是为了解决范例变量（private String name）和局部变量（setName(String
name)中的name变量）之间发生的同名的冲突。



## 2\. Java 封装的范例

让我们来看一个java封装类的例子：

    
    
    /* 文件名: EncapTest.java */
    public class EncapTest{
        
        private String name;
        private String idNum;
        private int age;
        
        public int getAge(){
            return age;
        }
        
        public String getName(){
            return name;
        }
        
        public String getIdNum(){
            return idNum;
        }
        
        public void setAge( int newAge){
            age = newAge;
        }
        
        public void setName(String newName){
            name = newName;
        }
        
        public void setIdNum( String newId){
            idNum = newId;
        }
    }
    

以上范例中public方法是外部类访问该类成员变量的入口。

通常情况下，这些方法被称为getter和setter方法。

因此，任何要访问类中私有成员变量的类都要通过这些getter和setter方法。

通过如下的例子说明EncapTest类的变量怎样被访问：

    
    
    public class RunEncap{
        public static void main(String args[]){
            EncapTest encap = new EncapTest();
            encap.setName("James");
            encap.setAge(20);
            
            System.out.print("Name : " + encap.getName()+ 
                                    " Age : "+ encap.getAge());
        }
    }
    

以上代码编译运行结果如下:

    
    
    Name : James Age : 20
    

