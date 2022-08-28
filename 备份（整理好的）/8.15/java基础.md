



# Java 简介

Java 是由 Sun Microsystems 公司于 1995 年 5 月推出的 Java 面向对象程序设计语言和 Java 平台的总称。由 James
Gosling和同事们共同研发，并在 1995 年正式推出。

后来 Sun 公司被 Oracle （甲骨文）公司收购，Java 也随之成为 Oracle 公司的产品。

Java分为三个体系：

  * JavaSE（J2SE）（Java2 Platform Standard Edition，java平台标准版）
  * JavaEE(J2EE)(Java 2 Platform,Enterprise Edition，java平台企业版)
  * JavaME(J2ME)(Java 2 Platform Micro Edition，java平台微型版)。

2005 年 6 月，JavaOne 大会召开，SUN 公司公开 Java SE 6。此时，Java 的各种版本已经更名，以取消其中的数字 "2"：J2EE
更名为 Java EE，J2SE 更名为Java SE，J2ME 更名为 Java ME。

* * *

##  主要特性

  * **Java 语言是简单的：**

Java 语言的语法与 C 语言和 C++ 语言很接近，使得大多数程序员很容易学习和使用。另一方面，Java 丢弃了 C++
中很少使用的、很难理解的、令人迷惑的那些特性，如操作符重载、多继承、自动的强制类型转换。特别地，Java
语言不使用指针，而是引用。并提供了自动分配和回收内存空间，使得程序员不必为内存管理而担忧。

  * **Java 语言是面向对象的：**

Java 语言提供类、接口和继承等面向对象的特性，为了简单起见，只支持类之间的单继承，但支持接口之间的多继承，并支持类与接口之间的实现机制（关键字为
implements）。Java 语言全面支持动态绑定，而 C++语言只对虚函数使用动态绑定。总之，Java语言是一个纯的面向对象程序设计语言。

  * **Java语言是分布式的：**

Java 语言支持 Internet 应用的开发，在基本的 Java 应用编程接口中有一个网络应用编程接口（java
net），它提供了用于网络应用编程的类库，包括 URL、URLConnection、Socket、ServerSocket 等。Java 的
RMI（远程方法激活）机制也是开发分布式应用的重要手段。

  * **Java 语言是健壮的：**

Java 的强类型机制、异常处理、垃圾的自动收集等是 Java 程序健壮性的重要保证。对指针的丢弃是 Java 的明智选择。Java 的安全检查机制使得
Java 更具健壮性。

  * **Java语言是安全的：**

Java通常被用在网络环境中，为此，Java 提供了一个安全机制以防恶意代码的攻击。除了Java 语言具有的许多安全特性以外，Java
对通过网络下载的类具有一个安全防范机制（类 ClassLoader），如分配不同的名字空间以防替代本地的同名类、字节代码检查，并提供安全管理机制（类
SecurityManager）让 Java 应用设置安全哨兵。

  * **Java 语言是体系结构中立的：**

Java 程序（后缀为 java 的文件）在 Java 平台上被编译为体系结构中立的字节码格式（后缀为 class 的文件），然后可以在实现这个 Java
平台的任何系统中运行。这种途径适合于异构的网络环境和软件的分发。

  * **Java 语言是可移植的：**

这种可移植性来源于体系结构中立性，另外，Java 还严格规定了各个基本数据类型的长度。Java 系统本身也具有很强的可移植性，Java 编译器是用 Java
实现的，Java 的运行环境是用 ANSI C 实现的。

  * **Java 语言是解释型的：**

如前所述，Java 程序在 Java 平台上被编译为字节码格式，然后可以在实现这个 Java 平台的任何系统中运行。在运行时，Java 平台中的 Java
解释器对这些字节码进行解释执行，执行过程中需要的类在联接阶段被载入到运行环境中。

  * **Java 是高性能的：**

与那些解释型的高级脚本语言相比，Java 的确是高性能的。事实上，Java 的运行速度随着 JIT(Just-In-Time）编译器技术的发展越来越接近于
C++。

  * **Java 语言是多线程的：**

在 Java 语言中，线程是一种特殊的对象，它必须由 Thread 类或其子（孙）类来创建。通常有两种方法来创建线程：其一，使用型构为
Thread(Runnable) 的构造子类将一个实现了 Runnable 接口的对象包装成一个线程，其二，从 Thread 类派生出子类并重写 run
方法，使用该子类创建的对象即为线程。值得注意的是 Thread 类已经实现了 Runnable 接口，因此，任何一个线程均有它的 run 方法，而 run
方法中包含了线程所要运行的代码。线程的活动由一组方法来控制。Java 语言支持多个线程的同时执行，并提供多线程之间的同步机制（关键字为
synchronized）。

  * **Java 语言是动态的：**

Java 语言的设计目标之一是适应于动态变化的环境。Java
程序需要的类能够动态地被载入到运行环境，也可以通过网络来载入所需要的类。这也有利于软件的升级。另外，Java
中的类有一个运行时刻的表示，能进行运行时刻的类型检查。

* * *

## 发展历史

  * 1995 年 5 月 23 日，Java 语言诞生

  * 1996 年 1 月，第一个 JDK-JDK1.0 诞生

  * 1996 年 4 月，10 个最主要的操作系统供应商申明将在其产品中嵌入 JAVA 技术

  * 1996 年 9 月，约 8.3 万个网页应用了 JAVA 技术来制作

  * 1997 年 2 月 18 日，JDK1.1 发布

  * 1997 年 4 月 2 日，JavaOne 会议召开，参与者逾一万人，创当时全球同类会议规模之纪录

  * 1997 年 9 月，JavaDeveloperConnection 社区成员超过十万

  * 1998 年 2 月，JDK1.1 被下载超过 2,000,000次

  * 1998 年 12 月 8 日，JAVA2 企业平台 J2EE 发布

  * 1999 年 6月，SUN 公司发布 Java 的三个版本：标准版（JavaSE, 以前是 J2SE）、企业版（JavaEE 以前是 J2EE）和微型版（JavaME，以前是 J2ME）

  * 2000 年 5 月 8 日，JDK1.3 发布

  * 2000 年 5 月 29 日，JDK1.4 发布

  * 2001 年 6 月 5 日，NOKIA 宣布，到 2003 年将出售 1 亿部支持 Java 的手机

  * 2001 年 9 月 24 日，J2EE1.3 发布

  * 2002 年 2 月 26 日，J2SE1.4 发布，自此 Java 的计算能力有了大幅提升

  * 2004 年 9 月 30 日 18:00PM，J2SE1.5 发布，成为 Java 语言发展史上的又一里程碑。为了表示该版本的重要性，J2SE1.5 更名为 Java SE 5.0

  * 2005 年 6 月，JavaOne 大会召开，SUN 公司公开 Java SE 6。此时，Java 的各种版本已经更名，以取消其中的数字 "2"：J2EE 更名为 Java EE，J2SE 更名为 Java SE，J2ME 更名为 Java ME

  * 2006 年 12 月，SUN 公司发布 JRE6.0

  * **2009 年 04 月 20 日，甲骨文 74 亿美元收购 Sun，取得 Java 的版权。**

  * 2010 年 11 月，由于甲骨文对于 Java 社区的不友善，因此 Apache 扬言将退出 JCP。

  * 2011 年 7 月 28 日，甲骨文发布 Java7.0 的正式版。

  * 2014 年 3 月 18 日，Oracle 公司发表 Java SE 8。

  * 2017 年 9 月 21 日，Oracle 公司发表 Java SE 9

  * 2018 年 3 月 21 日，Oracle 公司发表 Java SE 10

  * 2018 年 9 月 25 日，Java SE 11 发布

  * 2019 年 3 月 20 日，Java SE 12 发布

    


# Java 变量

Java 变量是在 Java 语言中通过名字可以访问的一块内存空间，里面存储的数据可以在程序运行时修改。



## 1\. Java 变量定义

在Java语言中，所有的变量在使用前必须声明。

### 1）Java 变量声明的语法




```java
type identifier [ = value][, identifier [= value] ...];
```


说明：type为Java数据类型。identifier是变量名。可以使用逗号隔开来声明多个同类型变量。

### 2）Java 变量声明的范例




```java
int a, b, c;         // 声明三个int型整数：a、 b、c	
int d = 3, e = 4, f = 5; // 声明三个整数并赋予初值
byte z = 22;         // 声明并初始化 z
String s = "codebaoku";  // 声明并初始化字符串 s
double pi = 3.14159; // 声明了双精度浮点型变量 pi
char x = 'x';        // 声明变量 x 的值是字符 'x'。
```


### 3）Java语言支持的变量类型

  * 类变量：独立于方法之外的变量，用 static 修饰。

  * 范例变量：独立于方法之外的变量，不过没有 static 修饰。 

  * 局部变量：类的方法中的变量。

    ```java
    public class Variable{
        static int allClicks=0;    // 类变量
        String str="hello world";  // 范例变量
        public void method(){ 
            int i =0;  // 局部变量
        }
    }
    ```

    

    



## 2\. Java 局部变量

  * 局部变量声明在方法、构造方法或者语句块中；
  * 局部变量在方法、构造方法、或者语句块被执行的时候创建，当它们执行完成后，变量将会被销毁；
  * 访问修饰符不能用于局部变量；
  * 局部变量只在声明它的方法、构造方法或者语句块中可见；
  * 局部变量是在栈上分配的。
  * 局部变量没有默认值，所以局部变量被声明后，必须经过初始化，才可以使用。

在以下范例中age是一个局部变量。定义在pupAge()方法中，它的作用域就限制在这个方法中。




```java
package com.codebaoku.test;
public class Test{ 
   public void pupAge(){
      int age = 0;
      age = age + 7;
      System.out.println("小狗的年龄是: " + age);
   }
   
   public static void main(String[] args){
      Test test = new Test();
      test.pupAge();
   }
}
```


以上范例编译运行结果如下:




```java
小狗的年龄是: 7
```


在下面的例子中 age 变量没有初始化，所以在编译时会出错：




```java
package com.codebaoku.test;
 
public class Test{ 
   public void pupAge(){
      int age;
      age = age + 7;
      System.out.println("小狗的年龄是 : " + age);
   }
   
   public static void main(String[] args){
      Test test = new Test();
      test.pupAge();
   }
}
```


以上范例编译运行结果如下:




```java
Test.java:4:variable number might not have been initialized
age = age + 7;
         ^
1 error
```




## 3\. 范例变量

  * 范例变量声明在一个类中，但在方法、构造方法和语句块之外；

  * 当一个对象被范例化之后，每个范例变量的值就跟着确定；

  * 范例变量在对象创建的时候创建，在对象被销毁的时候销毁；

  * 范例变量的值应该至少被一个方法、构造方法或者语句块引用，使得外部能够通过这些方式获取范例变量信息；

  * 范例变量可以声明在使用前或者使用后；

  * 访问修饰符可以修饰范例变量；

  * 范例变量对于类中的方法、构造方法或者语句块是可见的。一般情况下应该把范例变量设为私有。通过使用访问修饰符可以使范例变量对子类可见；

  * 范例变量具有默认值。数值型变量的默认值是0，布尔型变量的默认值是false，引用类型变量的默认值是null。变量的值可以在声明时指定，也可以在构造方法中指定；

  * 范例变量可以直接通过变量名访问。但在静态方法以及其他类中，就应该使用完全限定名：ObejectReference.VariableName。

    

    ```java
    import java.io.*;
    public class Employee{
       // 这个范例变量对子类可见
       public String name;
       // 私有变量，仅在该类可见
       private double salary;
       //在构造器中对name赋值
       public Employee (String empName){
          name = empName;
       }
       //设定salary的值
       public void setSalary(double empSal){
          salary = empSal;
       }  
       // 打印信息
       public void printEmp(){
          System.out.println("名字 : " + name );
          System.out.println("薪水 : " + salary);
       }
    
       public static void main(String[] args){
          Employee empOne = new Employee("RUNOOB");
          empOne.setSalary(1000.0);
          empOne.printEmp();
       }
    }
    ```

    

    

以上范例编译运行结果如下:




```java
$ javac Employee.java 
$ java Employee
名字 : RUNOOB
薪水 : 1000.0
```




## 4\. 类变量（静态变量）

  * 类变量也称为静态变量，在类中以 static 关键字声明，但必须在方法之外。

  * 无论一个类创建了多少个对象，类只拥有类变量的一份拷贝。

  * 静态变量除了被声明为常量外很少使用，静态变量是指声明为 public/private，final 和 static 类型的变量。静态变量初始化后不可改变。

  * 静态变量储存在静态存储区。经常被声明为常量，很少单独使用 static 声明变量。

  * 静态变量在第一次被访问时创建，在程序结束时销毁。

  * 与范例变量具有相似的可见性。但为了对类的使用者可见，大多数静态变量声明为 public 类型。

  * 默认值和范例变量相似。数值型变量默认值是 0，布尔型默认值是 false，引用类型默认值是 null。变量的值可以在声明的时候指定，也可以在构造方法中指定。此外，静态变量还可以在静态语句块中初始化。

  * 静态变量可以通过： _ClassName.VariableName_ 的方式访问。

  * 类变量被声明为 public static final 类型时，类变量名称一般建议使用大写字母。如果静态变量不是 public 和 final 类型，其命名方式与范例变量以及局部变量的命名方式一致。

    

    

以上范例编译运行结果如下:




```java
开发人员平均工资:10000.0
```


**注意：** 如果其他类想要访问该变量，可以这样访问： **Employee.DEPARTMENT** 。




# Java 基本语法

Java 程序是一系列对象的集合，对象通过调用彼此的方法协同工作。Java 程序中基本概念包括：类、对象、方法和范例变量。

  * **对象** ：对象是类的一个范例，有状态和行为。例如，一条狗是一个对象，它的状态有：颜色、名字、品种；行为有：摇尾巴、叫、吃等。
  * **类** ：类是一个模板，它描述一类对象的行为和状态。
  * **方法** ：方法就是行为，一个类可以有很多方法。逻辑运算、数据修改以及所有动作都是在方法中完成的。
  * **范例变量** ：每个对象都有独特的范例变量，对象的状态由这些范例变量的值决定。



## 1\. Java 程序范例

下面看一个简单的 Java 程序，它将输出字符串 _Hello World_




```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World"); // 输出 Hello World
    }
}
```




下面将逐步介绍如何保存、编译以及运行这个程序：

  * 打开代码编辑器，把上面的代码添加进去；
  * 把文件名保存为：HelloWorld.java；
  * 打开 cmd 命令窗口，进入目标文件所在的位置，假设是 C:\
  * 在命令行窗口输入 javac HelloWorld.java 按下回车键编译代码。如果代码没有错误，cmd 命令提示符会进入下一行（假设环境变量都设置好了）。
  * 再键输入 java HelloWorld 按下回车键就可以运行程序了

程序运行后，输出 Hello World。




```java
$ javac HelloWorld.java
$ java HelloWorld 
Hello World
```


如果遇到编码问题，我们可以使用 -encoding 选项设置 **utf-8** 来编译：




```java
javac -encoding UTF-8 HelloWorld.java 
java HelloWorld 
```



## 2\. 基本语法

编写 Java 程序时，应注意以下几点：

  * **大小写敏感** ：Java 是大小写敏感的，这就意味着标识符 Hello 与 hello 是不同的。
  * **类名** ：对于所有的类来说，类名的首字母应该大写。如果类名由若干单词组成，那么每个单词的首字母应该大写，例如 **MyFirstJavaClass** 。
  * **方法名** ：所有的方法名都应该以小写字母开头。如果方法名含有若干单词，则后面的每个单词首字母大写。
  * **源文件名** ：源文件名必须和类名相同。当保存文件的时候，你应该使用类名作为文件名保存（切记 Java 是大小写敏感的），文件名的后缀为 **.java** 。（如果文件名和类名不相同则会导致编译错误）。
  * **主方法入口** ：所有的 Java 程序由 **public static void main(String[] args)** 方法开始执行。



## 3\. Java 标识符

Java 所有的组成部分都需要名字。类名、变量名以及方法名都被称为标识符。

关于 Java 标识符，有以下几点需要注意：

  * 所有的标识符都应该以字母（A-Z 或者 a-z）,美元符（$）、或者下划线（_）开始
  * 首字符之后可以是字母（A-Z 或者 a-z）,美元符（$）、下划线（_）或数字的任何字符组合
  * 关键字不能用作标识符
  * 标识符是大小写敏感的
  * 合法标识符举例：age、$salary、_value、__1_value
  * 非法标识符举例：123abc、-salary



## 4\. Java修饰符

像其他语言一样，Java可以使用修饰符来修饰类中方法和属性。主要有两类修饰符：

  * 访问控制修饰符 : default, public , protected, private
  * 非访问控制修饰符 : final, abstract, static, synchronized 

在后面的章节中我们会深入讨论 Java 修饰符。





## 5\. Java 数组

数组是储存在堆上的对象，可以保存多个同类型变量。在后面的章节中，我们将会学到如何声明、构造以及初始化一个数组。



## 6\. Java 枚举

Java 5.0引入了枚举，枚举限制变量只能是预先设定好的值。使用枚举可以减少代码中的 bug。

例如，我们为果汁店设计一个程序，它将限制果汁为小杯、中杯、大杯。这就意味着它不允许顾客点除了这三种尺寸外的果汁。




```java
class FreshJuice {
   enum FreshJuiceSize{ SMALL, MEDIUM , LARGE }
   FreshJuiceSize size;
}
 
public class FreshJuiceTest {
   public static void main(String[] args){
      FreshJuice juice = new FreshJuice();
      juice.size = FreshJuice.FreshJuiceSize.MEDIUM  ;
   }
}
```


**注意：** 枚举可以单独声明或者声明在类里面。方法、变量、构造函数也可以在枚举中定义。



## 7\. Java 关键字

下面列出了 Java 关键字。这些保留字不能用于常量、变量、和任何标识符的名称。

| 类别         | 关键字                         | 说明                 |
| ------------ | ------------------------------ | -------------------- |
| private      | 私有的                         |                      |
| protected    | 受保护的                       |                      |
| public       | 公共的                         |                      |
| default      | 默认                           | 类、方法和变量修饰符 |
| abstract     | 声明抽象                       |                      |
| class        | 类                             |                      |
| extends      | 扩充,继承                      |                      |
| final        | 最终值,不可改变的              |                      |
| implements   | 实现（接口）                   |                      |
| interface    | 接口                           |                      |
| native       | 本地，原生方法（非 Java 实现） |                      |
| new          | 新,创建                        |                      |
| static       | 静态                           |                      |
| strictfp     | 严格,精准                      |                      |
| synchronized | 线程,同步                      |                      |
| transient    | 短暂                           |                      |
| volatile     | 易失                           |                      |
| 程序控制语句 | break                          | 跳出循环             |
| case         | 定义一个值以供 switch 选择     |                      |
| continue     | 继续                           |                      |
| default      | 默认                           |                      |
| do           | 运行                           |                      |
| else         | 否则                           |                      |
| for          | 循环                           |                      |
| if           | 如果                           |                      |
| instanceof   | 范例                           |                      |
| return       | 返回                           |                      |
| switch       | 根据值选择执行                 |                      |
| while        | 循环                           |                      |
| 错误处理     | assert                         | 断言表达式是否为真   |
| catch        | 捕捉异常                       |                      |
| finally      | 有没有异常都执行               |                      |
| throw        | 抛出一个异常对象               |                      |
| throws       | 声明一个异常可能被抛出         |                      |
| try          | 捕获异常                       |                      |
| 包相关       | import                         | 引入                 |
| package      | 包                             |                      |
| 基本类型     | boolean                        | 布尔型               |
| byte         | 字节型                         |                      |
| char         | 字符型                         |                      |
| double       | 双精度浮点                     |                      |
| float        | 单精度浮点                     |                      |
| int          | 整型                           |                      |
| long         | 长整型                         |                      |
| short        | 短整型                         |                      |
| 变量引用     | super                          | 父类,超类            |
| this         | 本类                           |                      |
| void         | 无返回值                       |                      |
| 保留关键字   | goto                           | 是关键字，但不能使用 |
| const        | 是关键字，但不能使用           |                      |
| null         | 空                             |                      |



## 8\. Java注释

类似于 C/C++、Java 也支持单行以及多行注释。注释中的字符将被 Java 编译器忽略。




```java
public class HelloWorld {
   /* 输出 Hello World
    * 这是一个多行注释的示例
    */
    public static void main(String[] args){
       // 这是单行注释的示例
       /* 这个也是单行注释的示例 */
       System.out.println("Hello World"); 
    }
}
```




## 9\. Java 空行

空白行或者有注释的行，Java 编译器都会忽略掉。



## 10\. 继承

在 Java 中，一个类可以由其他类派生。如果你要创建一个类，而且已经存在一个类具有你所需要的属性或方法，那么你可以将新创建的类继承该类。

利用继承的方法，可以重用已存在类的方法和属性，而不用重写这些代码。被继承的类称为超类（super class），派生类称为子类（subclass）。



## 11\. 接口

在 Java 中，接口可理解为对象间相互通信的协议。接口在继承中扮演着很重要的角色。

接口只定义派生要用到的方法，但是方法的具体实现完全取决于派生类。





# Java 修饰符

Java语言提供了很多修饰符，主要分为以下两类：

  * 访问控制修饰符
  * 非访问控制修饰符

修饰符用来定义类、方法或者变量，通常放在语句的最前端。




```java
public class ClassName {
}
private boolean myFlag;
static final double weeks = 9.5;
protected static final int BOXWIDTH = 42;
public static void main(String[] arguments) {
}
```


其中 private, public, protected, static, final 都是修饰符。



## 1\. 访问控制修饰符

Java中，可以使用访问控制符来保护对类、变量、方法和构造方法的访问。Java 支持 4 种不同的访问权限。

  * **default** (即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。
  * **private** : 在同一类内可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**
  * **public** : 对所有类可见。使用对象：类、接口、变量、方法
  * **protected** : 对同一包内的类和所有子类可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）** 。

我们可以通过以下表来说明访问权限：

| 访问控制 修饰符 | 当前类 | 同一包内 | 子孙类(同一包) | 子孙类(不同包) | 其他包 |
| --------------- | ------ | -------- | -------------- | -------------- | ------ |
| public          | Y      | Y        | Y              | Y              | Y      |
| protected       | Y      | Y        | Y              | Y/N（说明）    | N      |
| default         | Y      | Y        | Y              | N              | N      |
| private         | Y      | N        | N              | N              | N      |

### 1）无访问修饰符

使用默认访问修饰符声明的变量和方法，对同一个包内的类是可见的。

接口里的变量都隐式声明为 public static final,而接口里的方法默认情况下访问权限为 public。

如下例所示，变量和方法的声明不使用任何修饰符。




```java
String version = "1.5.1";
boolean processOrder() {
   return true;
}
```


### 2）私有访问修饰符 private

私有访问修饰符是最严格的访问级别，所以被声明为 **private** 的方法、变量和构造方法只能被所属类访问，并且类和接口不能声明为
**private** 。

声明为私有访问类型的变量只能通过类中公共的 getter 方法被外部类访问。

private 访问修饰符的使用主要用来隐藏类的实现细节和保护类的数据。

下面的类使用了私有访问修饰符：




```java
public class Logger {
   private String format;
   public String getFormat() {
      return this.format;
   }
   public void setFormat(String format) {
      this.format = format;
   }
}
```


范例中，Logger 类中的 format 变量为私有变量，所以其他类不能直接得到和设置该变量的值。为了使其他类能够操作该变量，定义了两个 public
方法：getFormat() （返回 format的值）和 setFormat(String)（设置 format 的值）

### 3）公有访问修饰符 public

被声明为 public 的类、方法、构造方法和接口能够被任何其他类访问。

如果几个相互访问的 public 类分布在不同的包中，则需要导入相应 public 类所在的包。由于类的继承性，类所有的公有方法和变量都能被其子类继承。

以下函数使用了公有访问控制：




```java
public static void main(String[] arguments) {

}
```


Java 程序的 main() 方法必须设置成公有的，否则，Java 解释器将不能运行该类。

### 4）受保护的访问修饰符 protected

protected 需要从以下两个点来分析说明：

  * **子类与基类在同一包中** ：被声明为 protected 的变量、方法和构造器能被同一个包中的任何其他类访问；
  * **子类与基类不在同一包中** ：那么在子类中，子类范例可以访问其从基类继承而来的 protected 方法，而不能访问基类范例的protected方法。

protected 可以修饰数据成员，构造方法，方法成员， **不能修饰类（内部类除外）** 。

接口及接口的成员变量和成员方法不能声明为 protected。

子类能访问 protected 修饰符声明的方法和变量，这样就能保护不相关的类使用这些方法和变量。

下面的父类使用了 protected 访问修饰符，子类重写了父类的 openSpeaker() 方法。




```java
class AudioPlayer {
   protected boolean openSpeaker(Speaker sp) {
      // 实现细节
   }
}
 
class StreamingAudioPlayer extends AudioPlayer {
   protected boolean openSpeaker(Speaker sp) {
      // 实现细节
   }
}
```


如果把 openSpeaker() 方法声明为 private，那么除了 AudioPlayer 之外的类将不能访问该方法。

如果把 openSpeaker() 声明为 public，那么所有的类都能够访问该方法。

如果我们只想让该方法对其所在类的子类可见，则将该方法声明为 protected。

### 5\. 访问控制和继承

请注意以下方法继承的规则：

  * 父类中声明为 public 的方法在子类中也必须为 public。
  * 父类中声明为 protected 的方法在子类中要么声明为 protected，要么声明为 public，不能声明为 private。
  * 父类中声明为 private 的方法，不能够被继承。



## 6\. 非访问修饰符

为了实现一些其他的功能，Java 也提供了许多非访问修饰符。

static 修饰符，用来修饰类方法和类变量。

final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。

abstract 修饰符，用来创建抽象类和抽象方法。

synchronized 和 volatile 修饰符，主要用于线程的编程。

### 1）static 修饰符

**static 变量：**

static 关键字用来声明独立于对象的静态变量，无论一个类范例化多少对象，它的静态变量只有一份拷贝。 静态变量也被称为类变量。局部变量不能被声明为
static 变量。

**static 方法：**

static 关键字用来声明独立于对象的静态方法。静态方法不能使用类的非静态变量。静态方法从参数列表得到数据，然后计算这些数据。

对类变量和方法的访问可以直接使用 **classname.variablename** 和 **classname.methodname** 的方式访问。

如下例所示，static修饰符用来创建类方法和类变量。




```java
public class InstanceCounter {
   private static int numInstances = 0;
   protected static int getCount() {
      return numInstances;
   }
 
   private static void addInstance() {
      numInstances++;
   }
 
   InstanceCounter() {
      InstanceCounter.addInstance();
   }
 
   public static void main(String[] arguments) {
      System.out.println("Starting with " +
      InstanceCounter.getCount() + " instances");
      for (int i = 0; i < 500; ++i){
         new InstanceCounter();
          }
      System.out.println("Created " +
      InstanceCounter.getCount() + " instances");
   }
}
```


以上范例运行编辑结果如下:




```java
Starting with 0 instances
Created 500 instances
```


### 2）final 修饰符

**final 变量：**

final 表示"最后的、最终的"含义，变量一旦赋值后，不能被重新赋值。被 final 修饰的范例变量必须显式指定初始值。

final 修饰符通常和 static 修饰符一起使用来创建类常量。




```java
public class Test{
  final int value = 10;
  // 下面是声明常量的范例
  public static final int BOXWIDTH = 6;
  static final String TITLE = "Manager";
 
  public void changeValue(){
     value = 12; //将输出一个错误
  }
}
```


**final 方法：**

父类中的 final 方法可以被子类继承，但是不能被子类重写。

声明 final 方法的主要目的是防止该方法的内容被修改。

如下所示，使用 final 修饰符声明方法。




```java
public class Test{
    public final void changeName(){
       // 方法体
    }
}
```


**final 类：**

final 类不能被继承，没有类能够继承 final 类的任何特性。




```java
public final class Test {
   // 类体
}
```


### 3）abstract 修饰符

**abstract 类：**

抽象类不能用来范例化对象，声明抽象类的唯一目的是为了将来对该类进行扩充。

一个类不能同时被 abstract 和 final 修饰。如果一个类包含抽象方法，那么该类一定要声明为抽象类，否则将出现编译错误。

抽象类可以包含抽象方法和非抽象方法。




```java
abstract class Caravan{
   private double price;
   private String model;
   private String year;
   public abstract void goFast(); //抽象方法
   public abstract void changeColor();
}
```


**abstract 方法：**

抽象方法是一种没有任何实现的方法，该方法的的具体实现由子类提供。

抽象方法不能被声明成 final 和 static。

任何继承抽象类的子类必须实现父类的所有抽象方法，除非该子类也是抽象类。

如果一个类包含若干个抽象方法，那么该类必须声明为抽象类。抽象类可以不包含抽象方法。

抽象方法的声明以分号结尾，例如： **public abstract sample();** 。




```java
public abstract class SuperClass{
    abstract void m(); //抽象方法
}
 
class SubClass extends SuperClass{
     //实现抽象方法
      void m(){
      }
}
```


### 4）synchronized 修饰符

synchronized 关键字声明的方法同一时间只能被一个线程访问。synchronized 修饰符可以应用于四个访问修饰符。




```java
public synchronized void showDetails(){

}
```


### 5）transient 修饰符

序列化的对象包含被 transient 修饰的范例变量时，java 虚拟机(JVM)跳过该特定的变量。

该修饰符包含在定义变量的语句中，用来预处理类和变量的数据类型。




```java
public transient int limit = 55;   // 不会持久化
public int b; // 持久化
```


### 6）volatile 修饰符

volatile
修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。

一个 volatile 对象引用可能是 null。




```java
public class MyRunnable implements Runnable
{
    private volatile boolean active;
    public void run()
    {
        active = true;
        while (active) // 第一行
        {
            // 代码
        }
    }
    public void stop()
    {
        active = false; // 第二行
    }
}
```


通常情况下，在一个线程调用 run() 方法（在 Runnable 开启的线程），在另一个线程调用 stop() 方法。 如果 **_第一行_**
中缓冲区的 active 值被使用，那么在 **_第二行_** 的 active 值为 false 时循环不会停止。

但是以上代码中我们使用了 volatile 修饰 active，所以该循环会停止。







# Java 数据类型

Java 语言提供了四大分类，共八种基本数据类型。包括：六种数字类型（四个整数型，两个浮点型），一种字符类型，还有一种布尔型。

1、 **整型** ：byte 、short 、int 、long。

2、 **浮点型** ：float 、 double。

3、 **字符型** ：char。

4、 **布尔型** ：boolean。





## 1\. Java 数据类型介绍

### 1）byte 类型

  * byte 数据类型是8位、有符号的，以二进制补码表示的整数；
  * 最小值是 -128（-2^7）；
  * 最大值是 127（2^7-1）；
  * 默认值是 0；
  * byte 类型用在大型数组中节约空间，主要代替整数，因为 byte 变量占用的空间只有 int 类型的四分之一；
  * 例子：byte a = 100，byte b = -50。

### 2）short 类型

  * short 数据类型是 16 位、有符号的以二进制补码表示的整数
  * 最小值是 -32768（-2^15）；
  * 最大值是 32767（2^15 - 1）；
  * Short 数据类型也可以像 byte 那样节省空间。一个short变量是int型变量所占空间的二分之一；
  * 默认值是 0；
  * 例子：short s = 1000，short r = -20000。

### 3）int 类型

  * int 数据类型是32位、有符号的以二进制补码表示的整数；
  * 最小值是 -2,147,483,648（-2^31）；
  * 最大值是 2,147,483,647（2^31 - 1）；
  * 一般地整型变量默认为 int 类型；
  * 默认值是 0 ；
  * 例子：int a = 100000, int b = -200000。

### 4）long 类型

  * long 数据类型是 64 位、有符号的以二进制补码表示的整数；
  * 最小值是 -9,223,372,036,854,775,808（-2^63）；
  * 最大值是 9,223,372,036,854,775,807（2^63 -1）；
  * 这种类型主要使用在需要比较大整数的系统上；
  * 默认值是 0L；
  * 例子： long a = 100000L，Long b = -200000L。  
    "L"理论上不分大小写，但是若写成"l"容易与数字"1"混淆，不容易分辩。所以最好大写。

### 5）float 类型

  * float 数据类型是单精度、32位、符合IEEE 754标准的浮点数；
  * float 在储存大型浮点数组的时候可节省内存空间；
  * 默认值是 0.0f；
  * 浮点数不能用来表示精确的值，如货币；
  * 例子：float f1 = 234.5f。

### 6）double 类型

  * double 数据类型是双精度、64 位、符合 IEEE 754 标准的浮点数；

  * 浮点数的默认类型为 double 类型；

  * double类型同样不能表示精确的值，如货币；

  * 默认值是 0.0d；

  * 例子：  


```java
  double   d1  = 7D ;
double   d2  = 7.; 
double   d3  =  8.0; 
double   d4  =  8.D; 
double   d5  =  12.9867; 
```

7 是一个 int 字面量，而 7D，7. 和 8.0 是 double 字面量。

### 7）boolean 类型

  * boolean数据类型表示一位的信息；
  * 只有两个取值：true 和 false；
  * 这种类型只作为一种标志来记录 true/false 情况；
  * 默认值是 false；
  * 例子：boolean one = true。

### 8）char 类型

  * char 类型是一个单一的 16 位 Unicode 字符；
  * 最小值是 \u0000（十进制等效值为 0）；
  * 最大值是 \uffff（即为 65535）；
  * char 数据类型可以储存任何字符；
  * 例子：char letter = 'A'。



## 2\. Java 数据类型范例

对于数值类型的基本类型的取值范围，我们无需强制去记忆，因为它们的值都已经以常量的形式定义在对应的包装类中了。请看下面的例子：




```java
public class PrimitiveTypeTest {  
    public static void main(String[] args) {  
        // byte  
        System.out.println("基本类型：byte 二进制位数：" + Byte.SIZE);  
        System.out.println("包装类：java.lang.Byte");  
        System.out.println("最小值：Byte.MIN_VALUE=" + Byte.MIN_VALUE);  
        System.out.println("最大值：Byte.MAX_VALUE=" + Byte.MAX_VALUE);  
        System.out.println();  
  
        // short  
        System.out.println("基本类型：short 二进制位数：" + Short.SIZE);  
        System.out.println("包装类：java.lang.Short");  
        System.out.println("最小值：Short.MIN_VALUE=" + Short.MIN_VALUE);  
        System.out.println("最大值：Short.MAX_VALUE=" + Short.MAX_VALUE);  
        System.out.println();  
  
        // int  
        System.out.println("基本类型：int 二进制位数：" + Integer.SIZE);  
        System.out.println("包装类：java.lang.Integer");  
        System.out.println("最小值：Integer.MIN_VALUE=" + Integer.MIN_VALUE);  
        System.out.println("最大值：Integer.MAX_VALUE=" + Integer.MAX_VALUE);  
        System.out.println();  
  
        // long  
        System.out.println("基本类型：long 二进制位数：" + Long.SIZE);  
        System.out.println("包装类：java.lang.Long");  
        System.out.println("最小值：Long.MIN_VALUE=" + Long.MIN_VALUE);  
        System.out.println("最大值：Long.MAX_VALUE=" + Long.MAX_VALUE);  
        System.out.println();  
  
        // float  
        System.out.println("基本类型：float 二进制位数：" + Float.SIZE);  
        System.out.println("包装类：java.lang.Float");  
        System.out.println("最小值：Float.MIN_VALUE=" + Float.MIN_VALUE);  
        System.out.println("最大值：Float.MAX_VALUE=" + Float.MAX_VALUE);  
        System.out.println();  
  
        // double  
        System.out.println("基本类型：double 二进制位数：" + Double.SIZE);  
        System.out.println("包装类：java.lang.Double");  
        System.out.println("最小值：Double.MIN_VALUE=" + Double.MIN_VALUE);  
        System.out.println("最大值：Double.MAX_VALUE=" + Double.MAX_VALUE);  
        System.out.println();  
  
        // char  
        System.out.println("基本类型：char 二进制位数：" + Character.SIZE);  
        System.out.println("包装类：java.lang.Character");  
        // 以数值形式而不是字符形式将Character.MIN_VALUE输出到控制台  
        System.out.println("最小值：Character.MIN_VALUE="  
                + (int) Character.MIN_VALUE);  
        // 以数值形式而不是字符形式将Character.MAX_VALUE输出到控制台  
        System.out.println("最大值：Character.MAX_VALUE="  
                + (int) Character.MAX_VALUE);  
    }  
}
```


编译以上代码输出结果如下所示：




```java
基本类型：byte 二进制位数：8
包装类：java.lang.Byte
最小值：Byte.MIN_VALUE=-128
最大值：Byte.MAX_VALUE=127

基本类型：short 二进制位数：16
包装类：java.lang.Short
最小值：Short.MIN_VALUE=-32768
最大值：Short.MAX_VALUE=32767

基本类型：int 二进制位数：32
包装类：java.lang.Integer
最小值：Integer.MIN_VALUE=-2147483648
最大值：Integer.MAX_VALUE=2147483647

基本类型：long 二进制位数：64
包装类：java.lang.Long
最小值：Long.MIN_VALUE=-9223372036854775808
最大值：Long.MAX_VALUE=9223372036854775807

基本类型：float 二进制位数：32
包装类：java.lang.Float
最小值：Float.MIN_VALUE=1.4E-45
最大值：Float.MAX_VALUE=3.4028235E38

基本类型：double 二进制位数：64
包装类：java.lang.Double
最小值：Double.MIN_VALUE=4.9E-324
最大值：Double.MAX_VALUE=1.7976931348623157E308

基本类型：char 二进制位数：16
包装类：java.lang.Character
最小值：Character.MIN_VALUE=0
最大值：Character.MAX_VALUE=65535
```


Float和Double的最小值和最大值都是以科学记数法的形式输出的，结尾的"E+数字"表示E之前的数字要乘以10的多少次方。比如3.14E3就是3.14
× 103 =3140，3.14E-3 就是 3.14 x 10-3 =0.00314。

实际上，JAVA中还存在另外一种基本类型 void，它也有对应的包装类 java.lang.Void，不过我们无法直接对它们进行操作。



## 3\. Java 数据类型转换

##

### 1）自动数据类型转换

**整型、实型（常量）、字符型数据可以混合运算。运算中，不同类型的数据先转化为同一类型，然后进行运算。**

转换从低级到高级。




```java
低  ------------------------------------>  高

byte,short,char—> int —> long—> float —> double 
```


数据类型转换必须满足如下规则：

  * 1\. 不能对boolean类型进行类型转换。

  * 2\. 不能把对象类型转换成不相关类的对象。

  * 3\. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。

  * 4\. 转换过程中可能导致溢出或损失精度，例如：  


```java
  int i = 128;   
byte b = (byte)i;
```

因为 byte 类型是 8 位，最大值为127，所以当 int 强制转换为 byte 类型时，值 128 时候就会导致溢出。

  * 5\. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入，例如：   


```java
  (int)23.7 == 23;        
(int)-45.89f == -45
```

### 2）强制数据类型转换

  * 1\. 条件是转换的数据类型必须是兼容的。

  * 2\. 格式：(type)value，其中 type 是要强制类型转换后的数据类型。  


```java
  public class QiangZhiZhuanHuan{
  public static void main(String[] args){
      int i1 = 123;
      byte b = (byte)i1;//强制类型转换为byte
      System.out.println("int强制类型转换为byte后的值等于"+b);
  }
}
```

运行结果：


```java
    int强制类型转换为byte后的值等于123
```


### 3）隐含强制类型转换

  * 1\. 整数的默认类型是 int。
  * 2\. 浮点型不存在这种情况，因为在定义 float 类型时必须在数字后面跟上 F 或者 f。




# Java 数据结构

Java工具包提供了强大的数据结构。在Java中的数据结构主要包括以下几种接口和类：

  * 枚举（Enumeration）
  * 位集合（BitSet）
  * 向量（Vector）
  * 栈（Stack）
  * 字典（Dictionary）
  * 哈希表（Hashtable）
  * 属性（Properties）

以上这些类是传统遗留的，在Java2中引入了一种新的框架-集合框架(Collection)，我们后面再讨论。



## 1\. 枚举（Enumeration）

枚举（Enumeration）接口虽然它本身不属于数据结构,但它在其他数据结构的范畴里应用很广。 枚举（The
Enumeration）接口定义了一种从数据结构中取回连续元素的方式。

例如，枚举定义了一个叫nextElement 的方法，该方法用来得到一个包含多元素的数据结构的下一个元素。



## 2\. 位集合（BitSet）

位集合类实现了一组可以单独设置和清除的位或标志。

该类在处理一组布尔值的时候非常有用，你只需要给每个值赋值一"位"，然后对位进行适当的设置或清除，就可以对布尔值进行操作了。



## 3\. 向量（Vector）

向量（Vector）类和传统数组非常相似，但是Vector的大小能根据需要动态的变化。

和数组一样，Vector对象的元素也能通过索引访问。

使用Vector类最主要的好处就是在创建对象的时候不必给对象指定大小，它的大小会根据需要动态的变化。



## 4\. 栈（Stack）

栈（Stack）实现了一个后进先出（LIFO）的数据结构。

你可以把栈理解为对象的垂直分布的栈，当你添加一个新元素时，就将新元素放在其他元素的顶部。

当你从栈中取元素的时候，就从栈顶取一个元素。换句话说，最后进栈的元素最先被取出。



## 5\. 字典（Dictionary）

字典（Dictionary） 类是一个抽象类，它定义了键映射到值的数据结构。

当你想要通过特定的键而不是整数索引来访问数据的时候，这时候应该使用Dictionary。

由于Dictionary类是抽象类，所以它只提供了键映射到值的数据结构，而没有提供特定的实现。



## 6\. 哈希表（Hashtable）

Hashtable类提供了一种在用户定义键结构的基础上来组织数据的手段。

例如，在地址列表的哈希表中，你可以根据邮政编码作为键来存储和排序数据，而不是通过人名。

哈希表键的具体含义完全取决于哈希表的使用情景和它包含的数据。



## 7\. 属性（Properties）

Properties 继承于 Hashtable.Properties 类表示了一个持久的属性集.属性列表中每个键及其对应值都是一个字符串。

Properties 类被许多Java类使用。例如，在获取环境变量时它就作为System.getProperties()方法的返回值。






# Java 数组

Java 语言中提供的数组是用来存储固定大小的同类型元素。



## 1\. 声明数组变量

首先必须声明数组变量，才能在程序中使用数组。

### 1）声明数组变量的语法




```java
dataType[] arrayRefVar;   // 首选的方法
或
dataType arrayRefVar[];  // 效果相同，但不是首选方法
```


**注意:** 建议使用 **dataType[] arrayRefVar** 的声明风格声明数组变量。 dataType arrayRefVar[]
风格是来自 C/C++ 语言 ，在Java中采用是为了让 C/C++ 程序员能够快速理解java语言。

### 2）声明数组变量的范例




```java
double[] myList;         // 首选的方法
或
double myList[];         //  效果相同，但不是首选方法
```




## 2\. 创建数组

Java语言使用new操作符来创建数组。

### 1）创建数组变量的语法




```java
arrayRefVar = new dataType[arraySize];
```


上面的语法语句做了两件事：

  * 一、使用 dataType[arraySize] 创建了一个数组。
  * 二、把新创建的数组的引用赋值给变量 arrayRefVar。

数组变量的声明，和创建数组可以用一条语句完成，如下所示：




```java
dataType[] arrayRefVar = new dataType[arraySize];
```


另外，你还可以使用如下的方式创建数组。




```java
dataType[] arrayRefVar = {value0, value1, ..., valuek};
```


数组的元素是通过索引访问的。数组索引从 0 开始，所以索引值从 0 到 arrayRefVar.length-1。

### 2）创建数组变量的范例

下面的语句首先声明了一个数组变量 myList，接着创建了一个包含 10 个 double 类型元素的数组，并且把它的引用赋值给 myList 变量。




```java
public class TestArray {
   public static void main(String[] args) {
      // 数组大小
      int size = 10;
      // 定义数组
      double[] myList = new double[size];
      myList[0] = 5.6;
      myList[1] = 4.5;
      myList[2] = 3.3;
      myList[3] = 13.2;
      myList[4] = 4.0;
      myList[5] = 34.33;
      myList[6] = 34.0;
      myList[7] = 45.45;
      myList[8] = 99.993;
      myList[9] = 11123;
      // 计算所有元素的总和
      double total = 0;
      for (int i = 0; i < size; i++) {
         total += myList[i];
      }
      System.out.println("总和为： " + total);
   }
}
```


以上范例输出结果为：




```java
总和为： 11367.373
```


下面的图片描绘了数组 myList。这里 myList 数组里有 10 个 double 元素，它的下标从 0 到 9。

![java数组结构说明](http://static.codebaoku.com/pics/53/42/53422d35ed89b1caed74213ee2568950.jpg)



## 3\. 操作数组

数组的元素类型和数组的大小都是确定的，所以当处理数组元素时候，我们通常使用基本循环或者 For-Each 循环。

该范例完整地展示了如何创建、初始化和操纵数组：




```java
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (int i = 0; i < myList.length; i++) {
         System.out.println(myList[i] + " ");
      }
      // 计算所有元素的总和
      double total = 0;
      for (int i = 0; i < myList.length; i++) {
         total += myList[i];
      }
      System.out.println("Total is " + total);
      // 查找最大元素
      double max = myList[0];
      for (int i = 1; i < myList.length; i++) {
         if (myList[i] > max) max = myList[i];
      }
      System.out.println("Max is " + max);
   }
}
```


以上范例编译运行结果如下：




```java
1.9
2.9
3.4
3.5
Total is 11.7
Max is 3.5
```




## 4\. For-Each 循环

JDK 1.5 引进了一种新的循环类型，被称为 For-Each 循环或者加强型循环，它能在不使用下标的情况下遍历数组。

语法格式如下：




```java
for(type element: array)
{
    System.out.println(element);
}
```

该范例用来显示数组 myList 中的所有元素：




```java
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (double element: myList) {
         System.out.println(element);
      }
   }
}
```


以上范例编译运行结果如下：




```java
1.9
2.9
3.4
3.5
```




## 5\. 数组作为函数的参数

数组可以作为参数传递给方法。

例如，下面的例子就是一个打印 int 数组中元素的方法:




```java
public static void printArray(int[] array) {
  for (int i = 0; i < array.length; i++) {
    System.out.print(array[i] + " ");
  }
}
```


下面例子调用 printArray 方法打印出 3，1，2，6，4 和 2：




```java
printArray(new int[]{3, 1, 2, 6, 4, 2});
```




## 6\. 数组作为函数的返回值




```java
public static int[] reverse(int[] list) {
  int[] result = new int[list.length];
 
  for (int i = 0, j = result.length - 1; i < list.length; i++, j--) {
    result[j] = list[i];
  }
  return result;
}
```


以上范例中 result 数组作为函数的返回值。



## 7\. 多维数组

多维数组可以看成是数组的数组，比如二维数组就是一个特殊的一维数组，其每一个元素都是一个一维数组，例如：




```java
String str[][] = new String[3][4];
```


### 多维数组的动态初始化（以二维数组为例）

1\. 直接为每一维分配空间，格式如下：




```java
type[][] typeName = new type[typeLength1][typeLength2];
```


type 可以为基本数据类型和复合数据类型，typeLength1 和 typeLength2 必须为正整数，typeLength1
为行数，typeLength2 为列数。

例如：




```java
int a[][] = new int[2][3];
```


解析：

二维数组 a 可以看成一个两行三列的数组。

2\. 从最高维开始，分别为每一维分配空间，例如：




```java
String s[][] = new String[2][];
s[0] = new String[2];
s[1] = new String[3];
s[0][0] = new String("Good");
s[0][1] = new String("Luck");
s[1][0] = new String("to");
s[1][1] = new String("you");
s[1][2] = new String("!");
```


解析：

**s[0]=new String[2]** 和 **s[1]=new String[3]**
是为最高维分配引用空间，也就是为最高维限制其能保存数据的最长的长度，然后再为其每个数组元素单独分配空间 **s0=new String("Good")**
等操作。

### 多维数组的引用（以二维数组为例）

对二维数组中的每个元素，引用方式为 arrayName [index1][index2]，例如：




```java
num[1][0];
```




## 8\. Arrays 类

java.util.Arrays 类能方便地操作数组，它提供的所有方法都是静态的。

具有以下功能：

  * 给数组赋值：通过 fill 方法。
  * 对数组排序：通过 sort 方法,按升序。
  * 比较数组：通过 equals 方法比较数组中元素值是否相等。
  * 查找数组元素：通过 binarySearch 方法能对排序好的数组进行二分查找法操作。

具体说明请查看下表：

| 序号                                                         | 方法和说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| 1                                                            | **public static int binarySearch(Object[] a, Object key)** |
| 用二分查找算法在给定数组中搜索给定值的对象(Byte,Int,double等)。数组在调用前必须排序好的。如果查找值包含在数组中，则返回搜索键的索引；否则返回 |                                                            |
| (-( _插入点_ ) - 1)。                                        |                                                            |
| 2                                                            | **public static boolean equals(long[] a, long[] a2)**      |
| 如果两个指定的 long 型数组彼此 _相等_ ，则返回               |                                                            |
| true。如果两个数组包含相同数量的元素，并且两个数组中的所有相应元素对都是相等的，则认为这两个数组是相等的。换句话说，如果两个数组以相同顺序包含相同的元素，则两个数组是相等的。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |                                                            |
| 3                                                            | **public static void fill(int[] a, int val)**              |
| 将指定的 int 值分配给指定 int 型数组指定范围中的每个元素。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |                                                            |
| 4                                                            | **public static void sort(Object[] a)**                    |
| 对指定对象数组根据其元素的自然顺序进行升序排列。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。 |                                                            |








# Java 运算符

计算机的最基本用途之一就是执行数学运算，作为一门计算机语言，Java也提供了一套丰富的运算符来操纵变量。我们可以把运算符分成以下几组：

  * 算术运算符
  * 关系运算符
  * 位运算符
  * 逻辑运算符
  * 赋值运算符
  * 其他运算符

## 算术运算符

算术运算符用在数学表达式中，它们的作用和在数学中的作用一样。下表列出了所有的算术运算符。

表格中的实例假设整数变量A的值为10，变量B的值为20：

| 操作符 | 描述 | 例子 |
| ------ | ---- | ---- |

+ |  加法 - 相加运算符两侧的值 |  A + B 等于 30  

- |  减法 - 左操作数减去右操作数 |  A – B 等于 -10  

* |  乘法 - 相乘操作符两侧的值 |  A * B等于200  
  / |  除法 - 左操作数除以右操作数 |  B / A等于2  
  ％ |  取余 - 左操作数除以右操作数的余数 |  B%A等于0  
  ++ |  自增: 操作数的值增加1 |  B++ 或 ++B 等于 21（区别详见下文）  
  \-- |  自减: 操作数的值减少1 |  B-- 或 --B 等于 19（区别详见下文）  解析：

  * int b = ++a; 拆分运算过程为: a=a+1=4; b=a=4, 最后结果为b=4,a=4

  * int d = --c; 拆分运算过程为: c=c-1=2; d=c=2, 最后结果为d=2,c=2

**2、前缀自增自减法(++a,--a):** 先进行自增或者自减运算，再进行表达式运算。

**3、后缀自增自减法(a++,a--):** 先进行表达式运算，再进行自增或者自减运算 实例：



## instanceof 运算符

该运算符用于操作对象实例，检查该对象是否是一个特定类型（类类型或接口类型）。

instanceof运算符使用格式如下：



 ```java
 ( Object reference variable ) instanceof (class/interface type)
 ```





如果运算符左侧变量所指的对象，是操作符右侧类或接口(class/interface)的一个对象，那么结果为真。







# Java 集合框架

Java 提供了一些特定类，用来存储和操作对象组，比如：Dictionary, Vector, Stack, 和 Properties。

这些类各有各的实现，没有统一的访问和操作方式，所以使用 Vector 类的方式和使用 Properties 类的方式有着很大不同

集合框架被设计成要满足以下几个目标：

  * 该框架必须是高性能的。基本集合（动态数组，链表，树，哈希表）的实现也必须是高效的。
  * 该框架允许不同类型的集合，以类似的方式工作，具有高度的互操作性。
  * 对一个集合的扩展和适应必须是简单的。

为此，整个集合框架就围绕一组标准接口而设计。你可以直接使用这些接口的标准实现，诸如： **LinkedList** , **HashSet** , 和
**TreeSet** 等,除此之外你也可以通过这些接口实现自己的集合。

从上面的集合框架图可以看到，Java
集合框架主要包括两种类型的容器，一种是集合（Collection），存储一个元素集合，另一种是图（Map），存储键/值对映射。Collection 接口又有
3 种子类型，List、Set 和 Queue，再下面是一些抽象类，最后是具体实现类，常用的有
[ArrayList](http://www.0.com/java/java-
arraylist.html)、[LinkedList](http://www.0.com/java/java-
linkedlist.html)、[HashSet](http://www.0.com/java/java-
hashset.html)、LinkedHashSet、[HashMap](http://www.0.com/java/java-
hashmap.html)、LinkedHashMap 等等。

集合框架是一个用来代表和操纵集合的统一架构。所有的集合框架都包含如下内容：

  * **接口：** 是代表集合的抽象数据类型。例如 Collection、List、Set、Map 等。之所以定义多个接口，是为了以不同的方式操作集合对象
  * **实现（类）：** 是集合接口的具体实现。从本质上讲，它们是可重复使用的数据结构，例如：ArrayList、LinkedList、HashSet、HashMap。
  * **算法：** 是实现集合接口的对象里的方法执行的一些有用的计算，例如：搜索和排序。这些算法被称为多态，那是因为相同的方法可以在相似的接口上有着不同的实现。

除了集合，该框架也定义了几个 Map 接口和类。Map 里存储的是键/值对。尽管 Map 不是集合，但是它们完全整合在集合中。



## 1\. 集合框架体系

Java 集合框架提供了一套性能优良，使用方便的接口和类，java集合框架位于java.util包中， 所以当使用集合框架的时候需要进行导包。



## 2\. 集合接口

集合框架定义了一些接口。本节提供了每个接口的概述：

| 序号 | 接口描述        |
| ---- | --------------- |
| 1    | Collection 接口 |

Collection 是最基本的集合接口，一个 Collection 代表一组 Object，即 Collection 的元素,
Java不提供直接继承自Collection的类，只提供继承于的子接口(如List和set)。

Collection 接口存储一组不唯一，无序的对象。  

2 |  List 接口  

List接口是一个有序的
Collection，使用此接口能够精确的控制每个元素插入的位置，能够通过索引(元素在List中位置，类似于数组的下标)来访问List中的元素，第一个元素的索引为
0，而且允许有相同的元素。

List 接口存储一组不唯一，有序（插入顺序）的对象。  

3 |  Set  

Set 具有与 Collection 完全一样的接口，只是行为上不同，Set 不保存重复的元素。

Set 接口存储一组唯一，无序的对象。  

4 |  SortedSet  
继承于Set保存有序的集合。  
5 |  Map  

Map 接口存储一组键值对象，提供key（键）到value（值）的映射。  

6 |  Map.Entry  
描述在一个Map中的一个元素（键/值对）。是一个 Map 的内部接口。  
7 |  SortedMap  
继承于 Map，使 Key 保持在升序排列。  
8 |  Enumeration  
这是一个传统的接口和定义的方法，通过它可以枚举（一次获得一个）对象集合中的元素。这个传统接口已被迭代器取代。  



## 3\. Set 和 List 区别

  * 1\. Set 接口范例存储的是无序的，不重复的数据。List 接口范例存储的是有序的，可以重复的元素。
  * 2\. Set检索效率低下，删除和插入效率高，插入和删除不会引起元素位置改变 **< 实现类有HashSet,TreeSet>**。
  * 3\. List和数组类似，可以动态增长，根据实际存储的数据的长度自动增长List的长度。查找元素效率高，插入删除效率低，因为会引起其他元素位置改变 **< 实现类有ArrayList,LinkedList,Vector>** 。



## 4\. 集合实现类（集合类）

Java提供了一套实现了Collection接口的标准集合类。其中一些是具体类，这些类可以直接拿来使用，而另外一些是抽象类，提供了接口的部分实现。

标准集合类汇总于下表：

| 序号                                                         | 类描述                       |
| ------------------------------------------------------------ | ---------------------------- |
| 1                                                            | **AbstractCollection  **     |
| 实现了大部分的集合接口。                                     |                              |
| 2                                                            | **AbstractList  **           |
| 继承于AbstractCollection 并且实现了大部分List接口。          |                              |
| 3                                                            | **AbstractSequentialList  ** |
| 继承于 AbstractList ，提供了对数据元素的链式访问而不是随机访问。 |                              |
| 4                                                            | LinkedList                   |

该类实现了List接口，允许有null（空）元素。主要用于创建链表数据结构，该类没有同步方法，如果多个线程同时访问一个List，则必须自己实现访问同步，解决方法就是在创建List时候构造一个同步的List。例如：




```java
List list=Collections.synchronizedList(newLinkedList(...));
```


LinkedList 查找效率低。  

5 | ArrayList  

该类也是实现了List的接口，实现了可变大小的数组，随机访问和遍历元素时，提供更好的性能。该类也是非同步的,在多线程的情况下不要使用。ArrayList
增长当前长度的50%，插入删除效率低。  

6 | **AbstractSet  **  
继承于AbstractCollection 并且实现了大部分Set接口。  
7 | HashSet  

该类实现了Set接口，不允许出现重复元素，不保证集合中元素的顺序，允许包含值为null的元素，但最多只能一个。  

8 | LinkedHashSet  
具有可预知迭代顺序的 `Set` 接口的哈希表和链接列表实现。  
9 | TreeSet  

该类实现了Set接口，可以实现排序等功能。  

10 | **AbstractMap  **  
实现了大部分的Map接口。  
11 | HashMap  
HashMap 是一个散列表，它存储的内容是键值对(key-value)映射。  
该类实现了Map接口，根据键的HashCode值存储数据，具有很快的访问速度，最多允许一条记录的键为null，不支持线程同步。  
12 | TreeMap  
继承了AbstractMap，并且使用一颗树。  
13 | WeakHashMap  
继承AbstractMap类，使用弱密钥的哈希表。  
14 | LinkedHashMap  
继承于HashMap，使用元素的自然顺序对元素进行排序.  
15 | IdentityHashMap  
继承AbstractMap类，比较文档时使用引用相等。  

在前面的教程中已经讨论通过java.util包中定义的类，如下所示：

| 序号 | 类描述 |
| ---- | ------ |
| 1    | Vector |

该类和ArrayList非常相似，但是该类是同步的，可以用在多线程的情况，该类允许设置默认的增长长度，默认扩容方式为原来的2倍。  

2 | Stack  
栈是Vector的一个子类，它实现了一个标准的后进先出的栈。  
3 | Dictionary  
Dictionary 类是一个抽象类，用来存储键/值对，作用和Map类相似。  
4 | Hashtable  

Hashtable 是 Dictionary(字典) 类的子类，位于 java.util 包中。  

5 | Properties  
Properties 继承于 Hashtable，表示一个持久的属性集，属性列表中每个键及其对应值都是一个字符串。  
6 | BitSet  
一个Bitset类创建一种特殊类型的数组来保存位值。BitSet中数组大小会随需要增加。  



## 5\. 集合算法

集合框架定义了几种算法，可用于集合和映射。这些算法被定义为集合类的静态方法。

在尝试比较不兼容的类型时，一些方法能够抛出
ClassCastException异常。当试图修改一个不可修改的集合时，抛出UnsupportedOperationException异常。

集合定义三个静态的变量：EMPTY_SET，EMPTY_LIST，EMPTY_MAP的。这些变量都不可改变。

| 序号                             | 算法描述              |
| -------------------------------- | --------------------- |
| 1                                | Collection Algorithms |
| 这里是一个列表中的所有算法实现。 |                       |





## 6\. 如何使用迭代器

通常情况下，你会希望遍历一个集合中的元素。例如，显示集合中的每个元素。

一般遍历数组都是采用for循环或者增强for，这两个方法也可以用在集合框架，但是还有一种方法是采用迭代器遍历集合框架，它是一个对象，实现了Iterator
接口或 ListIterator接口。

迭代器，使你能够通过循环来得到或删除集合的元素。ListIterator 继承了 Iterator，以允许双向遍历列表和修改元素。

| 序号                                                         | 迭代器方法描述     |
| ------------------------------------------------------------ | ------------------ |
| 1                                                            | 使用 Java Iterator |
| 这里通过范例列出 Iterator 和 ListIterator 接口提供的所有方法。 |                    |



## 7\. 遍历 ArrayList




```java
import java.util.*;

public class Test{
    public static void main(String[] args) {
        List<String> list=new ArrayList<String>();
        list.add("Hello");
        list.add("World");
        list.add("HAHAHAHA");
        //第一种遍历方法使用 For-Each 遍历 List
        for (String str : list) {            
            //也可以改写 for(int i=0;i<list.size();i++) 这种形式
            System.out.println(str);
        }
    
        //第二种遍历，把链表变为数组相关的内容进行遍历
        String[] strArray=new String[list.size()];
        list.toArray(strArray);
        for(int i=0;i<strArray.length;i++) //这里也可以改写为  for(String str:strArray) 这种形式
        {
        System.out.println(strArray[i]);
        }
        
    //第三种遍历 使用迭代器进行相关遍历
        
        Iterator<String> ite=list.iterator();
        while(ite.hasNext())//判断下一个元素之后有值
        {
            System.out.println(ite.next());
        }
    }
}
```


**解析：**

三种方法都是用来遍历ArrayList集合，第三种方法是采用迭代器的方法，该方法可以不用担心在遍历的过程中会超出集合的长度。



## 8\. 遍历 Map




```java
import java.util.*;

public class Test{
    public static void main(String[] args) {
        Map map = new HashMap();
        map.put("1", "value1");
        map.put("2", "value2");
        map.put("3", "value3");
        
        //第一种：普遍使用，二次取值
        System.out.println("通过Map.keySet遍历key和value：");
        for (String key : map.keySet()) {
            System.out.println("key= "+ key + " and value= " + map.get(key));
        }
        
        //第二种
        System.out.println("通过Map.entrySet使用iterator遍历key和value：");
        Iterator<Map.Entry<String, String>> it = map.entrySet().iterator();
        while (it.hasNext()) {
        Map.Entry<String, String> entry = it.next();
            System.out.println("key= " + entry.getKey() + " and value= " + entry.getValue());
        }
        
        //第三种：推荐，尤其是容量大时
        System.out.println("通过Map.entrySet遍历key和value");
        for (Map.Entry<String, String> entry : map.entrySet()) {
            System.out.println("key= " + entry.getKey() + " and value= " + entry.getValue());
        }

        //第四种
        System.out.println("通过Map.values()遍历所有的value，但不能遍历key");
        for (String v : map.values()) {
            System.out.println("value= " + v);
        }
    }
}
```




## 9\. 如何使用比较器

TreeSet和TreeMap的按照排序顺序来存储元素. 然而，这是通过比较器来精确定义按照什么样的排序顺序。

这个接口可以让我们以不同的方式来排序一个集合。

| 序号                                         | 比较器方法描述       |
| -------------------------------------------- | -------------------- |
| 1                                            | 使用 Java Comparator |
| 这里通过范例列出Comparator接口提供的所有方法 |                      |



## 10\. 总结

Java集合框架为程序员提供了预先包装的数据结构和算法来操纵他们。

集合是一个对象，可容纳其他对象的引用。集合接口声明对每一种类型的集合可以执行的操作。

集合框架的类和接口均在java.util包中。

任何对象加入集合类后，自动转变为Object类型，所以在取出的时候，需要进行强制类型转换。



+++

# Java 继承

继承是使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。

通过继承创建的新类称为“子类”，被继承的类称为“父类”。

Java 的继承就是子类继承父类的特征和行为，使得子类对象具有父类的范例域和方法，或子类从父类继承方法，使得子类具有父类相同的行为。



## 1\. Java 类继承的语法

在 Java 中通过 extends 关键字可以申明一个类是从另外一个类继承而来：




```java
class ParentClass {
}
 
class ChildClass extends ParentClass {
}
```




## 2\. Java 类继承的案例

我们要开发动物类，其中动物分别为企鹅以及老鼠，要求如下：

  * 企鹅：属性（姓名，id），方法（吃，睡，自我介绍）
  * 老鼠：属性（姓名，id），方法（吃，睡，自我介绍）

### 企鹅类：




```java
public class Penguin { 
    private String name; 
    private int id; 
    public Penguin(String myName, int  myid) { 
        name = myName; 
        id = myid; 
    } 
    public void eat(){ 
        System.out.println(name+"正在吃"); 
    }
    public void sleep(){
        System.out.println(name+"正在睡");
    }
    public void introduction() { 
        System.out.println("大家好！我是" + id + "号" + name + "."); 
    } 
}
```


### 老鼠类：




```java
public class Mouse { 
    private String name; 
    private int id; 
    public Mouse(String myName, int  myid) { 
        name = myName; 
        id = myid; 
    } 
    public void eat(){ 
        System.out.println(name+"正在吃"); 
    }
    public void sleep(){
        System.out.println(name+"正在睡");
    }
    public void introduction() { 
        System.out.println("大家好！我是" + id + "号" + name + "."); 
    } 
}
```


从这两段代码可以看出来，代码存在重复了，导致后果就是代码量大且臃肿，而且维护性不高(维护性主要是后期需要修改的时候，就需要修改很多的代码，容易出错)，所以要从根本上解决这两段代码的问题，就需要继承，将两段代码中相同的部分提取出来组成
一个父类：

### 公共父类：




```java
public class Animal { 
    private String name;  
    private int id; 
    public Animal(String myName, int myid) { 
        name = myName; 
        id = myid;
    } 
    public void eat(){ 
        System.out.println(name+"正在吃"); 
    }
    public void sleep(){
        System.out.println(name+"正在睡");
    }
    public void introduction() { 
        System.out.println("大家好！我是" + id + "号" + name + "."); 
    } 
}
```


这个Animal类就可以作为一个父类，然后企鹅类和老鼠类继承这个类之后，就具有父类当中的属性和方法，子类就不会存在重复的代码，维护性也提高，代码也更加简洁，提高代码的复用性（复用性主要是可以多次使用，不用再多次写同样的代码）
继承之后的代码：

### 企鹅类：




```java
public class Penguin extends Animal { 
    public Penguin(String myName, int myid) { 
        super(myName, myid); 
    } 
}
```


### 老鼠类：




```java
public class Mouse extends Animal { 
    public Mouse(String myName, int myid) { 
        super(myName, myid); 
    } 
}
```




## 3\. 继承类型

![](http://static.codebaoku.com/pics/1f/78/1f78aa4f719d9b9af7d5a2c782bbec6f.png)



## 继承的特性

  * 子类拥有父类非 private 的属性、方法。

  * 子类可以拥有自己的属性和方法，即子类可以对父类进行扩展。

  * 子类可以用自己的方式实现父类的方法。

  * Java 的继承是单继承，但是可以多重继承，单继承就是一个子类只能继承一个父类，多重继承就是，例如 B 类继承 A 类，C 类继承 B 类，所以按照关系就是 B 类是 C 类的父类，A 类是 B 类的父类，这是 Java 继承区别于 C++ 继承的一个特性。

  * 提高了类之间的耦合性（继承的缺点，耦合度高就会造成代码之间的联系越紧密，代码独立性越差）。



## 4\. 继承关键字

继承可以使用 extends 和 implements 这两个关键字来实现继承，而且所有的类都是继承于
java.lang.Object，当一个类没有继承的两个关键字，则默认继承object（这个类在 **java.lang** 包中，所以不需要
**import** ）祖先类。

### 1）extends关键字

在 Java 中，类的继承是单一继承，也就是说，一个子类只能拥有一个父类，所以 extends 只能继承一个类。




```java
public class Animal { 
    private String name;   
    private int id; 
    public Animal(String myName, String myid) { 
        //初始化属性值
    } 
    public void eat() {  //吃东西方法的具体实现  } 
    public void sleep() { //睡觉方法的具体实现  } 
} 
 
public class Penguin  extends  Animal{ 
}
```


### 2）implements关键字

使用 implements 关键字可以变相的使java具有多继承的特性，使用范围为类继承接口的情况，可以同时继承多个接口（接口跟接口之间采用逗号分隔）。




```java
public interface A {
    public void eat();
    public void sleep();
}
 
public interface B {
    public void show();
}
 
public class C implements A,B {
}
```


### 3）super 与 this 关键字

super关键字：我们可以通过super关键字来实现对父类成员的访问，用来引用当前对象的父类。

this关键字：指向自己的引用。




```java
class Animal {
  void eat() {
    System.out.println("animal : eat");
  }
}
 
class Dog extends Animal {
  void eat() {
    System.out.println("dog : eat");
  }
  void eatTest() {
    this.eat();   // this 调用自己的方法
    super.eat();  // super 调用父类方法
  }
}
 
public class Test {
  public static void main(String[] args) {
    Animal a = new Animal();
    a.eat();
    Dog d = new Dog();
    d.eatTest();
  }
}
```


输出结果为：




```java
animal : eat
dog : eat
animal : eat
```


### 4）final关键字

final 关键字声明类可以把类定义为不能继承的，即最终类；或者用于修饰方法，该方法不能被子类重写：

  * 声明类：

      final class 类名 {//类体}

  * 声明方法：

      修饰符(public/private/default/protected) final 返回值类型 方法名(){//方法体}

**注** :范例变量也可以被定义为 final，被定义为 final 的变量不能被修改。被声明为 final 类的方法自动地声明为
final，但是范例变量并不是 final



## 5\. 构造器

子类是不继承父类的构造器（构造方法或者构造函数）的，它只是调用（隐式或显式）。如果父类的构造器带有参数，则必须在子类的构造器中显式地通过 super
关键字调用父类的构造器并配以适当的参数列表。

如果父类构造器没有参数，则在子类的构造器中不需要使用 super 关键字调用父类构造器，系统会自动调用父类的无参构造器。




```java
class SuperClass {
  private int n;
  SuperClass(){
    System.out.println("SuperClass()");
  }
  SuperClass(int n) {
    System.out.println("SuperClass(int n)");
    this.n = n;
  }
}
// SubClass 类继承
class SubClass extends SuperClass{
  private int n;
  
  SubClass(){ // 自动调用父类的无参数构造器
    System.out.println("SubClass");
  }  
  
  public SubClass(int n){ 
    super(300);  // 调用父类中带有参数的构造器
    System.out.println("SubClass(int n):"+n);
    this.n = n;
  }
}
// SubClass2 类继承
class SubClass2 extends SuperClass{
  private int n;
  
  SubClass2(){
    super(300);  // 调用父类中带有参数的构造器
    System.out.println("SubClass2");
  }  
  
  public SubClass2(int n){ // 自动调用父类的无参数构造器
    System.out.println("SubClass2(int n):"+n);
    this.n = n;
  }
}
public class TestSuperSub{
  public static void main (String args[]){
    System.out.println("------SubClass 类继承------");
    SubClass sc1 = new SubClass();
    SubClass sc2 = new SubClass(100); 
    System.out.println("------SubClass2 类继承------");
    SubClass2 sc3 = new SubClass2();
    SubClass2 sc4 = new SubClass2(200); 
  }
}
```


输出结果为：




```java
------SubClass 类继承------
SuperClass()
SubClass
SuperClass(int n)
SubClass(int n):100
------SubClass2 类继承------
SuperClass(int n)
SubClass2
SuperClass()
SubClass2(int n):200
```






# Java 异常处理

异常是指程序中的一些错误，但并不是所有的错误都是异常。在程序设计中，进行异常处理是非常关键和重要的一部分。Java提供了try、catch、finally这三个关键字来处理异常。



## 1\. 异常发生的原因

异常发生的原因有很多，通常包含以下几大类：

  * 用户输入了非法数据。
  * 要打开的文件不存在。
  * 网络通信时连接中断，或者JVM内存溢出。

这些异常有的是因为用户错误引起，有的是程序错误引起的，还有其它一些是因为物理错误引起的。



## 2\. 异常类型

为了更好地处理 Java 异常，我们需要掌握以下三种类型的异常：

  * **检查性异常：**  
    最具代表的检查性异常是用户错误或问题引起的异常，这是程序员无法预见的。例如要打开一个不存在文件时，一个异常就发生了，这些异常在编译时不能被简单地忽略。

  * **运行时异常：**  
    运行时异常是可能被程序员避免的异常。与检查性异常相反，运行时异常可以在编译时被忽略。

  * **错误：**  
    错误不是异常，而是脱离程序员控制的问题。错误在代码中通常被忽略。例如，当栈溢出时，一个错误就发生了，它们在编译也检查不到的。



## 3\. Exception 类的层次

所有的异常类是从 java.lang.Exception 类继承的子类。

Exception 类是 Throwable 类的子类。除了Exception类外，Throwable还有一个子类Error 。

Java 程序通常不捕获错误。错误一般发生在严重故障时，它们在Java程序处理的范畴之外。

Error 用来指示运行时环境发生的错误。

例如，JVM 内存溢出。一般地，程序不会从错误中恢复。

异常类有两个主要的子类：IOException 类和 RuntimeException 类。

在 Java 内置类中(接下来会说明)，有大部分常用检查性和非检查性异常。



## 4\. Java 内置异常类

Java 语言定义了一些异常类在 java.lang 标准包中。

标准运行时异常类的子类是最常见的异常类。由于 java.lang 包是默认加载到所有的 Java
程序的，所以大部分从运行时异常类继承而来的异常都可以直接使用。

Java 根据各个类库也定义了一些其他的异常，下面的表中列出了 Java 的非检查性异常。

| **异常**                                                     | **描述**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ArithmeticException                                          | 当出现异常的运算条件时，抛出此异常。例如，一个整数"除以零"时，抛出此类的一个范例。 |
| ArrayIndexOutOfBoundsException                               | 用非法索引访问数组时抛出的异常。如果索引为负或大于等于数组大小，则该索引为非法索引。 |
| ArrayStoreException                                          | 试图将错误类型的对象存储到一个对象数组时抛出的异常。         |
| ClassCastException                                           | 当试图将对象强制转换为不是范例的子类时，抛出该异常。         |
| IllegalArgumentException                                     | 抛出的异常表明向方法传递了一个不合法或不正确的参数。         |
| IllegalMonitorStateException                                 |      抛出的异常表明某一线程已经试图等待对象的监视器，或者试图通知其他正在等待对象的监视器而本身没有指定监视器的线程。                                                        |
|  |                                                              |
| IllegalStateException                                        | 在非法或不适当的时间调用方法时产生的信号。换句话说，即 Java 环境或 Java |
| 应用程序没有处于请求操作所要求的适当状态下。                 |                                                              |
| IllegalThreadStateException                                  | 线程没有处于请求操作所要求的适当状态时抛出的异常。           |
| IndexOutOfBoundsException                                    | 指示某排序索引（例如对数组、字符串或向量的排序）超出范围时抛出。 |
| NegativeArraySizeException                                   | 如果应用程序试图创建大小为负的数组，则抛出该异常。           |
| NullPointerException                                         | 当应用程序试图在需要对象的地方使用 null 时，抛出该异常       |
| NumberFormatException                                        | 当应用程序试图将字符串转换成一种数值类型，但该字符串不能转换为适当格式时，抛出该异常。 |
| SecurityException                                            | 由安全管理器抛出的异常，指示存在安全侵犯。                   |
| StringIndexOutOfBoundsException                              | 此异常由 String 方法抛出，指示索引或者为负，或者超出字符串的大小。 |
| UnsupportedOperationException                                | 当不支持请求的操作时，抛出该异常。                           |

下面的表中列出了 Java 定义在 java.lang 包中的检查性异常类。

| **异常**                                                     | **描述**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ClassNotFoundException                                       | 应用程序试图加载类时，找不到相应的类，抛出该异常。           |
| CloneNotSupportedException                                   | 当调用 Object 类中的 clone 方法克隆对象，但该对象的类无法实现 Cloneable |
| 接口时，抛出该异常。                                         |                                                              |
| IllegalAccessException                                       | 拒绝访问一个类的时候，抛出该异常。                           |
| InstantiationException                                       | 当试图使用 Class 类中的 newInstance                          |
| 方法创建一个类的范例，而指定的类对象因为是一个接口或是一个抽象类而无法范例化时，抛出该异常。 |                                                              |
| InterruptedException                                         | 一个线程被另一个线程中断，抛出该异常。                       |
| NoSuchFieldException                                         | 请求的变量不存在                                             |
| NoSuchMethodException                                        | 请求的方法不存在                                             |



## 5\. 异常方法

下面的列表是 Throwable 类的主要方法:

| **序号**                                                     | **方法及说明**                                  |
| ------------------------------------------------------------ | ----------------------------------------------- |
| 1                                                            | **public String getMessage()**                  |
| 返回关于发生的异常的详细信息。这个消息在Throwable 类的构造函数中初始化了。 |                                                 |
| 2                                                            | **public Throwable getCause()**                 |
| 返回一个Throwable 对象代表异常原因。                         |                                                 |
| 3                                                            | **public String toString()**                    |
| 使用getMessage()的结果返回类的串级名字。                     |                                                 |
| 4                                                            | **public void printStackTrace()**               |
| 打印toString()结果和栈层次到System.err，即错误输出流。       |                                                 |
| 5                                                            | **public StackTraceElement [] getStackTrace()** |
| 返回一个包含堆栈层次的数组。下标为0的元素代表栈顶，最后一个元素代表方法调用堆栈的栈底。 |                                                 |
| 6                                                            | **public Throwable fillInStackTrace()**         |
| 用当前的调用栈层次填充Throwable 对象栈层次，添加到栈层次任何先前信息中。 |                                                 |



## 6\. 捕获异常

使用 try 和 catch 关键字可以捕获异常。try/catch 代码块放在异常可能发生的地方。

try/catch代码块中的代码称为保护代码，使用 try/catch 的语法如下：




```java
try
{
   // 程序代码
}catch(ExceptionName e1)
{
   //Catch 块
}
```


Catch 语句包含要捕获异常类型的声明。当保护代码块中发生一个异常时，try 后面的 catch 块就会被检查。

如果发生的异常包含在 catch 块中，异常会被传递到该 catch 块，这和传递一个参数到方法是一样。

### 范例

下面的例子中声明有两个元素的一个数组，当代码试图访问数组的第三个元素的时候就会抛出一个异常。




```java
// 文件名 : ExcepTest.java
import java.io.*;
public class ExcepTest{
    
    public static void main(String args[]){
        try{
            int a[] = new int[2];
            System.out.println("Access element three :" + a[3]);
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Exception thrown  :" + e);
        }
        System.out.println("Out of the block");
    }
}
```


以上代码编译运行输出结果如下：




```java
Exception thrown  :java.lang.ArrayIndexOutOfBoundsException: 3
Out of the block
```




## 7\. 多重捕获块

一个 try 代码块后面跟随多个 catch 代码块的情况就叫多重捕获。

多重捕获块的语法如下所示：




```java
try{
    // 程序代码
    }catch(异常类型1 异常的变量名1){
    // 程序代码
    }catch(异常类型2 异常的变量名2){
    // 程序代码
    }catch(异常类型3 异常的变量名3){
    // 程序代码
    }
```


上面的代码段包含了 3 个 catch块。

可以在 try 语句后面添加任意数量的 catch 块。

如果保护代码中发生异常，异常被抛给第一个 catch 块。

如果抛出异常的数据类型与 ExceptionType1 匹配，它在这里就会被捕获。

如果不匹配，它会被传递给第二个 catch 块。

如此，直到异常被捕获或者通过所有的 catch 块。

### 范例

该范例展示了怎么使用多重 try/catch。




```java
try {
    file = new FileInputStream(fileName);
    x = (byte) file.read();
} catch(FileNotFoundException f) { // Not valid!
    f.printStackTrace();
    return -1;
} catch(IOException i) {
    i.printStackTrace();
    return -1;
}
```




## 8\. throws/throw 关键字：

如果一个方法没有捕获到一个检查性异常，那么该方法必须使用 throws 关键字来声明。throws 关键字放在方法签名的尾部。

也可以使用 throw 关键字抛出一个异常，无论它是新范例化的还是刚捕获到的。

下面方法的声明抛出一个 RemoteException 异常：




```java
import java.io.*;
public class className
{
    public void deposit(double amount) throws RemoteException
    {
    // Method implementation
    throw new RemoteException();
    }
    //Remainder of class definition
}    
```


一个方法可以声明抛出多个异常，多个异常之间用逗号隔开。

例如，下面的方法声明抛出 RemoteException 和 InsufficientFundsException：




```java
import java.io.*;
public class className
{
    public void withdraw(double amount) throws RemoteException,
                                InsufficientFundsException
    {
        // Method implementation
    }
    //Remainder of class definition
}
```




## 9\. finally关键字

finally 关键字用来创建在 try 代码块后面执行的代码块。

无论是否发生异常，finally 代码块中的代码总会被执行。

在 finally 代码块中，可以运行清理类型等收尾善后性质的语句。

finally 代码块出现在 catch 代码块最后，语法如下：




```java
try {
    // 程序代码
    }catch(异常类型1 异常的变量名1){
    // 程序代码
    }catch(异常类型2 异常的变量名2){
    // 程序代码
    }finally{
    // 程序代码
}
```


### 范例




```java
public class ExcepTest{
    public static void main(String args[]){
        int a[] = new int[2];
        try{
            System.out.println("Access element three :" + a[3]);
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("Exception thrown  :" + e);
        }
        finally{
            a[0] = 6;
            System.out.println("First element value: " +a[0]);
            System.out.println("The finally statement is executed");
        }
    }
    }
```


以上范例编译运行结果如下：




```java
Exception thrown  :java.lang.ArrayIndexOutOfBoundsException: 3
First element value: 6
The finally statement is executed
```


注意下面事项：

  * catch 不能独立于 try 存在。
  * 在 try/catch 后面添加 finally 块并非强制性要求的。
  * try 代码后不能既没 catch 块也没 finally 块。
  * try, catch, finally 块之间不能添加任何代码。



## 10\. 声明自定义异常

在 Java 中你可以自定义异常。编写自己的异常类时需要记住下面的几点。  

  * 所有异常都必须是 Throwable 的子类。
  * 如果希望写一个检查性异常类，则需要继承 Exception 类。
  * 如果你想写一个运行时异常类，那么需要继承 RuntimeException 类。

可以像下面这样定义自己的异常类：




```java
class MyException extends Exception{
}    
```


只继承Exception 类来创建的异常类是检查性异常类。

下面的 InsufficientFundsException 类是用户定义的异常类，它继承自 Exception。

一个异常类和其它任何类一样，包含有变量和方法。

### 范例

以下范例是一个银行账户的模拟，通过银行卡的号码完成识别，可以进行存钱和取钱的操作。




```java
// 文件名InsufficientFundsException.java
import java.io.*;
    
//自定义异常类，继承Exception类
public class InsufficientFundsException extends Exception
{
    //此处的amount用来储存当出现异常（取出钱多于余额时）所缺乏的钱
    private double amount;
    public InsufficientFundsException(double amount)
    {
    this.amount = amount;
    } 
    public double getAmount()
    {
    return amount;
    }
}
```


为了展示如何使用我们自定义的异常类，

在下面的 CheckingAccount 类中包含一个 withdraw() 方法抛出一个 InsufficientFundsException 异常。




```java
// 文件名称 CheckingAccount.java
import java.io.*;
    
//此类模拟银行账户
public class CheckingAccount
{
    //balance为余额，number为卡号
    private double balance;
    private int number;
    public CheckingAccount(int number)
    {
        this.number = number;
    }
    //方法：存钱
    public void deposit(double amount)
    {
        balance += amount;
    }
    //方法：取钱
    public void withdraw(double amount) throws
                                InsufficientFundsException
    {
        if(amount <= balance)
        {
            balance -= amount;
        }
        else
        {
            double needs = amount - balance;
            throw new InsufficientFundsException(needs);
        }
    }
    //方法：返回余额
    public double getBalance()
    {
        return balance;
    }
    //方法：返回卡号
    public int getNumber()
    {
        return number;
    }
}
```


下面的 BankDemo 程序示范了如何调用 CheckingAccount 类的 deposit() 和 withdraw() 方法。




```java
//文件名称 BankDemo.java
public class BankDemo
{
    public static void main(String [] args)
    {
        CheckingAccount c = new CheckingAccount(101);
        System.out.println("Depositing $500...");
        c.deposit(500.00);
        try
        {
            System.out.println("\nWithdrawing $100...");
            c.withdraw(100.00);
            System.out.println("\nWithdrawing $600...");
            c.withdraw(600.00);
        }catch(InsufficientFundsException e)
        {
            System.out.println("Sorry, but you are short $"
                                    + e.getAmount());
            e.printStackTrace();
        }
    }
}
```


编译上面三个文件，并运行程序 BankDemo，得到结果如下所示：




```java
Depositing $500...

Withdrawing $100...

Withdrawing $600...
Sorry, but you are short $200.0
InsufficientFundsException
        at CheckingAccount.withdraw(CheckingAccount.java:25)
        at BankDemo.main(BankDemo.java:13)
```




## 11\. 通用异常

在Java中定义了两种类型的异常和错误。

  * **JVM(Java** **虚拟机** **)** **异常：** 由 JVM 抛出的异常或错误。例如：NullPointerException 类，ArrayIndexOutOfBoundsException 类，ClassCastException 类。
  * **程序级异常：** 由程序或者API程序抛出的异常。例如 IllegalArgumentException 类，IllegalStateException 类。

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


```java
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
```


一个类可以包含以下类型变量：

```scala
局部变量：在方法、构造方法或者语句块中定义的变量被称为局部变量。变量声明和初始化都是在方法中，方法结束后，变量就会自动销毁。
成员变量：成员变量是定义在类中，方法体之外的变量。这种变量在创建对象的时候范例化。成员变量可以被类中方法、构造方法和特定类的语句块访问。
类变量：类变量也声明在类中，方法体之外，但必须声明为 static 类型。
```

一个类可以拥有多个方法，在上面的例子中：eat()、run()、sleep() 和 name() 都是 Dog 类的方法。



## 4\. 构造方法

每个类都有构造方法。如果没有显式地为类定义构造方法，Java 编译器将会为该类提供一个默认构造方法。

在创建一个对象的时候，至少要调用一个构造方法。构造方法的名称必须与类同名，一个类可以有多个构造方法。

下面是一个构造方法示例：


```java
            public class Puppy{
        public Puppy(){
        }
     
        public Puppy(String name){
            // 这个构造器仅有一个参数：name
        }
    }
```




## 5\. 创建对象

对象是根据类创建的。在Java中，使用关键字 new 来创建一个新的对象。创建对象需要以下三步：

```java
  * **声明** ：声明一个对象，包括对象名称和对象类型。
  * **范例化** ：使用关键字 new 来创建一个对象。
  * **初始化** ：使用 new 创建对象时，会调用构造方法初始化对象。
```

下面是一个创建对象的例子：


```java
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
```


编译并运行上面的程序，会打印出下面的结果：


```java
            小狗的名字是 : tommy
```




## 6\. 访问范例的变量和方法

通过已创建的对象来访问成员变量和成员方法，如下所示：


```java
            /* 范例化对象 */
    Object referenceVariable = new Constructor();
    /* 访问类中的变量 */
    referenceVariable.variableName;
    /* 访问类中的方法 */
    referenceVariable.methodName();
```


下面的例子展示如何访问范例变量和调用成员方法：


```java
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
```


编译并运行上面的程序，产生如下结果：


```java
            小狗的名字是 : tommy
    小狗的年龄为 : 2
    变量值 : 2
```




## 7\. 源文件声明规则

在本节的最后部分，我们将学习源文件的声明规则。当在一个源文件中定义多个类，并且还有import语句和package语句时，要特别注意这些规则。

```java
  * 一个源文件中只能有一个 public 类
  * 一个源文件可以有多个非 public 类
  * 源文件的名称应该和 public 类的类名保持一致。例如：源文件中 public 类的类名是 Employee，那么源文件应该命名为Employee.java。
  * 如果一个类定义在某个包中，那么 package 语句应该在源文件的首行。
  * 如果源文件包含 import 语句，那么应该放在 package 语句和类定义之间。如果没有 package 语句，那么 import 语句应该在源文件中最前面。
  * import 语句和 package 语句对源文件中定义的所有类都有效。在同一源文件中，不能给不同的类不同的包声明。
```

类有若干种访问级别，并且类也分不同的类型：抽象类和 final 类等。这些将在访问控制章节介绍。

除了上面提到的几种类型，Java 还有一些特殊的类，如：内部类、匿名类。



## 8\. Java 包

包主要用来对类和接口进行分类。当开发 Java 程序时，可能编写成百上千的类，因此很有必要对类和接口进行分类。

在 Java 中，如果给出




        
```java
   import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;
    
public class SendHTMLEmail
{
    public static void main(String [] args)
    {
   // 收件人电子邮箱
    String to = "abcd@gmail.com";

    // 发件人电子邮箱
    String from = "web@gmail.com";

    // 指定发送邮件的主机为 localhost
    String host = "localhost";

    // 获取系统属性
    Properties properties = System.getProperties();

    // 设置邮件服务器
    properties.setProperty("mail.smtp.host", host);

    // 获取默认的 Session 对象。
    Session session = Session.getDefaultInstance(properties);

    try{
        // 创建默认的 MimeMessage 对象。
        MimeMessage message = new MimeMessage(session);

        // Set From: 头部头字段
        message.setFrom(new InternetAddress(from));

        // Set To: 头部头字段
        message.addRecipient(Message.RecipientType.TO,
                                new InternetAddress(to));

        // Set Subject: 头字段
        message.setSubject("This is the Subject Line!");

        // 发送 HTML 消息, 可以插入html标签
        message.setContent("<h1>This is actual message</h1>",
                        "text/html" );

        // 发送消息
        Transport.send(message);
        System.out.println("Sent message successfully....");
    }catch (MessagingException mex) {
        mex.printStackTrace();
    }
}
```
}


# Java 网络编程

网络编程是指编写运行在多个设备（计算机）的程序，这些程序通过网络进行通信。

java.net 包中 J2SE 的 API 包含有类和接口，它们提供低层次的通信细节。你可以直接使用这些类和接口，来专注于解决问题，而不用关注通信细节。

java.net 包中提供了两种常见的网络协议的支持：

  * **TCP** ：TCP（英语：Transmission Control Protocol，传输控制协议） 是一种面向连接的、可靠的、基于字节流的传输层通信协议，TCP 层是位于 IP 层之上，应用层之下的中间层。TCP 保障了两个应用程序之间的可靠通信。通常用于互联网协议，被称 TCP / IP。
  * **UDP** ：UDP （英语：User Datagram Protocol，用户数据报协议），位于 OSI 模型的传输层。一个无连接的协议。提供了应用程序之间要发送数据的数据报。由于UDP缺乏可靠性且属于无连接协议，所以应用程序通常必须容许一些丢失、错误或重复的数据包。

本教程主要讲解以下两个主题。

  * **Socket 编程** ：这是使用最广泛的网络概念，它已被解释地非常详细。
  * **URL 处理** ：这部分会在另外的篇幅里讲，点击这里更详细地了解在 Java 语言中的 URL 处理。



## 1\. Socket 编程

套接字使用TCP提供了两台计算机之间的通信机制。 客户端程序创建一个套接字，并尝试连接服务器的套接字。

当连接建立时，服务器会创建一个 Socket 对象。客户端和服务器现在可以通过对 Socket 对象的写入和读取来进行通信。

java.net.Socket 类代表一个套接字，并且 java.net.ServerSocket
类为服务器程序提供了一种来监听客户端，并与他们建立连接的机制。

以下步骤在两台计算机之间使用套接字建立TCP连接时会出现：

  * 服务器范例化一个 ServerSocket 对象，表示通过服务器上的端口通信。
  * 服务器调用 ServerSocket 类的 accept() 方法，该方法将一直等待，直到客户端连接到服务器上给定的端口。
  * 服务器正在等待时，一个客户端范例化一个 Socket 对象，指定服务器名称和端口号来请求连接。
  * Socket 类的构造函数试图将客户端连接到指定的服务器和端口号。如果通信被建立，则在客户端创建一个 Socket 对象能够与服务器进行通信。
  * 在服务器端，accept() 方法返回服务器上一个新的 socket 引用，该 socket 连接到客户端的 socket。

连接建立后，通过使用 I/O
流在进行通信，每一个socket都有一个输出流和一个输入流，客户端的输出流连接到服务器端的输入流，而客户端的输入流连接到服务器端的输出流。

TCP 是一个双向的通信协议，因此数据可以通过两个数据流在同一时间发送.以下是一些类提供的一套完整的有用的方法来实现 socket。



## 2\. ServerSocket 类的方法

服务器应用程序通过使用 java.net.ServerSocket 类以获取一个端口,并且侦听客户端请求。

ServerSocket 类有四个构造方法：

| **序号**                                                     | **方法描述**                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                                                            | **public ServerSocket(int port) throws IOException**         |
| 创建绑定到特定端口的服务器套接字。                           |                                                              |
| 2                                                            | **public ServerSocket(int port, int backlog) throws IOException** |
| 利用指定的 backlog 创建服务器套接字并将其绑定到指定的本地端口号。 |                                                              |
| 3                                                            | **public ServerSocket(int port, int backlog, InetAddress address) throws |
| IOException**                                                |                                                              |
| 使用指定的端口、侦听 backlog 和要绑定到的本地 IP 地址创建服务器。 |                                                              |
| 4                                                            | **public ServerSocket() throws IOException**                 |
| 创建非绑定服务器套接字。                                     |                                                              |

创建非绑定服务器套接字。 如果 ServerSocket 构造方法没有抛出异常，就意味着你的应用程序已经成功绑定到指定的端口，并且侦听客户端请求。

这里有一些 ServerSocket 类的常用方法：

| **序号**                                            | **方法描述**                                          |
| --------------------------------------------------- | ----------------------------------------------------- |
| 1                                                   | **public int getLocalPort()**                         |
| 返回此套接字在其上侦听的端口。                      |                                                       |
| 2                                                   | **public Socket accept() throws IOException**         |
| 侦听并接受到此套接字的连接。                        |                                                       |
| 3                                                   | **public void setSoTimeout(int timeout)**             |
| 通过指定超时值启用/禁用 SO_TIMEOUT，以毫秒为单位。  |                                                       |
| 4                                                   | **public void bind(SocketAddress host, int backlog)** |
| 将 ServerSocket 绑定到特定地址（IP 地址和端口号）。 |                                                       |



## 3\. Socket 类的方法

java.net.Socket 类代表客户端和服务器都用来互相沟通的套接字。客户端要获取一个 Socket 对象通过范例化 ，而 服务器获得一个
Socket 对象则通过 accept() 方法的返回值。

Socket 类有五个构造方法.

| **序号**                                                 | **方法描述**                                                 |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| 1                                                        | **public Socket(String host, int port) throws UnknownHostException, |
| IOException.**                                           |                                                              |
| 创建一个流套接字并将其连接到指定主机上的指定端口号。     |                                                              |
| 2                                                        | **public Socket(InetAddress host, int port) throws IOException** |
| 创建一个流套接字并将其连接到指定 IP 地址的指定端口号。   |                                                              |
| 3                                                        | **public Socket(String host, int port, InetAddress localAddress, int |
| localPort) throws IOException.**                         |                                                              |
| 创建一个套接字并将其连接到指定远程主机上的指定远程端口。 |                                                              |
| 4                                                        | **public Socket(InetAddress host, int port, InetAddress localAddress, int |
| localPort) throws IOException.**                         |                                                              |
| 创建一个套接字并将其连接到指定远程地址上的指定远程端口。 |                                                              |
| 5                                                        | **public Socket()**                                          |
| 通过系统默认类型的 SocketImpl 创建未连接套接字           |                                                              |

当 Socket 构造方法返回，并没有简单的范例化了一个 Socket 对象，它实际上会尝试连接到指定的服务器和端口。

下面列出了一些感兴趣的方法，注意客户端和服务器端都有一个 Socket 对象，所以无论客户端还是服务端都能够调用这些方法。

| **序号**                                              | **方法描述**                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| 1                                                     | **public void connect(SocketAddress host, int timeout) throws |
| IOException**                                         |                                                              |
| 将此套接字连接到服务器，并指定一个超时值。            |                                                              |
| 2                                                     | **public InetAddress getInetAddress()**                      |
| 返回套接字连接的地址。                                |                                                              |
| 3                                                     | **public int getPort()**                                     |
| 返回此套接字连接到的远程端口。                        |                                                              |
| 4                                                     | **public int getLocalPort()**                                |
| 返回此套接字绑定到的本地端口。                        |                                                              |
| 5                                                     | **public SocketAddress getRemoteSocketAddress()**            |
| 返回此套接字连接的端点的地址，如果未连接则返回 null。 |                                                              |
| 6                                                     | **public InputStream getInputStream() throws IOException**   |
| 返回此套接字的输入流。                                |                                                              |
| 7                                                     | **public OutputStream getOutputStream() throws IOException** |
| 返回此套接字的输出流。                                |                                                              |
| 8                                                     | **public void close() throws IOException**                   |
| 关闭此套接字。                                        |                                                              |



## 4\. InetAddress 类的方法

这个类表示互联网协议(IP)地址。下面列出了 Socket 编程时比较有用的方法：

| **序号**                                            | **方法描述**                                                 |
| --------------------------------------------------- | ------------------------------------------------------------ |
| 1                                                   | **static InetAddress getByAddress(byte[] addr)**             |
| 在给定原始 IP 地址的情况下，返回 InetAddress 对象。 |                                                              |
| 2                                                   | **static InetAddress getByAddress(String host, byte[] addr)** |
| 根据提供的主机名和 IP 地址创建 InetAddress。        |                                                              |
| 3                                                   | **static InetAddress getByName(String host)**                |
| 在给定主机名的情况下确定主机的 IP 地址。            |                                                              |
| 4                                                   | **String getHostAddress()  **                                |
| 返回 IP 地址字符串（以文本表现形式）。              |                                                              |
| 5                                                   | **String getHostName()  **                                   |
| 获取此 IP 地址的主机名。                            |                                                              |
| 6                                                   | **static InetAddress getLocalHost()**                        |
| 返回本地主机。                                      |                                                              |
| 7                                                   | **String toString()**                                        |
| 将此 IP 地址转换为 String。                         |                                                              |



## 5\. Socket 客户端范例

如下的 GreetingClient 是一个客户端程序，该程序通过 socket 连接到服务器并发送一个请求，然后等待一个响应。




```java
import java.net.*;
import java.io.*;
    
public class GreetingClient
{
    public static void main(String [] args)
    {
        String serverName = args[0];
        int port = Integer.parseInt(args[1]);
        try
        {
            System.out.println("连接到主机：" + serverName + " ，端口号：" + port);
            Socket client = new Socket(serverName, port);
            System.out.println("远程主机地址：" + client.getRemoteSocketAddress());
            OutputStream outToServer = client.getOutputStream();
            DataOutputStream out = new DataOutputStream(outToServer);
    
            out.writeUTF("Hello from " + client.getLocalSocketAddress());
            InputStream inFromServer = client.getInputStream();
            DataInputStream in = new DataInputStream(inFromServer);
            System.out.println("服务器响应： " + in.readUTF());
            client.close();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
}
```




## 6\. Socket 服务端范例

如下的GreetingServer 程序是一个服务器端应用程序，使用 Socket 来监听一个指定的端口。




```java
import java.net.*;
import java.io.*;
    
public class GreetingServer extends Thread
{
    private ServerSocket serverSocket;
    
    public GreetingServer(int port) throws IOException
    {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(10000);
    }
    
    public void run()
    {
        while(true)
        {
            try
            {
            System.out.println("等待远程连接，端口号为：" + serverSocket.getLocalPort() + "...");
            Socket server = serverSocket.accept();
            System.out.println("远程主机地址：" + server.getRemoteSocketAddress());
            DataInputStream in = new DataInputStream(server.getInputStream());
            System.out.println(in.readUTF());
            DataOutputStream out = new DataOutputStream(server.getOutputStream());
            out.writeUTF("谢谢连接我：" + server.getLocalSocketAddress() + "\nGoodbye!");
            server.close();
            }catch(SocketTimeoutException s)
            {
            System.out.println("Socket timed out!");
            break;
            }catch(IOException e)
            {
            e.printStackTrace();
            break;
            }
        }
    }
    public static void main(String [] args)
    {
        int port = Integer.parseInt(args[0]);
        try
        {
            Thread t = new GreetingServer(port);
            t.run();
        }catch(IOException e)
        {
            e.printStackTrace();
        }
    }
} 
```


编译以上两个 java 文件代码，并执行以下命令来启动服务，使用端口号为 6066：




```java
$ javac GreetingServer.java 
$ java GreetingServer 6066
等待远程连接，端口号为：6066...
```


新开一个命令窗口，执行以上命令来开启客户端：




```java
$ javac GreetingClient.java 
$ java GreetingClient localhost 6066
连接到主机：localhost ，端口号：6066
远程主机地址：localhost/127.0.0.1:6066
服务器响应： 谢谢连接我：/127.0.0.1:6066
Goodbye!
```




# Java 泛型

Java 泛型（generics）提供了编译时类型安全检测机制，该机制允许程序员在编译时检测到非法的类型。
泛型的本质是参数化类型，也就是说所操作的数据类型被指定为一个参数。

假定我们有这样一个需求：写一个排序方法，能够对整型数组、字符串数组甚至其他任何类型的数组进行排序，该如何实现？

答案是可以使用 **Java 泛型** 。

使用 Java 泛型的概念，我们可以写一个泛型方法来对一个对象数组排序。然后，调用该泛型方法来对整型数组、浮点数数组、字符串数组等进行排序。



## 1\. 泛型方法

你可以写一个泛型方法，该方法在调用时可以接收不同类型的参数。根据传递给泛型方法的参数类型，编译器适当地处理每一个方法调用。

下面是定义泛型方法的规则：

  * 所有泛型方法声明都有一个类型参数声明部分（由尖括号分隔），该类型参数声明部分在方法返回类型之前（在下面例子中的<E>）。
  * 每一个类型参数声明部分包含一个或多个类型参数，参数间用逗号隔开。一个泛型参数，也被称为一个类型变量，是用于指定一个泛型类型名称的标识符。
  * 类型参数能被用来声明返回值类型，并且能作为泛型方法得到的实际参数类型的占位符。
  * 泛型方法体的声明和其他方法一样。注意类型参数只能代表引用型类型，不能是原始类型（像int,double,char的等）。

### 范例如下：

下面的例子演示了如何使用泛型方法打印不同类型的数组元素：




```java
public class GenericMethodTest
{
    // 泛型方法 printArray                         
    public static <E> void printArray( E[] inputArray )
    {
        // 输出数组元素            
            for ( E element : inputArray ){        
                System.out.printf( "%s ", element );
            }
    }
    
    public static void main( String args[] )
    {
        // 创建不同类型数组： Integer, Double 和 Character
        Integer[] intArray = { 1, 2, 3, 4, 5 };
        Double[] doubleArray = { 1.1, 2.2, 3.3, 4.4 };
        Character[] charArray = { 'H', 'E', 'L', 'L', 'O' };
    
        System.out.println( "整型数组元素为:" );
        printArray( intArray  ); // 传递一个整型数组
    
        System.out.println( "\n双精度型数组元素为:" );
        printArray( doubleArray ); // 传递一个双精度型数组
    
        System.out.println( "\n字符型数组元素为:" );
        printArray( charArray ); // 传递一个字符型数组
    } 
}
```


编译以上代码，运行结果如下所示：




```java
整型数组元素为:
1 2 3 4 5 

双精度型数组元素为:
1.1 2.2 3.3 4.4 

字符型数组元素为:
H E L L O 
```


有界的类型参数:

可能有时候，你会想限制那些被允许传递到一个类型参数的类型种类范围。例如，一个操作数字的方法可能只希望接受 Number 或者 Number
子类的范例。这就是有界类型参数的目的。

要声明一个有界的类型参数，首先列出类型参数的名称，后跟 extends 关键字，最后紧跟它的上界。

### 范例如下：

下面的例子演示了 "extends" 如何使用在一般意义上的意思 "extends"（类）或者
"implements"（接口）。该例子中的泛型方法返回三个可比较对象的最大值。




```java
public class MaximumTest
{
    // 比较三个值并返回最大值
    public static <T extends Comparable<T>> T maximum(T x, T y, T z)
    {                     
        T max = x; // 假设x是初始最大值
        if ( y.compareTo( max ) > 0 ){
            max = y; //y 更大
        }
        if ( z.compareTo( max ) > 0 ){
            max = z; // 现在 z 更大           
        }
        return max; // 返回最大对象
    }
    public static void main( String args[] )
    {
        System.out.printf( "%d, %d 和 %d 中最大的数为 %d\n\n",
                    3, 4, 5, maximum( 3, 4, 5 ) );
    
        System.out.printf( "%.1f, %.1f 和 %.1f 中最大的数为 %.1f\n\n",
                    6.6, 8.8, 7.7, maximum( 6.6, 8.8, 7.7 ) );
    
        System.out.printf( "%s, %s 和 %s 中最大的数为 %s\n","pear",
            "apple", "orange", maximum( "pear", "apple", "orange" ) );
    }
}    
```


编译以上代码，运行结果如下所示：




```java
3, 4 和 5 中最大的数为 5

6.6, 8.8 和 7.7 中最大的数为 8.8

pear, apple 和 orange 中最大的数为 pear
```




## 2\. 泛型类

泛型类的声明和非泛型类的声明类似，除了在类名后面添加了类型参数声明部分。

和泛型方法一样，泛型类的类型参数声明部分也包含一个或多个类型参数，参数间用逗号隔开。一个泛型参数，也被称为一个类型变量，是用于指定一个泛型类型名称的标识符。因为他们接受一个或多个参数，这些类被称为参数化的类或参数化的类型。

### 范例如下：

如下范例演示了我们如何定义一个泛型类:




```java
public class Box<T> {
    private T t;
    
    public void add(T t) {
        this.t = t;
    }
    
    public T get() {
        return t;
    }
    
    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<Integer>();
        Box<String> stringBox = new Box<String>();
    
        integerBox.add(new Integer(10));
        stringBox.add(new String("itbenkyou"));
    
        System.out.printf("整型值为 :%d\n\n", integerBox.get());
        System.out.printf("字符串为 :%s\n", stringBox.get());
    }
}
```


编译以上代码，运行结果如下所示：




```java
整型值为 :10

字符串为 :itbenkyou
```




## 3\. 类型通配符

1、类型通配符一般是使用?代替具体的类型参数。例如 **List <?>** 在逻辑上是 **List <String>,List<Integer>**
等所有List<具体类型实参>的父类。




```java
import java.util.*;

public class GenericTest {
        
    public static void main(String[] args) {
        List<String> name = new ArrayList<String>();
        List<Integer> age = new ArrayList<Integer>();
        List<Number> number = new ArrayList<Number>();
        
        name.add("icon");
        age.add(18);
        number.add(314);
    
        getData(name);
        getData(age);
        getData(number);
    }
    
    public static void getData(List<?> data) {
        System.out.println("data :" + data.get(0));
    }
}
```


输出结果为：




```java
data :icon
data :18
data :314
```


**解析：** 因为 getData() 方法的参数是 List 类型的，所以name，age，number 都可以作为这个方法的实参，这就是通配符的作用

2、类型通配符上限通过形如 List 来定义，如此定义就是通配符泛型值接受 Number 及其下层子类类型。




```java
import java.util.*;

public class GenericTest {
        
    public static void main(String[] args) {
        List<String> name = new ArrayList<String>();
        List<Integer> age = new ArrayList<Integer>();
        List<Number> number = new ArrayList<Number>();
        
        name.add("icon");
        age.add(18);
        number.add(314);
    
        //getUperNumber(name);//1
        getUperNumber(age);//2
        getUperNumber(number);//3
    }
    
    public static void getData(List<?> data) {
        System.out.println("data :" + data.get(0));
    }
    
    public static void getUperNumber(List<? extends Number> data) {
            System.out.println("data :" + data.get(0));
        }
}
```


输出结果：




```java
data :18
data :314
```


**解析：** 在(//1)处会出现错误，因为 getUperNumber() 方法中的参数已经限定了参数泛型上限为 Number，所以泛型为 String
是不在这个范围之内，所以会报错

3、类型通配符下限通过形如 **List <? super Number>**来定义，表示类型只能接受 Number 及其三层父类类型，如 Object
类型的范例。



修饰符 返回值类型 方法名(参数类型 参数名){
    ...
    方法体
    ...
    return 返回值;
}



# Java 包(package)

为了更好地组织类，Java 提供了包机制，用于区别类名的命名空间。



## 1\. 包的作用

  * 1、把功能相似或相关的类或接口组织在同一个包中，方便类的查找和使用。
  * 2、如同文件夹一样，包也采用了树形目录的存储方式。同一个包中的类名字是不同的，不同的包中的类的名字是可以相同的，当同时调用两个不同包中相同类名的类时，应该加上包名加以区别。因此，包可以避免名字冲突。
  * 3、包也限定了访问权限，拥有包访问权限的类才能访问某个包中的类。

Java
使用包（package）这种机制是为了防止命名冲突，访问控制，提供搜索和定位类（class）、接口、枚举（enumerations）和注释（annotation）等。

包的语法格式为：




```java
package pkg1[．pkg2[．pkg3…]];
```


例如：一个 Something.java 文件的内容。




```java
package net.java.util;

public class Something{
    ...
}
```


那么它的路径应该是 **net/java/util/Something.java** 这样保存的。 package(包) 的作用是把不同的 java
程序分类保存，更方便的被其他 java 程序调用。

一个包（package）可以定义为一组相互联系的类型（类、接口、枚举和注释），为这些类型提供访问保护和命名空间管理的功能。

以下是一些 Java 中的包：

  * **java.lang** -打包基础的类
  * **java.io** -包含输入输出功能的函数

开发者可以自己把一组类和接口等打包，并定义自己的包。而且在实际开发中这样做是值得提倡的，当你自己完成类的实现之后，将相关的类分组，可以让其他的编程者更容易地确定哪些类、接口、枚举和注释等是相关的。

由于包创建了新的命名空间（namespace），所以不会跟其他包中的任何名字产生命名冲突。使用包这种机制，更容易实现访问控制，并且让定位相关类更加简单。



## 2\. 创建包

创建包的时候，你需要为这个包取一个合适的名字。之后，如果其他的一个源文件包含了这个包提供的类、接口、枚举或者注释类型的时候，都必须将这个包的声明放在这个源文件的开头。

包声明应该在源文件的第一行，每个源文件只能有一个包声明，这个文件中的每个类型都应用于它。

如果一个源文件中没有使用包声明，那么其中的类，函数，枚举，注释等将被放在一个无名的包（unnamed package）中。

### 范例如下：

让我们来看一个例子，这个例子创建了一个叫做animals的包。通常使用小写的字母来命名避免与类、接口名字的冲突。

在 animals 包中加入一个接口（interface）：




```java
/* 文件名: Animal.java */
package animals;
    
interface Animal {
    public void eat();
    public void travel();
}
```


接下来，在同一个包中加入该接口的实现：




```java
package animals;

/* 文件名 : MammalInt.java */
public class MammalInt implements Animal{
    
    public void eat(){
        System.out.println("Mammal eats");
    }
    
    public void travel(){
        System.out.println("Mammal travels");
    } 
    
    public int noOfLegs(){
        return 0;
    }
    
    public static void main(String args[]){
        MammalInt m = new MammalInt();
        m.eat();
        m.travel();
    }
}
```


然后，编译这两个文件，并把他们放在一个叫做 animals 的子目录中。 用下面的命令来运行：




```java
$ mkdir animals
$ cp Animal.class  MammalInt.class animals
$ java animals/MammalInt
Mammal eats
Mammal travel
```




## 3\. import 关键字

为了能够使用某一个包的成员，我们需要在 Java 程序中明确导入该包。使用 "import" 语句可完成此功能。

在 java 源文件中 import 语句应位于 package 语句之后，所有类的定义之前，可以没有，也可以有多条，其语法格式为：




```java
import package1[.package2…].(classname|*);    
```


如果在一个包中，一个类想要使用本包中的另一个类，那么该包名可以省略。

### 范例如下：

下面的 payroll 包已经包含了 Employee 类，接下来向 payroll 包中添加一个 Boss 类。Boss 类引用 Employee
类的时候可以不用使用 payroll 前缀，Boss 类的范例如下。




```java
package payroll;

public class Boss
{
    public void payEmployee(Employee e)
    {
        e.mailCheck();
    }
} 
```


如果 Boss 类不在 payroll 包中又会怎样？Boss 类必须使用下面几种方法之一来引用其他包中的类。

使用类全名描述，例如：




```java
payroll.Employee
```


用 **import** 关键字引入，使用通配符 "*"：




```java
import payroll.*;
```


使用 **import** 关键字引入 Employee 类：




```java
import payroll.Employee;
```


**注意：**

类文件中可以包含任意数量的 import 声明。import 声明必须在包声明之后，类声明之前。



## 4\. package 的目录结构

类放在包中会有两种主要的结果：

  * 包名成为类名的一部分，正如我们前面讨论的一样。
  * 包名必须与相应的字节码所在的目录结构相吻合。

下面是管理你自己 java 中文件的一种简单方式：

将类、接口等类型的源码放在一个文本中，这个文件的名字就是这个类型的名字，并以 .java 作为扩展名。例如：




```java
// 文件名 :  Car.java
package vehicle;
    
public class Car {
    // 类实现  
}
```


接下来，把源文件放在一个目录中，这个目录要对应类所在包的名字。




```java
....\vehicle\Car.java
```


现在，正确的类名和路径将会是如下样子：

  * 类名 -> vehicle.Car
  * 路径名 -> vehicle\Car.java (在 windows 系统中)

通常，一个公司使用它互联网域名的颠倒形式来作为它的包名.例如：互联网域名是 codebaoku.com，所有的包名都以 com.codebaoku
开头。包名中的每一个部分对应一个子目录。

例如：有一个 **com.codebaoku.test** 的包，这个包包含一个叫做 CodeBaoku.java
的源文件，那么相应的，应该有如下面的一连串子目录：




```java
....\com\codebaoku\test\Codebaoku.java
```


编译的时候，编译器为包中定义的每个类、接口等类型各创建一个不同的输出文件，输出文件的名字就是这个类型的名字，并加上 .class 作为扩展后缀。 例如：




```java
// 文件名: Codebaoku.java
package com.codebaoku.test;
public class codebaoku {
        
}
class Google {
        
}
```


现在，我们用-d选项来编译这个文件，如下：




```java
$javac -d . Codebaoku.java
```


这样会像下面这样放置编译了的文件：




```java
.\com\codebaoku\test\Codebaoku.class
.\com\codebaoku\test\Google.class
```


你可以像下面这样来导入所有 **\com\codebaoku\test\** 中定义的类、接口等：




```java
import com.codebaoku.test.*;
```

编译之后的 .class 文件应该和 .java 源文件一样，它们放置的目录应该跟包的名字对应起来。但是，并不要求 .class 文件的路径跟相应的
.java 的路径一样。你可以分开来安排源码和类的目录。




```java
<path-one>\sources\com\codebaoku\test\codebaoku.java
<path-two>\classes\com\codebaoku\test\Google.class
```


这样，你可以将你的类目录分享给其他的编程人员，而不用透露自己的源码。用这种方法管理源码和类文件可以让编译器和java
虚拟机（JVM）可以找到你程序中使用的所有类型。

类目录的绝对路径叫做 **class path** 。设置在系统变量 **CLASSPATH** 中。编译器和 java 虚拟机通过将 package
名字加到 class path 后来构造 .class 文件的路径。

<path- two>\classes 是 class path，package 名字是 com.codebaoku.test,而编译器和 JVM 会在
<path-two>\classes\com\codebaoku\test 中找 .class 文件。

一个 class path 可能会包含好几个路径，多路径应该用分隔符分开。默认情况下，编译器和 JVM 查找当前目录。JAR 文件按包含 Java
平台相关的类，所以他们的目录默认放在了 class path 中。



## 5\. 设置 CLASSPATH 系统变量

用下面的命令显示当前的CLASSPATH变量：

  * Windows 平台（DOS 命令行下）：C:\> set CLASSPATH
  * UNIX 平台（Bourne shell 下）：# echo $CLASSPATH

删除当前CLASSPATH变量内容：  

  * Windows 平台（DOS 命令行下）：C:\> set CLASSPATH=
  * UNIX 平台（Bourne shell 下）：# unset CLASSPATH; export CLASSPATH

设置CLASSPATH变量:

  * Windows 平台（DOS 命令行下）： C:\> set CLASSPATH=C:\users\jack\java\classes
  * UNIX 平台（Bourne shell 下）：# CLASSPATH=/home/jack/java/classes; export CLASSPATH



+++

# Java 文档注释<

Java 支持三种注释方式。前两种分别是 **//** 和 **/* */** ，第三种被称作说明注释，它以 **/**** 开始，以 ***/** 结束。

我们可以使用 javadoc 工具软件将程序中的说明注释，输出到 HTML 文件中。



## 1\. javadoc 标签

javadoc 工具软件识别以下标签：

| **标签**                | **描述**                                               | **示例**                                    |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------- |
| @author                 | 标识一个类的作者                                       | @author description                         |
| @deprecated             | 指名一个过期的类或成员                                 | @deprecated description                     |
| {@docRoot}              | 指明当前文档根目录的路径                               | Directory Path                              |
| @exception              | 标志一个类抛出的异常                                   | @exception exception-name explanation       |
| {@inheritDoc}           | 从直接父类继承的注释                                   | Inherits a comment from the immediate       |
| surperclass.            |                                                        |                                             |
| {@link}                 | 插入一个到另一个主题的链接                             | {@link name text}                           |
| {@linkplain}            | 插入一个到另一个主题的链接，但是该链接显示纯文本字体   | Inserts an in-line link to                  |
| another topic.          |                                                        |                                             |
| @param                  | 说明一个方法的参数                                     | @param parameter-name explanation           |
| @return                 | 说明返回值类型                                         | @return explanation                         |
| @see                    | 指定一个到另一个主题的链接                             | @see anchor                                 |
| @serial                 | 说明一个序列化属性                                     | @serial description                         |
| @serialData             | 说明通过writeObject( ) 和 writeExternal( )方法写的数据 | @serialData                                 |
| description             |                                                        |                                             |
| @serialField            | 说明一个ObjectStreamField组件                          | @serialField name type description          |
| @since                  | 标记当引入一个特定的变化时                             | @since release                              |
| @throws                 | 和 @exception标签一样.                                 | The @throws tag has the same meaning as the |
| @exception tag.         |                                                        |                                             |
| {@value}                | 显示常量的值，该常量必须是static属性。                 | Displays the value of a constant, which     |
| must be a static field. |                                                        |                                             |
| @version                | 指定类的版本                                           | @version info                               |



## 2\. 文档注释

在开始的 **/**** 之后，第一行或几行是关于类、变量和方法的主要描述。

之后，你可以包含一个或多个各种各样的 **@** 标签。每一个 **@** 标签必须在一个新行的开始或者在一行的开始紧跟星号(*).

多个相同类型的标签应该放成一组。例如，如果你有三个 **@see** 标签，可以将它们一个接一个的放在一起。

下面是一个类的说明注释的范例：




```java
/*** 这个类绘制一个条形图
* @author codebaoku
* @version 1.2
*/
```




## 3\. javadoc 输出什么

javadoc 工具将你 Java 程序的源代码作为输入，输出一些包含你程序注释的HTML文件。

每一个类的信息将在独自的HTML文件里。javadoc 也可以输出继承的树形结构和索引。

由于 javadoc 的实现不同，工作也可能不同，你需要检查你的 Java 开发系统的版本等细节，选择合适的 Javadoc 版本。



## 4\. javadoc 输出范例

下面是一个使用说明注释的简单范例。注意每一个注释都在它描述的项目的前面。

在经过 javadoc 处理之后，SquareNum 类的注释将在 SquareNum.html 中找到。




```java
import java.io.*;

/**
* 这个类演示了文档注释
* @author Ayan Amhed
* @version 1.2
*/
public class SquareNum {
    /**
    * This method returns the square of num.
    * This is a multiline description. You can use
    * as many lines as you like.
    * @param num The value to be squared.
    * @return num squared.
    */
    public double square(double num) {
        return num * num;
    }
    /**
    * This method inputs a number from the user.
    * @return The value input as a double.
    * @exception IOException On input error.
    * @see IOException
    */
    public double getNumber() throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader inData = new BufferedReader(isr);
        String str;
        str = inData.readLine();
        return (new Double(str)).doubleValue();
    }
    /**
    * This method demonstrates square().
    * @param args Unused.
    * @return Nothing.
    * @exception IOException On input error.
    * @see IOException
    */
    public static void main(String args[]) throws IOException
    {
        SquareNum ob = new SquareNum();
        double val;
        System.out.println("Enter value to be squared: ");
        val = ob.getNumber();
        val = ob.square(val);
        System.out.println("Squared value is " + val);
    }
}
```


如下，使用 javadoc 工具处理 SquareNum.java 文件：




```java
$ javadoc SquareNum.java
Loading source file SquareNum.java...
Constructing Javadoc information...
Standard Doclet version 1.5.0_13
Building tree for all the packages and classes...
Generating SquareNum.html...
SquareNum.java:39: warning - @return tag cannot be used\
                      in method with void return type.
Generating package-frame.html...
Generating package-summary.html...
Generating package-tree.html...
Generating constant-values.html...
Building index for all the packages and classes...
Generating overview-tree.html...
Generating index-all.html...
Generating deprecated-list.html...
Building index for all classes...
Generating allclasses-frame.html...
Generating allclasses-noframe.html...
Generating index.html...
Generating help-doc.html...
Generating stylesheet.css...
1 warning
$
```





# Java 文件操作

在 Java 程序开发中，我们对文件进行操作，比如创建文件或目录、读写文件等。Java 提供了文件封装类 java.io.File
用于操作硬盘上的文件目录。



## 1\. 创建目录

File类中有两个方法可以用来创建文件夹：

  * **mkdir( )** 方法创建一个文件夹，成功则返回true，失败则返回false。失败表明File对象指定的路径已经存在，或者由于整个路径还不存在，该文件夹不能被创建。
  * **mkdirs()** 方法创建一个文件夹和它的所有父文件夹。

下面的例子创建 "/tmp/user/java/bin"文件夹：




```java
import java.io.File;
 
public class CreateDir {
    public static void main(String[] args) {
        String dirname = "/tmp/user/java/bin";
        File d = new File(dirname);
        // 现在创建目录
        d.mkdirs();
    }
}
```


编译并执行上面代码来创建目录 "/tmp/user/java/bin"。

**注意：** Java 在 UNIX 和 Windows 自动按约定分辨文件路径分隔符。如果你在 Windows 版本的 Java 中使用分隔符 (/)
，路径依然能够被正确解析。



## 2\. 读取目录

一个目录其实就是一个 File 对象，它包含其他文件和文件夹。

如果创建一个 File 对象并且它是一个目录，那么调用 isDirectory() 方法会返回 true。

可以通过调用该对象上的 list() 方法，来提取它包含的文件和文件夹的列表。

下面展示的例子说明如何使用 list() 方法来检查一个文件夹中包含的内容：




```java
import java.io.File;

public class DirList {
    public static void main(String args[]) {
        String dirname = "/tmp";
        File f1 = new File(dirname);
        if (f1.isDirectory()) {
            System.out.println("目录 " + dirname);
            String s[] = f1.list();
            for (int i = 0; i < s.length; i++) {
                File f = new File(dirname + "/" + s[i]);
                if (f.isDirectory()) {
                    System.out.println(s[i] + " 是一个目录");
                } else {
                    System.out.println(s[i] + " 是一个文件");
                }
            }
        } else {
            System.out.println(dirname + " 不是一个目录");
        }
    }
}
```


以上范例编译运行结果如下：




```java
目录 /tmp
bin 是一个目录
lib 是一个目录
demo 是一个目录
test.txt 是一个文件
README 是一个文件
index.html 是一个文件
include 是一个目录
```




## 3\. 删除目录或文件

删除文件可以使用 **java.io.File.delete()** 方法。

以下代码会删除目录 **/tmp/java/** ，需要注意的是当删除某一目录时，必须保证该目录下没有其他文件才能正确删除，否则将删除失败。

测试目录结构：




```java
/tmp/java/
|-- 1.log
|-- test
```





```java
import java.io.File;

public class DeleteFileDemo {
    public static void main(String[] args) {
        // 这里修改为自己的测试目录
        File folder = new File("/tmp/java/");
        deleteFolder(folder);
    }
    
    // 删除文件及目录
    public static void deleteFolder(File folder) {
        File[] files = folder.listFiles();
        if (files != null) {
            for (File f : files) {
                if (f.isDirectory()) {
                    deleteFolder(f);
                } else {
                    f.delete();
                }
            }
        }
        folder.delete();
    }
}
```




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




```java
public class Person {
    private String name;
    private int age;
}
```


这段代码中，将 **name** 和 **age** 属性设置为私有的，只能本类才能访问，其他类都访问不了，如此就对信息进行了隐藏。

2）对每个值属性提供对外的公共方法访问，也就是创建一对赋取值方法，用于对私有属性的访问，例如：




```java
public class Person{
    private String name;
    private int age;

    public int getAge(){
        return age;
    }

    public String getName(){
        return name;
    }

    public void setAge(int age){
        this.age = age;
    }

    public void setName(String name){
        this.name = name;
    }
}
```


采用 **this** 关键字是为了解决范例变量（private String name）和局部变量（setName(String
name)中的name变量）之间发生的同名的冲突。



## 2\. Java 封装的范例

让我们来看一个java封装类的例子：




```java
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
```


以上范例中public方法是外部类访问该类成员变量的入口。

通常情况下，这些方法被称为getter和setter方法。

因此，任何要访问类中私有成员变量的类都要通过这些getter和setter方法。

通过如下的例子说明EncapTest类的变量怎样被访问：




```java
public class RunEncap{
    public static void main(String args[]){
        EncapTest encap = new EncapTest();
        encap.setName("James");
        encap.setAge(20);
        
        System.out.print("Name : " + encap.getName()+ 
                                " Age : "+ encap.getAge());
    }
}
```


以上代码编译运行结果如下:




```java
Name : James Age : 20
```



# Java 日期时间

java.util 包提供了 Date 类来封装当前的日期和时间。

java.util 包提供了 Calendar 类用来设置和获取日期数据的特定部分。

另外，还提供了 SimpleDateFormat 类来格式化日期的格式。



## 1\. Date 类

### 1）Date 类的创建

Date 类提供两个构造函数来范例化 Date 对象。

第一个构造函数使用当前日期和时间来初始化对象。




```java
Date()
```


第二个构造函数接收一个参数，该参数是从1970年1月1日起的毫秒数。




```java
Date(long millisec)
```


### 2）Date 类的操作

Date对象创建以后，可以调用下面的方法。

| 序号                                                         | 方法和描述                      |
| ------------------------------------------------------------ | ------------------------------- |
| 1                                                            | **boolean after(Date date)**    |
| 若当调用此方法的Date对象在指定日期之后返回true,否则返回false。 |                                 |
| 2                                                            | **boolean before(Date date)**   |
| 若当调用此方法的Date对象在指定日期之前返回true,否则返回false。 |                                 |
| 3                                                            | **Object clone( )**             |
| 返回此对象的副本。                                           |                                 |
| 4                                                            | **int compareTo(Date date)**    |
| 比较当调用此方法的Date对象和指定日期。两者相等时候返回0。调用对象在指定日期之前则返回负数。调用对象在指定日期之后则返回正数。 |                                 |
| 5                                                            | **int compareTo(Object obj)**   |
| 若obj是Date类型则操作等同于compareTo(Date) 。否则它抛出ClassCastException。 |                                 |
| 6                                                            | **boolean equals(Object date)** |
| 当调用此方法的Date对象和指定日期相等时候返回true,否则返回false。 |                                 |
| 7                                                            | **long getTime( )**             |
| 返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 Date 对象表示的毫秒数。 |                                 |
| 8                                                            | **int hashCode( )**             |
| 返回此对象的哈希码值。                                       |                                 |
| 9                                                            | **void setTime(long time)**     |

用自1970年1月1日00:00:00 GMT以后time毫秒数设置时间和日期。  
10 |  **String toString( )**  
把此 Date 对象转换为以下形式的 String： dow mon dd hh:mm:ss zzz yyyy 其中： dow 是一周中的某一天 (Sun,
Mon, Tue, Wed, Thu, Fri, Sat)。  

### 3）获取当前日期时间

Java中获取当前日期和时间很简单，使用 Date 对象的 toString() 方法来打印当前日期和时间：




```java
import java.util.Date;
  
public class DateDemo {
   public static void main(String args[]) {
       // 初始化 Date 对象
       Date date = new Date();
        
       // 使用 toString() 函数显示日期时间
       System.out.println(date.toString());
   }
}
```


以上范例编译运行结果如下:




```java
Mon May 04 09:51:52 CDT 2013
```


### 4）日期比较

Java使用以下三种方法来比较两个日期：

  * 使用 getTime() 方法获取两个日期（自1970年1月1日经历的毫秒数值），然后比较这两个值。
  * 使用方法 before()，after() 和 equals()。例如，一个月的12号比18号早，则 new Date(99, 2, 12).before(new Date (99, 2, 18)) 返回true。
  * 使用 compareTo() 方法，它是由 Comparable 接口定义的，Date 类实现了这个接口。



## 2\. SimpleDateFormat 类

SimpleDateFormat 是一个以语言环境敏感的方式来格式化和分析日期的类。SimpleDateFormat
允许你选择任何用户自定义日期时间格式来运行。

### 1）SimpleDateFormat 类使用案例




```java
import  java.util.*;
import java.text.*;
 
public class DateDemo {
   public static void main(String args[]) {
 
      Date dNow = new Date( );
      SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
 
      System.out.println("当前时间为: " + ft.format(dNow));
   }
}
```


代码说明:




```java
SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
```


这一行代码确立了转换的格式，其中 yyyy 是完整的公元年，MM 是月份，dd 是日期，HH:mm:ss 是时、分、秒。

**注意** :有的格式大写，有的格式小写，例如 MM 是月份，mm 是分；HH 是 24 小时制，而 hh 是 12 小时制。

以上范例编译运行结果如下:




```java
当前时间为: 2018-09-06 10:16:34
```


### 2）日期和时间的格式化编码

时间模式字符串用来指定时间格式。在此模式中，所有的 ASCII 字母被保留为模式字母，定义如下：

| **字母** | **描述**                 | **示例**                |
| -------- | ------------------------ | ----------------------- |
| G        | 纪元标记                 | AD                      |
| y        | 四位年份                 | 2001                    |
| M        | 月份                     | July or 07              |
| d        | 一个月的日期             | 10                      |
| h        | A.M./P.M. (1~12)格式小时 | 12                      |
| H        | 一天中的小时 (0~23)      | 22                      |
| m        | 分钟数                   | 30                      |
| s        | 秒数                     | 55                      |
| S        | 毫秒数                   | 234                     |
| E        | 星期几                   | Tuesday                 |
| D        | 一年中的日子             | 360                     |
| F        | 一个月中第几周的周几     | 2 (second Wed. in July) |
| w        | 一年中第几周             | 40                      |
| W        | 一个月中第几周           | 1                       |
| a        | A.M./P.M. 标记           | PM                      |
| k        | 一天中的小时(1~24)       | 24                      |
| K        | A.M./P.M. (0~11)格式小时 | 10                      |
| z        | 时区                     | Eastern Standard Time   |
| '        | 文字定界符               | Delimiter               |
| "        | 单引号                   | `                       |

### 3）解析字符串为时间

SimpleDateFormat 类有一些附加的方法，特别是parse()，它试图按照给定的SimpleDateFormat
对象的格式化存储来解析字符串。例如：




```java
import java.util.*;
import java.text.*;
  
public class DateDemo {
 
   public static void main(String args[]) {
      SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd"); 
 
      String input = args.length == 0 ? "1818-11-11" : args[0]; 
 
      System.out.print(input + " Parses as "); 
 
      Date t; 
 
      try { 
          t = ft.parse(input); 
          System.out.println(t); 
      } catch (ParseException e) { 
          System.out.println("Unparseable using " + ft); 
      }
   }
}
```


以上范例编译运行结果如下:




```java
$ java DateDemo
1818-11-11 Parses as Wed Nov 11 00:00:00 GMT 1818
$ java DateDemo 2007-12-01
2007-12-01 Parses as Sat Dec 01 00:00:00 GMT 2007
```




## 3\. Calendar类

我们现在已经能够格式化并创建一个日期对象了，但是我们如何才能设置和获取日期数据的特定部分呢，比如说小时，日，或者分钟?
我们又如何在日期的这些部分加上或者减去值呢? 答案是使用Calendar 类。

Calendar类的功能要比Date类强大很多，而且在实现方式上也比Date类要复杂一些。

Calendar类是一个抽象类，在实际使用时实现特定的子类的对象，创建对象的过程对程序员来说是透明的，只需要使用getInstance方法创建即可。

### 1）创建一个代表系统当前日期的Calendar对象




```java
Calendar c = Calendar.getInstance();//默认是当前日期
```


### 2）创建一个指定日期的Calendar对象

使用Calendar类代表特定的时间，需要首先创建一个Calendar的对象，然后再设定该对象中的年月日参数来完成。




```java
//创建一个代表2009年6月12日的Calendar对象
Calendar c1 = Calendar.getInstance();
c1.set(2009, 6 - 1, 12);
```


### 3）Calendar类对象字段类型

Calendar类中用以下这些常量表示不同的意义，jdk内的很多类其实都是采用的这种思想

| 常量                  | 描述                           |
| --------------------- | ------------------------------ |
| Calendar.YEAR         | 年份                           |
| Calendar.MONTH        | 月份                           |
| Calendar.DATE         | 日期                           |
| Calendar.DAY_OF_MONTH | 日期，和上面的字段意义完全相同 |
| Calendar.HOUR         | 12小时制的小时                 |
| Calendar.HOUR_OF_DAY  | 24小时制的小时                 |
| Calendar.MINUTE       | 分钟                           |
| Calendar.SECOND       | 秒                             |
| Calendar.DAY_OF_WEEK  | 星期几                         |

### 4）Calendar类对象信息的设置

**Set设置**

如：




```java
Calendar c1 = Calendar.getInstance();
```

调用：




```java
public final void set(int year,int month,int date)
```





```java
c1.set(2009, 6, 12);//把Calendar对象c1的年月日分别设这为：2009、6、12
```


利用字段类型设置

如果只设定某个字段，例如日期的值，则可以使用如下set方法：




```java
public void set(int field,int value)
```

把 c1对象代表的日期设置为10号，其它所有的数值会被重新计算




```java
c1.set(Calendar.DATE,10);
```


把c1对象代表的年份设置为2008年，其他的所有数值会被重新计算




```java
c1.set(Calendar.YEAR,2008);
```


其他字段属性set的意义以此类推

**Add设置**




```java
Calendar c1 = Calendar.getInstance();
```


把c1对象的日期加上10，也就是c1也就表示为10天后的日期，其它所有的数值会被重新计算




```java
c1.add(Calendar.DATE, 10);
```


把c1对象的日期减去10，也就是c1也就表示为10天前的日期，其它所有的数值会被重新计算




```java
c1.add(Calendar.DATE, -10);
```

其他字段属性的add的意义以此类推

### 5）Calendar类对象信息的获得




```java
Calendar c1 = Calendar.getInstance();
// 获得年份
int year = c1.get(Calendar.YEAR);
// 获得月份
int month = c1.get(Calendar.MONTH) + 1;
// 获得日期
int date = c1.get(Calendar.DATE);
// 获得小时
int hour = c1.get(Calendar.HOUR_OF_DAY);
// 获得分钟
int minute = c1.get(Calendar.MINUTE);
// 获得秒
int second = c1.get(Calendar.SECOND);
// 获得星期几（注意（这个与Date类是不同的）：1代表星期日、2代表星期1、3代表星期二，以此类推）
int day = c1.get(Calendar.DAY_OF_WEEK);
```



# Java 抽象类

如果一个类中没有包含足够的信息来描绘一个具体的对象，这样的类称为抽象类。抽象类无法进行范例化，不能直接使用 new 关键字调用其构造器生成该类的对象。

在 Java 语言中由 abstract 修饰的类叫抽象类，由 abstract 修饰的方法叫抽象方法。



## 1\. Java 抽象类的定义语法




```java
abstract class 类名
{
abstract int 方法名();
}
```


抽象方法没有方法体，也就是方法后面是没有大括号及其包含的代码。在抽象类中既可以有抽象方法，也可以有普通方法。

凡是继承这个抽象类的实体子类，都必须要实现所有的抽象方法。



## 2\. Java 抽象类的特点

  * （1）抽象类不能被范例化。
  * （2）构造方法 和 static 方法不能抽象。
  * （3）父类的抽象方法需要在子类中实现。
  * （4）抽象类可以具有指向子类对象的对象引用。

## 3\. Java 抽象类的范例

### 1）定义抽象类：Employee


```java
            /**
     * 员工类
     */
    public abstract class Employee {
        protected String name;
        protected boolean gender;
        public Employee(String name, boolean gender){
            this.name=name;
            this.gender=gender;
        }
        /**
        * 领工资操作
        */
        public abstract void getSalary();
    
        public void getName(){
            System.out.println("我是" + name);
        }
    }
```


### 2）继承抽象类：Manager

新建一个经理类 Manager，继承抽象类 Employee。我们必须要重写抽象方法 getSalary。


```java
            /**
     * 经理类
     */
    public class Manager extends Employee{
        public Manager(String name,boolean gender){
            super(name,gender);
        }
    
        //重写父类的抽象方法
        public void getSalary(){
            System.out.println("经理领9000元工资");
        }
    }
```


### 3）继承抽象类：Accountant

新建一个会计类 Accountant，继承抽象类 Employee。我们必须要重写抽象方法 getSalary。


```java
            /**
     * 会计类
     */
    public class Accountant extends Employee{
        public Accountant(String name,boolean gender){
            super(name,gender);
        }
    
        //重写父类的抽象方法
        public void getSalary(){
            System.out.println("会计领7000元工资");
        }
    }
```


### 4）抽象类测试


```java
            public class AbstractTest {
        public static void main(String[] args) {
            Manager manager = new Manager("张经理", true);
            manager.getName();
            manager.getSalary();
    
            Accountant accountant = new Accountant("李会计", false);
            accountant.getName();
            accountant.getSalary();
        }
    }
```


运行执行结果：


```java
            $ javac AbstractTest.java
    $ java AbstractTest
    
    我是张经理
    经理领9000元工资
    我是李会计
    会计领7000元工资
```






# Java 多线程编程

Java 给多线程编程提供了内置的支持。 一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。

多线程是多任务的一种特别的形式，但多线程使用了更小的资源开销。

这里定义和线程相关的另一个术语 -
进程：一个进程包括由操作系统分配的内存空间，包含一个或多个线程。一个线程不能独立的存在，它必须是进程的一部分。一个进程一直运行，直到所有的非守护线程都结束运行后才能结束。

多线程能满足程序员编写高效率的程序来达到充分利用 CPU 的目的。





## 1\. 线程的生命周期

线程是一个动态执行的过程，它也有一个从产生到死亡的过程。

下图显示了一个线程完整的生命周期。

  * **新建状态：** 使用 **new** 关键字和 **Thread** 类或其子类建立一个线程对象后，该线程对象就处于新建状态。它保持这个状态直到程序 **start()** 这个线程。
  * **就绪状态：** 当线程对象调用了start()方法之后，该线程就进入就绪状态。就绪状态的线程处于就绪队列中，要等待JVM里线程调度器的调度。
  * **运行状态：** 如果就绪状态的线程获取 CPU 资源，就可以执行 **run()** ，此时线程便处于运行状态。处于运行状态的线程最为复杂，它可以变为阻塞状态、就绪状态和死亡状态。
  * **阻塞状态：** 如果一个线程执行了sleep（睡眠）、suspend（挂起）等方法，失去所占用资源之后，该线程就从运行状态进入阻塞状态。在睡眠时间已到或获得设备资源后可以重新进入就绪状态。可以分为三种：   

    * 等待阻塞：运行状态中的线程执行 wait() 方法，使线程进入到等待阻塞状态。
    * 同步阻塞：线程在获取 synchronized 同步锁失败(因为同步锁被其他线程占用)。
    * 其他阻塞：通过调用线程的 sleep() 或 join() 发出了 I/O 请求时，线程就会进入到阻塞状态。当sleep() 状态超时，join() 等待线程终止或超时，或者 I/O 处理完毕，线程重新转入就绪状态。
  * **死亡状态：** 一个运行状态的线程完成任务或者其他终止条件发生时，该线程就切换到终止状态。



## 2\. 线程的优先级

每一个 Java 线程都有一个优先级，这样有助于操作系统确定线程的调度顺序。

Java 线程的优先级是一个整数，其取值范围是 1 （Thread.MIN_PRIORITY ） - 10 （Thread.MAX_PRIORITY ）。

默认情况下，每一个线程都会分配一个优先级 NORM_PRIORITY（5）。

具有较高优先级的线程对程序更重要，并且应该在低优先级的线程之前分配处理器资源。但是，线程优先级不能保证线程执行的顺序，而且非常依赖于平台。



## 3\. 创建线程

Java 提供了三种创建线程的方法：

  * 通过实现 Runnable 接口；
  * 通过继承 Thread 类本身；
  * 通过 Callable 和 Future 创建线程。



## 4\. 通过实现 Runnable 接口来创建线程

创建一个线程，最简单的方法是创建一个实现 Runnable 接口的类。

为了实现 Runnable，一个类只需要执行一个方法调用 run()，声明如下：




```java
public void run()
```


你可以重写该方法，重要的是理解的 run() 可以调用其他方法，使用其他类，并声明变量，就像主线程一样。

在创建一个实现 Runnable 接口的类之后，你可以在类中范例化一个线程对象。

Thread 定义了几个构造方法，下面的这个是我们经常使用的：




```java
Thread(Runnable threadOb,String threadName);
```


这里，threadOb 是一个实现 Runnable 接口的类的范例，并且 threadName 指定新线程的名字。

新线程创建之后，你调用它的 start() 方法它才会运行。




```java
void start();
```


下面是一个创建线程并开始让它执行的范例：




```java
class RunnableDemo implements Runnable {
    private Thread t;
    private String threadName;
    
    RunnableDemo( String name) {
        threadName = name;
        System.out.println("Creating " +  threadName );
    }
    
    public void run() {
        System.out.println("Running " +  threadName );
        try {
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                // 让线程睡眠一会
                Thread.sleep(50);
            }
        }catch (InterruptedException e) {
            System.out.println("Thread " +  threadName + " interrupted.");
        }
        System.out.println("Thread " +  threadName + " exiting.");
    }
    
    public void start () {
        System.out.println("Starting " +  threadName );
        if (t == null) {
            t = new Thread (this, threadName);
            t.start ();
        }
    }
    }
    
    public class TestThread {
    
    public static void main(String args[]) {
        RunnableDemo R1 = new RunnableDemo( "Thread-1");
        R1.start();
        
        RunnableDemo R2 = new RunnableDemo( "Thread-2");
        R2.start();
    }   
    }
```


编译以上程序运行结果如下：




```java
Creating Thread-1
Starting Thread-1
Creating Thread-2
Starting Thread-2
Running Thread-1
Thread: Thread-1, 4
Running Thread-2
Thread: Thread-2, 4
Thread: Thread-1, 3
Thread: Thread-2, 3
Thread: Thread-1, 2
Thread: Thread-2, 2
Thread: Thread-1, 1
Thread: Thread-2, 1
Thread Thread-1 exiting.
Thread Thread-2 exiting.
```




## 5\. 通过继承 Thread 来创建线程

创建一个线程的第二种方法是创建一个新的类，该类继承 Thread 类，然后创建一个该类的范例。

继承类必须重写 run() 方法，该方法是新线程的入口点。它也必须调用 start() 方法才能执行。

该方法尽管被列为一种多线程实现方式，但是本质上也是实现了 Runnable 接口的一个范例。




```java
class ThreadDemo extends Thread {
    private Thread t;
    private String threadName;
    
    ThreadDemo( String name) {
        threadName = name;
        System.out.println("Creating " +  threadName );
    }
    
    public void run() {
        System.out.println("Running " +  threadName );
        try {
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                // 让线程睡眠一会
                Thread.sleep(50);
            }
        }catch (InterruptedException e) {
            System.out.println("Thread " +  threadName + " interrupted.");
        }
        System.out.println("Thread " +  threadName + " exiting.");
    }
    
    public void start () {
        System.out.println("Starting " +  threadName );
        if (t == null) {
            t = new Thread (this, threadName);
            t.start ();
        }
    }
    }
    
    public class TestThread {
    
    public static void main(String args[]) {
        ThreadDemo T1 = new ThreadDemo( "Thread-1");
        T1.start();
        
        ThreadDemo T2 = new ThreadDemo( "Thread-2");
        T2.start();
    }   
    }
```


编译以上程序运行结果如下：




```java
Creating Thread-1
Starting Thread-1
Creating Thread-2
Starting Thread-2
Running Thread-1
Thread: Thread-1, 4
Running Thread-2
Thread: Thread-2, 4
Thread: Thread-1, 3
Thread: Thread-2, 3
Thread: Thread-1, 2
Thread: Thread-2, 2
Thread: Thread-1, 1
Thread: Thread-2, 1
Thread Thread-1 exiting.
Thread Thread-2 exiting.
```




## 6\. Thread 方法

下表列出了Thread类的一些重要方法：

| **序号**                                                     | **方法描述**                                    |
| ------------------------------------------------------------ | ----------------------------------------------- |
| 1                                                            | **public void start()**                         |
| 使该线程开始执行； **Java** 虚拟机调用该线程的 run 方法。    |                                                 |
| 2                                                            | **public void run()**                           |
| 如果该线程是使用独立的 Runnable 运行对象构造的，则调用该 Runnable 对象的 run 方法；否则，该方法不执行任何操作并返回。 |                                                 |
| 3                                                            | **public final void setName(String name)**      |
| 改变线程名称，使之与参数 name 相同。                         |                                                 |
| 4                                                            | **public final void setPriority(int priority)** |
| 更改线程的优先级。                                           |                                                 |
| 5                                                            | **public final void setDaemon(boolean on)**     |
| 将该线程标记为守护线程或用户线程。                           |                                                 |
| 6                                                            | **public final void join(long millisec)**       |
| 等待该线程终止的时间最长为 millis 毫秒。                     |                                                 |
| 7                                                            | **public void interrupt()**                     |
| 中断线程。                                                   |                                                 |
| 8                                                            | **public final boolean isAlive()**              |
| 测试线程是否处于活动状态。                                   |                                                 |

测试线程是否处于活动状态。 上述方法是被Thread对象调用的。下面的方法是Thread类的静态方法。

| **序号**                                                     | **方法描述**                                  |
| ------------------------------------------------------------ | --------------------------------------------- |
| 1                                                            | **public static void yield()**                |
| 暂停当前正在执行的线程对象，并执行其他线程。                 |                                               |
| 2                                                            | **public static void sleep(long millisec)**   |
| 在指定的毫秒数内让当前正在执行的线程休眠（暂停执行），此操作受到系统计时器和调度程序精度和准确性的影响。 |                                               |
| 3                                                            | **public static boolean holdsLock(Object x)** |
| 当且仅当当前线程在指定的对象上保持监视器锁时，才返回 true。  |                                               |
| 4                                                            | **public static Thread currentThread()**      |
| 返回对当前正在执行的线程对象的引用。                         |                                               |
| 5                                                            | **public static void dumpStack()**            |
| 将当前线程的堆栈跟踪打印至标准错误流。                       |                                               |

### 范例

如下的 ThreadClassDemo 程序演示了 Thread 类的一些方法：




```java
// 文件名 : DisplayMessage.java
// 通过实现 Runnable 接口创建线程
public class DisplayMessage implements Runnable {
    private String message;
    
    public DisplayMessage(String message) {
        this.message = message;
    }
    
    public void run() {
        while(true) {
            System.out.println(message);
        }
    }
}
```





```java
// 文件名 : GuessANumber.java
// 通过继承 Thread 类创建线程
    
public class GuessANumber extends Thread {
    private int number;
    public GuessANumber(int number) {
        this.number = number;
    }
    
    public void run() {
        int counter = 0;
        int guess = 0;
        do {
            guess = (int) (Math.random() * 100 + 1);
            System.out.println(this.getName() + " guesses " + guess);
            counter++;
        } while(guess != number);
        System.out.println("** Correct!" + this.getName() + "in" + counter + "guesses.**");
    }
}
```





```java
// 文件名 : ThreadClassDemo.java
public class ThreadClassDemo {
    
    public static void main(String [] args) {
        Runnable hello = new DisplayMessage("Hello");
        Thread thread1 = new Thread(hello);
        thread1.setDaemon(true);
        thread1.setName("hello");
        System.out.println("Starting hello thread...");
        thread1.start();
        
        Runnable bye = new DisplayMessage("Goodbye");
        Thread thread2 = new Thread(bye);
        thread2.setPriority(Thread.MIN_PRIORITY);
        thread2.setDaemon(true);
        System.out.println("Starting goodbye thread...");
        thread2.start();
    
        System.out.println("Starting thread3...");
        Thread thread3 = new GuessANumber(27);
        thread3.start();
        try {
            thread3.join();
        }catch(InterruptedException e) {
            System.out.println("Thread interrupted.");
        }
        System.out.println("Starting thread4...");
        Thread thread4 = new GuessANumber(75);
        
        thread4.start();
        System.out.println("main() is ending...");
    }
}
```


运行结果如下，每一次运行的结果都不一样。




```java
Starting hello thread...
Starting goodbye thread...
Hello
Hello
Hello
Hello
Hello
Hello
Goodbye
Goodbye
Goodbye
Goodbye
Goodbye
.......
```




## 7\. 通过 Callable 和 Future 创建线程

  * 1\. 创建 Callable 接口的实现类，并实现 call() 方法，该 call() 方法将作为线程执行体，并且有返回值。

  * 2\. 创建 Callable 实现类的范例，使用 FutureTask 类来包装 Callable 对象，该 FutureTask 对象封装了该 Callable 对象的 call() 方法的返回值。

  * 3\. 使用 FutureTask 对象作为 Thread 对象的 target 创建并启动新线程。

  * 4\. 调用 FutureTask 对象的 get() 方法来获得子线程执行结束后的返回值。

    

    
        
    
    ```java
    public class CallableThreadTest implements Callable<Integer> {
        public static void main(String[] args)  
        {  
            CallableThreadTest ctt = new CallableThreadTest();  
            FutureTask <Integer> ft = new FutureTask<>(ctt);  
            for(int i = 0;i < 100;i++)  
            {  
                System.out.println(Thread.currentThread().getName()+" 的循环变量i的值"+i);  
                if(i==20)  
                {  
                    new Thread(ft,"有返回值的线程").start();  
                }  
            }  
            try  
            {  
                System.out.println("子线程的返回值："+ft.get());  
            } catch (InterruptedException e)  
            {  
                e.printStackTrace();  
            } catch (ExecutionException e)  
            {  
                e.printStackTrace();  
            }  
    }
    @Override  
    public Integer call() throws Exception  
    {  
        int i = 0;  
        for(;i<100;i++)  
        {  
            System.out.println(Thread.currentThread().getName()+" "+i);  
        }  
        return i;  
    }  
    }
    ```
    
    



## 8\. 创建线程的三种方式的对比

  * 1\. 采用实现 Runnable、Callable 接口的方式创建多线程时，线程类只是实现了 Runnable 接口或 Callable 接口，还可以继承其他类。
  * 2\. 使用继承 Thread 类的方式创建多线程时，编写简单，如果需要访问当前线程，则无需使用 Thread.currentThread() 方法，直接使用 this 即可获得当前线程。 



## 9\. 线程的几个主要概念

在多线程编程时，你需要了解以下几个概念：

  * 线程同步
  * 线程间通信
  * 线程死锁
  * 线程控制：挂起、停止和恢复



## 10\. 多线程的使用

有效利用多线程的关键是理解程序是并发执行而不是串行执行的。例如：程序中有两个子系统需要并发执行，这时候就需要利用多线程编程。

通过对多线程的使用，可以编写出非常高效的程序。不过请注意，如果你创建太多的线程，程序执行的效率实际上是降低了，而不是提升了。

请记住，上下文的切换开销也很重要，如果你创建了太多的线程，CPU 花费在上下文的切换的时间将多于执行程序的时间！






# Java 多态



多态是同一个行为具有多个不同表现形式或形态的能力。

多态就是同一个接口，使用不同的范例而执行不同操作，如图所示：

多态性是对象多种表现形式的体现。



## 1\. 多态的优点

  * 1\. 消除类型之间的耦合关系
  * 2\. 可替换性
  * 3\. 可扩充性
  * 4\. 接口性
  * 5\. 灵活性
  * 6\. 简化性



## 2\. 多态存在的三个必要条件

  * 继承

  * 重写

  * 父类引用指向子类对象：

    

    ```java
    Parent p = new Child();
    
    class Shape {
        void draw() {}
    }
    
    class Circle extends Shape {
        void draw() {
            System.out.println("Circle.draw()");
        }
    }
    
    class Square extends Shape {
        void draw() {
            System.out.println("Square.draw()");
        }
    }
    
    class Triangle extends Shape {
        void draw() {
            System.out.println("Triangle.draw()");
        }
    }
    ```
    
    
    
    

当使用多态方式调用方法时，首先检查父类中是否有该方法，如果没有，则编译错误；如果有，再去调用子类的同名方法。

多态的好处：可以使程序有良好的扩展，并可以对所有类的对象进行通用处理。



## 3\. 多态的范例




```java
public class Test {
    public static void main(String[] args) {
      show(new Cat());  // 以 Cat 对象调用 show 方法
      show(new Dog());  // 以 Dog 对象调用 show 方法
                
      Animal a = new Cat();  // 向上转型  
      a.eat();               // 调用的是 Cat 的 eat
      Cat c = (Cat)a;        // 向下转型  
      c.work();        // 调用的是 Cat 的 work
  }  
            
    public static void show(Animal a)  {
      a.eat();  
        // 类型判断
        if (a instanceof Cat)  {  // 猫做的事情 
            Cat c = (Cat)a;  
            c.work();  
        } else if (a instanceof Dog) { // 狗做的事情 
            Dog c = (Dog)a;  
            c.work();  
        }  
    }  
}
 
abstract class Animal {  
    abstract void eat();  
}  
  
class Cat extends Animal {  
    public void eat() {  
        System.out.println("吃鱼");  
    }  
    public void work() {  
        System.out.println("抓老鼠");  
    }  
}  
  
class Dog extends Animal {  
    public void eat() {  
        System.out.println("吃骨头");  
    }  
    public void work() {  
        System.out.println("看家");  
    }  
}
```


执行以上程序，输出结果为：




```java
吃鱼
抓老鼠
吃骨头
看家
吃鱼
抓老鼠
```




## 4\. 多态的实现方式

  * 重写
  * 接口
  * 抽象类和抽象方法





# Java 条件语句 - if else

一个 if 语句包含一个布尔表达式和一条或多条语句。



## 1\. if 语句

如果布尔表达式的值为 true，则执行 if 语句中的代码块，否则执行 if 语句块后面的代码。

### 1）if 语句的语法




```java
if(布尔表达式)
{
   //如果布尔表达式为true将执行的语句
}
```


### 2）if 语句的范例




```java
public class Test {
 
   public static void main(String args[]){
      int x = 10;
 
      if( x < 20 ){
         System.out.print("这是 if 语句");
      }
   }
}
```


以上代码编译运行结果如下：




```java
这是 if 语句
```




## 2\. if...else 语句

if 语句后面可以跟 else 语句，当 if 语句的布尔表达式值为 false 时，else 语句块会被执行。

### 1）if...else 语句的语法




```java
if(布尔表达式){
   //如果布尔表达式的值为true
}else{
   //如果布尔表达式的值为false
}
```


### 2）if...else 语句的范例




```java
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
```


以上代码编译运行结果如下：




```java
这是 else 语句
```




## 3\. if...else if...else 语句

if 语句后面可以跟 else if...else 语句，这种语句可以检测到多种可能的情况。

使用 if，else if，else 语句的时候，需要注意下面几点：

  * if 语句至多有 1 个 else 语句，else 语句在所有的 else if 语句之后。
  * if 语句可以有若干个 else if 语句，它们必须在 else 语句之前。
  * 一旦其中一个 else if 语句检测为 true，其他的 else if 以及 else 语句都将跳过执行。

### 1）if...else if...else 语句的语法




```java
if(布尔表达式 1){
   //如果布尔表达式 1的值为true执行代码
}else if(布尔表达式 2){
   //如果布尔表达式 2的值为true执行代码
}else if(布尔表达式 3){
   //如果布尔表达式 3的值为true执行代码
}else {
   //如果以上布尔表达式都不为true执行代码
}
```


### 2）if...else if...else 语句的范例




```java
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
```


以上代码编译运行结果如下：




```java
Value of X is 30
```




## 4\. 嵌套的 if…else 语句

使用嵌套的 if…else 语句是合法的。也就是说你可以在另一个 if 或者 else if 语句中使用 if 或者 else if 语句。

### 1）嵌套 if…else 语句的语法




```java
if(布尔表达式 1){
   ////如果布尔表达式 1的值为true执行代码
   if(布尔表达式 2){
      ////如果布尔表达式 2的值为true执行代码
   }
}
```


你可以像 if 语句一样嵌套 else if...else。

### 2）嵌套 if…else 语句的范例




```java
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
```


以上代码编译运行结果如下：




```java
X = 30 and Y = 10
```




# Java 序列化

Java 提供了一种对象序列化的机制，该机制中，一个对象可以被表示为一个字节序列，该字节序列包括该对象的数据、有关对象的类型的信息和存储在对象中数据的类型。

将序列化对象写入文件之后，可以从文件中读取出来，并且对它进行反序列化，也就是说，对象的类型信息、对象的数据，还有对象中的数据类型可以用来在内存中新建对象。

整个过程都是 Java 虚拟机（JVM）独立的，也就是说，在一个平台上序列化的对象可以在另一个完全不同的平台上反序列化该对象。

类 ObjectInputStream 和 ObjectOutputStream 是高层次的数据流，它们包含反序列化和序列化对象的方法。

ObjectOutputStream 类包含很多写方法来写各种数据类型，但是一个特别的方法例外：




```java
public final void writeObject(Object x) throws IOExceptionpublic final void writeObject(Object x) throws IOException
```


上面的方法序列化一个对象，并将它发送到输出流。相似的 ObjectInputStream 类包含如下反序列化一个对象的方法：




```java
public final Object readObject() throws IOException, ClassNotFoundException
```


该方法从流中取出下一个对象，并将对象反序列化。它的返回值为 Object，因此，你需要将它转换成合适的数据类型。

为了演示序列化在 Java 中是怎样工作的，我将使用之前教程中提到的 Employee 类，假设我们定义了如下的 Employee
类，该类实现了Serializable 接口。




```java
public class Employee implements java.io.Serializable
{
    public String name;
    public String address;
    public transient int SSN;
    public int number;
    public void mailCheck()
    {
        System.out.println("Mailing a check to " + name
                            + " " + address);
    }
}
```


请注意，一个类的对象要想序列化成功，必须满足两个条件：

该类必须实现 java.io.Serializable 接口。

该类的所有属性必须是可序列化的。如果有一个属性不是可序列化的，则该属性必须注明是短暂的。

如果你想知道一个 Java 标准类是否是可序列化的，请查看该类的文档。检验一个类的范例是否能序列化十分简单， 只需要查看该类有没有实现
java.io.Serializable接口。



## 1\. 序列化对象

ObjectOutputStream 类用来序列化一个对象，如下的 SerializeDemo 例子范例化了一个 Employee
对象，并将该对象序列化到一个文件中。

该程序执行后，就创建了一个名为 employee.ser 文件。该程序没有任何输出，但是你可以通过代码研读来理解程序的作用。

**注意：** 当序列化一个对象到文件时， 按照 Java 的标准约定是给文件一个 .ser 扩展名。




```java
import java.io.*;

public class SerializeDemo
{
    public static void main(String [] args)
    {
        Employee e = new Employee();
        e.name = "Reyan Ali";
        e.address = "Phokka Kuan, Ambehta Peer";
        e.SSN = 11122333;
        e.number = 101;
        try
        {
            FileOutputStream fileOut =
            new FileOutputStream("/tmp/employee.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(e);
            out.close();
            fileOut.close();
            System.out.printf("Serialized data is saved in /tmp/employee.ser");
        }catch(IOException i)
        {
            i.printStackTrace();
        }
    }
}
```




## 2\. 反序列化对象

下面的 DeserializeDemo 程序范例了反序列化，/tmp/employee.ser 存储了 Employee 对象。




```java
import java.io.*;

public class DeserializeDemo
{
    public static void main(String [] args)
    {
        Employee e = null;
        try
        {
            FileInputStream fileIn = new FileInputStream("/tmp/employee.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);
            e = (Employee) in.readObject();
            in.close();
            fileIn.close();
        }catch(IOException i)
        {
            i.printStackTrace();
            return;
        }catch(ClassNotFoundException c)
        {
            System.out.println("Employee class not found");
            c.printStackTrace();
            return;
        }
        System.out.println("Deserialized Employee...");
        System.out.println("Name: " + e.name);
        System.out.println("Address: " + e.address);
        System.out.println("SSN: " + e.SSN);
        System.out.println("Number: " + e.number);
    }
}
```


以上程序编译运行结果如下所示：




```java
Deserialized Employee...
Name: Reyan Ali
Address:Phokka Kuan, Ambehta Peer
SSN: 0
Number:101
```


这里要注意以下要点：

readObject() 方法中的 try/catch 代码块尝试捕获 ClassNotFoundException 异常。对于 JVM
可以反序列化对象，它必须是能够找到字节码的类。如果JVM在反序列化对象的过程中找不到该类，则抛出一个 ClassNotFoundException 异常。

注意，readObject() 方法的返回值被转化成 Employee 引用。

当对象被序列化时，属性 SSN 的值为 111222333，但是因为该属性是短暂的，该值没有被发送到输出流。所以反序列化后 Employee 对象的 SSN
属性为 0。





+++

# Java 循环语句 - for while break continue

Java 循环语句用来在程序中重复执行某些语句。顺序结构的程序语句只能被执行一次。如果您想要同样的操作执行多次，就需要使用循环结构。

Java中有三种主要的循环结构：

  * **while** 循环
  * **do…while** 循环
  * **for** 循环



## 1\. while 循环

### 1）while 循环的语法



```java
while( 布尔表达式 ) {
  //循环内容
}
```


只要布尔表达式为 true，循环就会一直执行下去。

### 2）while 循环的范例



```java
public class Test {
   public static void main(String args[]) {
      int x = 10;
      while( x < 20 ) {
         System.out.print("value of x : " + x );
         x++;
         System.out.print("\n");
      }
   }
}
```


以上范例编译运行结果如下：



```java
value of x : 10
value of x : 11
value of x : 12
value of x : 13
value of x : 14
value of x : 15
value of x : 16
value of x : 17
value of x : 18
value of x : 19
```




## 2\. do while 循环

对于 while 语句而言，如果不满足条件，则不能进入循环。但有时候我们需要即使不满足条件，也至少执行一次。

do…while 循环和 while 循环相似，不同的是，do…while 循环至少会执行一次。

### 1）do while 循环的语法

###



```java
do {
       //代码语句
}while(布尔表达式);
```

**注意：** 布尔表达式在循环体的后面，所以语句块在检测布尔表达式之前已经执行了。 如果布尔表达式的值为 true，则语句块一直执行，直到布尔表达式的值为
false。

### 2）do while 循环的范例




```java
public class Test {
   public static void main(String args[]){
      int x = 10;
      do{
         System.out.print("value of x : " + x );
         x++;
         System.out.print("\n");
      }while( x < 20 );
   }
}
```


以上范例编译运行结果如下：



```java
value of x : 10
value of x : 11
value of x : 12
value of x : 13
value of x : 14
value of x : 15
value of x : 16
value of x : 17
value of x : 18
value of x : 19
```




## 3\. for循环

虽然所有循环结构都可以用 while 或者 do...while表示，但 Java 提供了另一种语句 —— for 循环，使一些循环结构变得更加简单。

for循环执行的次数是在执行前就确定的。

### 1）for 循环的语法



```java
for(初始化; 布尔表达式; 更新) {
    //代码语句
}
```


关于 for 循环有以下几点说明：

  * 最先执行初始化步骤。可以声明一种类型，但可初始化一个或多个循环控制变量，也可以是空语句。
  * 然后，检测布尔表达式的值。如果为 true，循环体被执行。如果为false，循环终止，开始执行循环体后面的语句。
  * 执行一次循环后，更新循环控制变量。
  * 再次检测布尔表达式。循环执行上面的过程。

### 2）for 循环的范例




```java
public class Test {
   public static void main(String args[]) {  
for(int x = 10; x < 20; x = x+1) {
         System.out.print("value of x : " + x );
         System.out.print("\n");
      }
   }
}
```


以上范例编译运行结果如下：



```java
value of x : 10
value of x : 11
value of x : 12
value of x : 13
value of x : 14
value of x : 15
value of x : 16
value of x : 17
value of x : 18
value of x : 19
```




## 4\. 增强 for 循环

Java5 引入了一种主要用于数组的增强型 for 循环。

### 1）增强 for 循环的语法



```java
for(声明语句 : 表达式)
{
   //代码句子
}
```


**声明语句：** 声明新的局部变量，该变量的类型必须和数组元素的类型匹配。其作用域限定在循环语句块，其值与此时数组元素的值相等。

**表达式：** 表达式是要访问的数组名，或者是返回值为数组的方法。

### 2）增强 for 循环的范例




```java
   public class Test {
   public static void main(String args[]){
      int [] numbers = {10, 20, 30, 40, 50};
for(int x : numbers ){
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names ={"James", "Larry", "Tom", "Lacy"};
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
```


以上范例编译运行结果如下：



```java
10,20,30,40,50,
James,Larry,Tom,Lacy,
```




## 5\. break 关键字

break 主要用在循环语句或者 switch 语句中，用来跳出整个语句块。

break 跳出最里层的循环，并且继续执行该循环下面的语句。

### 1）break 语句的语法

break 的用法很简单，就是循环结构中的一条语句：



```java
break;
```


### 2）break 语句的范例




```java
public class Test {
   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
for(int x : numbers ) {
         // x 等于 30 时跳出循环
         if( x == 30 ) {
            break;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}
```


以上范例编译运行结果如下：



```java
10
20
```




## 6\. continue 关键字

continue 适用于任何循环控制结构中。作用是让程序立刻跳转到下一次循环的迭代。

在 for 循环中，continue 语句使程序立即跳转到更新语句。

在 while 或者 do…while 循环中，程序立即跳转到布尔表达式的判断语句。

### 1）continue 语句的语法

continue 就是循环体中一条简单的语句：



```java
continue;
```


### 2）continue 语句的范例




```java
public class Test {
   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
for(int x : numbers ) {
         if( x == 30 ) {
        continue;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}
```


以上范例编译运行结果如下：



```java
10
20
40
50
```



+++

# Java 重写(Override)与重载(Overload)

Java 重写(Override)是子类对父类的允许访问的方法的实现过程进行重新编写。

Java 重载(overloading) 是在一个类里面，方法名字相同，而参数不同。



## 1\. Java 方法重写 Override

重写是子类对父类的允许访问的方法的实现过程进行重新编写, 返回值和形参都不能改变。

重写的好处在于子类可以根据需要，定义特定于自己的行为。也就是说子类能够根据需要实现父类的方法。

重写方法不能抛出新的检查异常或者比被重写方法申明更加宽泛的异常。例如： 父类的一个方法申明了一个检查异常
IOException，但是在重写这个方法的时候不能抛出 Exception 异常，因为 Exception 是 IOException 的父类，只能抛出
IOException 的子类异常。

在面向对象原则里，重写意味着可以重写任何现有方法。



### 1) Java 方法重写的范例




```java
class Animal{
   public void move(){
      System.out.println("动物可以移动");
   }
}
 
class Dog extends Animal{
   public void move(){
      System.out.println("狗可以跑和走");
   }
}
 
public class TestDog{
   public static void main(String args[]){
      Animal a = new Animal(); // Animal 对象
      Animal b = new Dog(); // Dog 对象
 
      a.move();// 执行 Animal 类的方法
 
      b.move();//执行 Dog 类的方法
   }
}
```


以上范例编译运行结果如下：




```java
动物可以移动
狗可以跑和走
```


在上面的例子中可以看到，尽管 b 属于 Animal 类型，但是它运行的是 Dog 类的 move方法。

这是由于在编译阶段，只是检查参数的引用类型。

然而在运行时，Java 虚拟机(JVM)指定对象的类型并且运行该对象的方法。

因此在上面的例子中，之所以能编译成功，是因为 Animal 类中存在 move 方法，然而运行时，运行的是特定对象的方法。

思考以下例子：




```java
class Animal{
   public void move(){
      System.out.println("动物可以移动");
   }
}
 
class Dog extends Animal{
   public void move(){
      System.out.println("狗可以跑和走");
   }
   public void bark(){
      System.out.println("狗可以吠叫");
   }
}
 
public class TestDog{
   public static void main(String args[]){
      Animal a = new Animal(); // Animal 对象
      Animal b = new Dog(); // Dog 对象
 
      a.move();// 执行 Animal 类的方法
      b.move();//执行 Dog 类的方法
      b.bark();
   }
}
```


以上范例编译运行结果如下：




```java
TestDog.java:30: cannot find symbol
symbol  : method bark()
location: class Animal
                b.bark();
                 ^
```


该程序将抛出一个编译错误，因为b的引用类型Animal没有bark方法。



### 2）Java 方法重写的规则

  * 参数列表与被重写方法的参数列表必须完全相同。
  * 返回类型与被重写方法的返回类型可以不相同，但是必须是父类返回值的派生类（java5 及更早版本返回类型要一样，java7 及更高版本可以不同）。
  * 访问权限不能比父类中被重写的方法的访问权限更低。例如：如果父类的一个方法被声明为 public，那么在子类中重写该方法就不能声明为 protected。
  * 父类的成员方法只能被它的子类重写。
  * 声明为 final 的方法不能被重写。
  * 声明为 static 的方法不能被重写，但是能够被再次声明。
  * 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为 private 和 final 的方法。
  * 子类和父类不在同一个包中，那么子类只能够重写父类的声明为 public 和 protected 的非 final 方法。
  * 重写的方法能够抛出任何非强制异常，无论被重写的方法是否抛出异常。但是，重写的方法不能抛出新的强制性异常，或者比被重写方法声明的更广泛的强制性异常，反之则可以。
  * 构造方法不能被重写。
  * 如果不能继承一个类，则不能重写该类的方法。



### 3) Super 关键字的使用

当需要在子类中调用父类的被重写方法时，要使用 super 关键字。




```java
class Animal{
   public void move(){
      System.out.println("动物可以移动");
   }
}
 
class Dog extends Animal{
   public void move(){
      super.move(); // 应用super类的方法
      System.out.println("狗可以跑和走");
   }
}
 
public class TestDog{
   public static void main(String args[]){
 
      Animal b = new Dog(); // Dog 对象
      b.move(); //执行 Dog类的方法
 
   }
}
```


以上范例编译运行结果如下：




```java
动物可以移动
狗可以跑和走
```




## 2\. Java 方法重载 Overload

重载(overloading) 是在一个类里面，方法名字相同，而参数不同。返回类型可以相同也可以不同。

每个重载的方法（或者构造函数）都必须有一个独一无二的参数类型列表。

最常用的地方就是构造器的重载。

**重载规则:**

  * 被重载的方法必须改变参数列表(参数个数或类型不一样)；
  * 被重载的方法可以改变返回类型；
  * 被重载的方法可以改变访问修饰符；
  * 被重载的方法可以声明新的或更广的检查异常；
  * 方法能够在同一个类中或者在一个子类中被重载。
  * 无法以返回值类型作为重载函数的区分标准。 



### 1）Java 方法重载的范例




```java
public class Overloading {
    public int test(){
        System.out.println("test1");
        return 1;
    }
 
    public void test(int a){
        System.out.println("test2");
    }   
 
    //以下两个参数类型顺序不同
    public String test(int a,String s){
        System.out.println("test3");
        return "returntest3";
    }   
 
    public String test(String s,int a){
        System.out.println("test4");
        return "returntest4";
    }   
 
    public static void main(String[] args){
        Overloading o = new Overloading();
        System.out.println(o.test());
        o.test(1);
        System.out.println(o.test(1,"test3"));
        System.out.println(o.test("test4",1));
    }
}
```




### 2）Java 重写与重载之间的区别

| 区别点   | 重载方法 | 重写方法                                       |
| -------- | -------- | ---------------------------------------------- |
| 参数列表 | 必须修改 | 一定不能修改                                   |
| 返回类型 | 可以修改 | 一定不能修改                                   |
| 异常     | 可以修改 | 可以减少或删除，一定不能抛出新的或者更广的异常 |
| 访问     | 可以修改 | 一定不能做更严格的限制（可以降低限制）         |



## 3\. Java 方法的重写和重载

Java 方法的重写(Overriding)和重载(Overloading)是 Java
多态性的不同表现，重写是父类与子类之间多态性的一种表现，重载可以理解成多态的具体表现形式。

  * 方法重载是一个类中定义了多个方法名相同,而他们的参数的数量不同或数量相同而类型和次序不同,则称为方法的重载(Overloading)。
  * 方法重写是在子类存在方法与父类的方法的名字相同,而且参数的个数与类型一样,返回值也一样的方法,就称为重写(Overriding)。
  * 方法重载是一个类的多态性表现,而方法重写是子类与父类的一种多态性表现。



