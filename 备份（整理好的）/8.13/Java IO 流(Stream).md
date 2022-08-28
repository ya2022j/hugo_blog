+++
title = "Java IO 流(Stream)"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java IO 流(Stream)

Java.io 包几乎包含了所有与输入、输出操作相关的类。所有这些流类 Stream 代表了输入源和输出目标。

Java.io 包中的流支持很多种格式，比如：基本类型、对象等。一个流可以理解为一个数据的序列。输入流表示从一个源读取数据，输出流表示向一个目标写数据。

Java 为 I/O 提供了强大的而灵活的支持，使其更广泛地应用到文件传输和网络编程中。



## 1\. Java IO 输入输出流的类层次图



## 2\. 读取控制台输入

Java 的控制台输入由 System.in 完成。

为了获得一个绑定到控制台的字符流，你可以把 System.in 包装在一个 BufferedReader 对象中来创建一个字符流。

### 1）创建 BufferedReader

创建 BufferedReader 的语法：

    
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    

BufferedReader 对象创建后，我们便可以使用 read() 方法从控制台读取一个字符，或者用 readLine() 方法读取一个字符串。

### 2）从控制台读取多字符输入

从 BufferedReader 对象读取一个字符要使用 read() 方法，它的语法如下：

    
    
    int read( ) throws IOException
    

每次调用 read() 方法，它从输入流读取一个字符并把该字符作为整数值返回。 当流结束的时候返回 -1。该方法抛出 IOException。

下面的程序示范了用 read() 方法从控制台不断读取字符直到用户输入 q。

    
    
    //使用 BufferedReader 在控制台读取字符
    
    import java.io.*;
        
    public class BRRead {
        public static void main(String[] args) throws IOException {
            char c;
            // 使用 System.in 创建 BufferedReader
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("输入字符, 按下 'q' 键退出。");
            // 读取字符
            do {
                c = (char) br.read();
                System.out.println(c);
            } while (c != 'q');
        }
    }
    

以上范例编译运行结果如下:

    
    
    输入字符, 按下 'q' 键退出。
    test
    t
    e
    s
    t
    
    q
    q
    

### 3）从控制台读取字符串

从标准输入读取一个字符串需要使用 BufferedReader 的 readLine() 方法。

它的一般格式是：

    
    
    String readLine( ) throws IOException    
    

下面的程序读取和显示字符行直到你输入了单词"end"。

    
    
    //使用 BufferedReader 在控制台读取字符
    import java.io.*;
        
    public class BRReadLines {
        public static void main(String[] args) throws IOException {
            // 使用 System.in 创建 BufferedReader
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String str;
            System.out.println("Enter lines of text.");
            System.out.println("Enter 'end' to quit.");
            do {
                str = br.readLine();
                System.out.println(str);
            } while (!str.equals("end"));
        }
    }
    

以上范例编译运行结果如下:

    
    
    Enter lines of text.
    Enter 'end' to quit.
    This is line one
    This is line one
    This is line two
    This is line two
    end
    end
    

> JDK 5 后的版本我们也可以使用 Java Scanner 类来获取控制台的输入。



## 3\. 从控制台输出

控制台的输出由 print( ) 和 println() 完成。这些方法都由类 PrintStream 定义，System.out 是该类对象的一个引用。

PrintStream 继承了 OutputStream类，并且实现了方法 write()。这样，write() 也可以用来往控制台写操作。

PrintStream 定义 write() 的最简单格式如下所示：

    
    
    void write(int byteval)
    

该方法将 byteval 的低八位字节写到流中。

### 1) 输出单个字符

下面的例子用 write() 把字符 "A" 和紧跟着的换行符输出到屏幕：

    
    
    import java.io.*;
     
    //演示 System.out.write().
    public class WriteDemo {
        public static void main(String[] args) {
            int b;
            b = 'A';
            System.out.write(b);
            System.out.write('\n');
        }
    }
    

运行以上范例在输出窗口输出 "A" 字符

    
    
    A
    

**注意：** write() 方法不经常使用，因为 print() 和 println() 方法用起来更为方便。

### 2) 输出字符串

在 java 中，System.out.println() 是我们经常会用到的一个语句，它的作用是将内容输出在控制台，常用于打印调试信息。除了
System.out.println() 之外，还有其他的打印结果的方法。

System.out.print()，这个方法与 System.out.println() 很像，区别就在于，System.out.println()
会在标准的输出中显示文字后换行，System.out.print() 输出文字后不会换行。

例如：输出两行字符串。

    
    
    System.out.println("HelloWord One-------");
    System.out.println("HelloWord Two-------");
    

