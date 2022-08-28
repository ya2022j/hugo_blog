+++
title = "Java 日期时间"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java 日期时间

java.util 包提供了 Date 类来封装当前的日期和时间。

java.util 包提供了 Calendar 类用来设置和获取日期数据的特定部分。

另外，还提供了 SimpleDateFormat 类来格式化日期的格式。



## 1\. Date 类

### 1）Date 类的创建

Date 类提供两个构造函数来范例化 Date 对象。

第一个构造函数使用当前日期和时间来初始化对象。

    
    
    Date()
    

第二个构造函数接收一个参数，该参数是从1970年1月1日起的毫秒数。

    
    
    Date(long millisec)
    

### 2）Date 类的操作

Date对象创建以后，可以调用下面的方法。

序号 |  方法和描述  
---|---  
1 |  **boolean after(Date date)**  
若当调用此方法的Date对象在指定日期之后返回true,否则返回false。  
2 |  **boolean before(Date date)**  
若当调用此方法的Date对象在指定日期之前返回true,否则返回false。  
3 |  **Object clone( )**  
返回此对象的副本。  
4 |  **int compareTo(Date date)**  
比较当调用此方法的Date对象和指定日期。两者相等时候返回0。调用对象在指定日期之前则返回负数。调用对象在指定日期之后则返回正数。  
5 |  **int compareTo(Object obj)**  
若obj是Date类型则操作等同于compareTo(Date) 。否则它抛出ClassCastException。  
6 |  **boolean equals(Object date)**  
当调用此方法的Date对象和指定日期相等时候返回true,否则返回false。  
7 |  **long getTime( )**  
返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 Date 对象表示的毫秒数。  
8 |  **int hashCode( )**  
 返回此对象的哈希码值。  
9 |  **void setTime(long time)**  
  
用自1970年1月1日00:00:00 GMT以后time毫秒数设置时间和日期。  
10 |  **String toString( )**  
把此 Date 对象转换为以下形式的 String： dow mon dd hh:mm:ss zzz yyyy 其中： dow 是一周中的某一天 (Sun,
Mon, Tue, Wed, Thu, Fri, Sat)。  
  
### 3）获取当前日期时间

Java中获取当前日期和时间很简单，使用 Date 对象的 toString() 方法来打印当前日期和时间：

    
    
    import java.util.Date;
      
    public class DateDemo {
       public static void main(String args[]) {
           // 初始化 Date 对象
           Date date = new Date();
            
           // 使用 toString() 函数显示日期时间
           System.out.println(date.toString());
       }
    }
    

以上范例编译运行结果如下:

    
    
    Mon May 04 09:51:52 CDT 2013
    

### 4）日期比较

Java使用以下三种方法来比较两个日期：

  * 使用 getTime() 方法获取两个日期（自1970年1月1日经历的毫秒数值），然后比较这两个值。
  * 使用方法 before()，after() 和 equals()。例如，一个月的12号比18号早，则 new Date(99, 2, 12).before(new Date (99, 2, 18)) 返回true。
  * 使用 compareTo() 方法，它是由 Comparable 接口定义的，Date 类实现了这个接口。



## 2\. SimpleDateFormat 类

SimpleDateFormat 是一个以语言环境敏感的方式来格式化和分析日期的类。SimpleDateFormat
允许你选择任何用户自定义日期时间格式来运行。

### 1）SimpleDateFormat 类使用案例

    
    
    import  java.util.*;
    import java.text.*;
     
    public class DateDemo {
       public static void main(String args[]) {
     
          Date dNow = new Date( );
          SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
     
          System.out.println("当前时间为: " + ft.format(dNow));
       }
    }
    

代码说明:

    
    
    SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");
    

这一行代码确立了转换的格式，其中 yyyy 是完整的公元年，MM 是月份，dd 是日期，HH:mm:ss 是时、分、秒。

**注意** :有的格式大写，有的格式小写，例如 MM 是月份，mm 是分；HH 是 24 小时制，而 hh 是 12 小时制。

以上范例编译运行结果如下:

    
    
    当前时间为: 2018-09-06 10:16:34
    

### 2）日期和时间的格式化编码

时间模式字符串用来指定时间格式。在此模式中，所有的 ASCII 字母被保留为模式字母，定义如下：

**字母** |  **描述** |  **示例**  
---|---|---  
G |  纪元标记 |  AD  
y |  四位年份 |  2001  
M |  月份 |  July or 07  
d |  一个月的日期 |  10  
h |   A.M./P.M. (1~12)格式小时 |  12  
H |  一天中的小时 (0~23) |  22  
m |  分钟数 |  30  
s |  秒数 |  55  
S |  毫秒数 |  234  
E |  星期几 |  Tuesday  
D |  一年中的日子 |  360  
F |  一个月中第几周的周几 |  2 (second Wed. in July)  
w |  一年中第几周 |  40  
W |  一个月中第几周 |  1  
a |  A.M./P.M. 标记 |  PM  
k |  一天中的小时(1~24) |  24  
K |   A.M./P.M. (0~11)格式小时 |  10  
z |  时区 |  Eastern Standard Time  
' |  文字定界符 |  Delimiter  
" |  单引号 |  `  
  
### 3）解析字符串为时间

SimpleDateFormat 类有一些附加的方法，特别是parse()，它试图按照给定的SimpleDateFormat
对象的格式化存储来解析字符串。例如：

    
    
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
    

以上范例编译运行结果如下:

    
    
    $ java DateDemo
    1818-11-11 Parses as Wed Nov 11 00:00:00 GMT 1818
    $ java DateDemo 2007-12-01
    2007-12-01 Parses as Sat Dec 01 00:00:00 GMT 2007
    



## 3\. Calendar类

我们现在已经能够格式化并创建一个日期对象了，但是我们如何才能设置和获取日期数据的特定部分呢，比如说小时，日，或者分钟?
我们又如何在日期的这些部分加上或者减去值呢? 答案是使用Calendar 类。

Calendar类的功能要比Date类强大很多，而且在实现方式上也比Date类要复杂一些。

Calendar类是一个抽象类，在实际使用时实现特定的子类的对象，创建对象的过程对程序员来说是透明的，只需要使用getInstance方法创建即可。

### 1）创建一个代表系统当前日期的Calendar对象

    
    
    Calendar c = Calendar.getInstance();//默认是当前日期
    

### 2）创建一个指定日期的Calendar对象

使用Calendar类代表特定的时间，需要首先创建一个Calendar的对象，然后再设定该对象中的年月日参数来完成。

    
    
    //创建一个代表2009年6月12日的Calendar对象
    Calendar c1 = Calendar.getInstance();
    c1.set(2009, 6 - 1, 12);
    

### 3）Calendar类对象字段类型

Calendar类中用以下这些常量表示不同的意义，jdk内的很多类其实都是采用的这种思想

常量| 描述  
---|---  
Calendar.YEAR| 年份  
Calendar.MONTH| 月份  
Calendar.DATE| 日期  
Calendar.DAY_OF_MONTH| 日期，和上面的字段意义完全相同  
Calendar.HOUR| 12小时制的小时  
Calendar.HOUR_OF_DAY| 24小时制的小时  
Calendar.MINUTE| 分钟  
Calendar.SECOND| 秒  
Calendar.DAY_OF_WEEK| 星期几  
  
### 4）Calendar类对象信息的设置

**Set设置**

如：

    
    
    Calendar c1 = Calendar.getInstance();

调用：

    
    
    public final void set(int year,int month,int date)
    
    
    
    c1.set(2009, 6, 12);//把Calendar对象c1的年月日分别设这为：2009、6、12
    

利用字段类型设置

如果只设定某个字段，例如日期的值，则可以使用如下set方法：

    
    
    public void set(int field,int value)

把 c1对象代表的日期设置为10号，其它所有的数值会被重新计算

    
    
    c1.set(Calendar.DATE,10);
    

把c1对象代表的年份设置为2008年，其他的所有数值会被重新计算

    
    
    c1.set(Calendar.YEAR,2008);
    

其他字段属性set的意义以此类推

**Add设置**

    
    
    Calendar c1 = Calendar.getInstance();
    

把c1对象的日期加上10，也就是c1也就表示为10天后的日期，其它所有的数值会被重新计算

    
    
    c1.add(Calendar.DATE, 10);
    

把c1对象的日期减去10，也就是c1也就表示为10天前的日期，其它所有的数值会被重新计算

    
    
    c1.add(Calendar.DATE, -10);

其他字段属性的add的意义以此类推

### 5）Calendar类对象信息的获得

    
    
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
    

