+++
title = "Java 数据类型"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
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

    
            double   d1  = 7D ;
        double   d2  = 7.; 
        double   d3  =  8.0; 
        double   d4  =  8.D; 
        double   d5  =  12.9867; 
        

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
    

编译以上代码输出结果如下所示：

    
    
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
    

Float和Double的最小值和最大值都是以科学记数法的形式输出的，结尾的"E+数字"表示E之前的数字要乘以10的多少次方。比如3.14E3就是3.14
× 103 =3140，3.14E-3 就是 3.14 x 10-3 =0.00314。

实际上，JAVA中还存在另外一种基本类型 void，它也有对应的包装类 java.lang.Void，不过我们无法直接对它们进行操作。



## 3\. Java 数据类型转换

##

### 1）自动数据类型转换

**整型、实型（常量）、字符型数据可以混合运算。运算中，不同类型的数据先转化为同一类型，然后进行运算。**

转换从低级到高级。

    
    
    低  ------------------------------------>  高
    
    byte,short,char—> int —> long—> float —> double 
    

数据类型转换必须满足如下规则：

  * 1\. 不能对boolean类型进行类型转换。
  * 2\. 不能把对象类型转换成不相关类的对象。
  * 3\. 在把容量大的类型转换为容量小的类型时必须使用强制类型转换。
  * 4\. 转换过程中可能导致溢出或损失精度，例如：  

    
        int i = 128;   
    byte b = (byte)i;
    

因为 byte 类型是 8 位，最大值为127，所以当 int 强制转换为 byte 类型时，值 128 时候就会导致溢出。

  * 5\. 浮点数到整数的转换是通过舍弃小数得到，而不是四舍五入，例如：   

    
        (int)23.7 == 23;        
    (int)-45.89f == -45
    

### 2）强制数据类型转换

  * 1\. 条件是转换的数据类型必须是兼容的。
  * 2\. 格式：(type)value，其中 type 是要强制类型转换后的数据类型。  

    
        public class QiangZhiZhuanHuan{
        public static void main(String[] args){
            int i1 = 123;
            byte b = (byte)i1;//强制类型转换为byte
            System.out.println("int强制类型转换为byte后的值等于"+b);
        }
    }
    

运行结果：

    
        int强制类型转换为byte后的值等于123
    

### 3）隐含强制类型转换

  * 1\. 整数的默认类型是 int。
  * 2\. 浮点型不存在这种情况，因为在定义 float 类型时必须在数字后面跟上 F 或者 f。

