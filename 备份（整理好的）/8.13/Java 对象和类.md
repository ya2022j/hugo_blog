+++
title = "Java 对象和类"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java 对象和类

Java一种面向对象语言。使用 Java 语言编程，必须深刻的理解面向对象的基本概念。



## 1\. 什么是面向对象

面向对象是一种软件开发方法。面向对象是把数据及对数据的操作方法放在一起，作为一个相互依存的整体。

面向对象的三大特征是抽象、继承、多态：

  * 封装

封装是面向对象的特征之一，是对象和类概念的主要特性。封装就是把客观事物封装成抽象的类，通过类把自己的数据和方法只让可信的类或者对象操作，对不可信的进行信息隐藏。

  * 继承

继承是使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。

通过继承创建的新类称为“子类”或“派生类”。

被继承的类称为“基类”、“父类”或“超类”。

  * 多态

多态是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，父对象就可以根据当前赋值给它的子对象的特性以不同的方式运作。简单的说，就是一句话：允许将子类类型的指针赋值给父类类型的指针。



## 2\. Java 对象

什么是对象？看看周围真实的世界，会发现身边有很多对象，车，狗，人等等。所有这些对象都有自己的状态和行为。

拿一条狗来举例，它的状态有：名字、品种、颜色，行为有：叫、摇尾巴和跑。对比现实对象和软件对象，它们之间十分相似。

软件对象也有状态和行为。软件对象的状态就是属性，行为通过方法体现。在软件开发中，方法操作对象内部状态的改变，对象的相互调用也是通过方法来完成。



## 3\. Java 类

类可以看成是创建 Java 对象的模板。

通过上图创建一个简单的类来理解下 Java 中类的定义：

        
                public class Dog {
            String breed;
            int size;
            String colour;
            int age;
         
            void eat() {
            }
         
            void run() {
            }
         
            void sleep(){
            }
         
            void name(){
            }
        }
        

一个类可以包含以下类型变量：

      * **局部变量** ：在方法、构造方法或者语句块中定义的变量被称为局部变量。变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁。
      * **成员变量** ：成员变量是定义在类中，方法体之外的变量。这种变量在创建对象的时候范例化。成员变量可以被类中方法、构造方法和特定类的语句块访问。
      * **类变量** ：类变量也声明在类中，方法体之外，但必须声明为 static 类型。

一个类可以拥有多个方法，在上面的例子中：eat()、run()、sleep() 和 name() 都是 Dog 类的方法。



## 4\. 构造方法

每个类都有构造方法。如果没有显式地为类定义构造方法，Java 编译器将会为该类提供一个默认构造方法。

在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名，一个类可以有多个构造方法。

下面是一个构造方法示例：

        
                public class Puppy{
            public Puppy(){
            }
         
            public Puppy(String name){
                // 这个构造器仅有一个参数：name
            }
        }
        



## 5\. 创建对象

对象是根据类创建的。在Java中，使用关键字 new 来创建一个新的对象。创建对象需要以下三步：

      * **声明** ：声明一个对象，包括对象名称和对象类型。
      * **范例化** ：使用关键字 new 来创建一个对象。
      * **初始化** ：使用 new 创建对象时，会调用构造方法初始化对象。

下面是一个创建对象的例子：

        
                public class Puppy{
           public Puppy(String name){
              //这个构造器仅有一个参数：name
              System.out.println("小狗的名字是 : " + name ); 
           }
           public static void main(String[] args){
              // 下面的语句将创建一个Puppy对象
              Puppy myPuppy = new Puppy( "tommy" );
           }
        }
        

编译并运行上面的程序，会打印出下面的结果：

        
                小狗的名字是 : tommy
        



## 6\. 访问范例的变量和方法

通过已创建的对象来访问成员变量和成员方法，如下所示：

        
                /* 范例化对象 */
        Object referenceVariable = new Constructor();
        /* 访问类中的变量 */
        referenceVariable.variableName;
        /* 访问类中的方法 */
        referenceVariable.methodName();
        

下面的例子展示如何访问范例变量和调用成员方法：

        
                public class Puppy{
           int puppyAge;
           public Puppy(String name){
              // 这个构造器仅有一个参数：name
              System.out.println("小狗的名字是 : " + name ); 
           }
         
           public void setAge( int age ){
               puppyAge = age;
           }
         
           public int getAge( ){
               System.out.println("小狗的年龄为 : " + puppyAge ); 
               return puppyAge;
           }
         
           public static void main(String[] args){
              /* 创建对象 */
              Puppy myPuppy = new Puppy( "tommy" );
              /* 通过方法来设定age */
              myPuppy.setAge( 2 );
              /* 调用另一个方法获取age */
              myPuppy.getAge( );
              /*你也可以像下面这样访问成员变量 */
              System.out.println("变量值 : " + myPuppy.puppyAge ); 
           }
        }
        

编译并运行上面的程序，产生如下结果：

        
                小狗的名字是 : tommy
        小狗的年龄为 : 2
        变量值 : 2
        



## 7\. 源文件声明规则

在本节的最后部分，我们将学习源文件的声明规则。当在一个源文件中定义多个类，并且还有import语句和package语句时，要特别注意这些规则。

      * 一个源文件中只能有一个 public 类
      * 一个源文件可以有多个非 public 类
      * 源文件的名称应该和 public 类的类名保持一致。例如：源文件中 public 类的类名是 Employee，那么源文件应该命名为Employee.java。
      * 如果一个类定义在某个包中，那么 package 语句应该在源文件的首行。
      * 如果源文件包含 import 语句，那么应该放在 package 语句和类定义之间。如果没有 package 语句，那么 import 语句应该在源文件中最前面。
      * import 语句和 package 语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。

类有若干种访问级别，并且类也分不同的类型：抽象类和 final 类等。这些将在访问控制章节介绍。

除了上面提到的几种类型，Java 还有一些特殊的类，如：内部类、匿名类。



## 8\. Java 包

包主要用来对类和接口进行分类。当开发 Java 程序时，可能编写成百上千的类，因此很有必要对类和接口进行分类。

在 Java 中，如果给出

