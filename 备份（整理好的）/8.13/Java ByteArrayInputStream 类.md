+++
title = "Java ByteArrayInputStream 类"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java ByteArrayInputStream 类

ByteArrayInputStream 字节数组输入流在内存中创建一个字节数组缓冲区，从输入流读取的数据保存在该字节数组缓冲区中。



## 1\. ByteArrayInputStream 创建方式

创建字节数组输入流对象有以下几种方式。

接收字节数组作为参数创建：

    
    
    ByteArrayInputStream bArray = new ByteArrayInputStream(byte [] a);
    

另一种创建方式是接收一个字节数组，和两个整形变量 off、len，off表示第一个读取的字节，len表示读取字节的长度。

    
    
    ByteArrayInputStream bArray = new ByteArrayInputStream(byte []a, int off, int len)
    



## 2\. ByteArrayInputStream 操作方法

成功创建字节数组输入流对象后，可以参见以下列表中的方法，对流进行读操作或其他操作。

序号 | 方法描述  
---|---  
1 | **public int read()         **  
从此输入流中读取下一个数据字节。  
2 | **public int read(byte[] r, int off, int len)**  
将最多 len 个数据字节从此输入流读入字节数组。  
3 | **public int available()**  
返回可不发生阻塞地从此输入流读取的字节数。  
4 | **public void mark(int read)**  
设置流中的当前标记位置。  
5 | **public long skip(long n)**  
从此输入流中跳过 n 个输入字节。  
  


## 3\. ByteArrayInputStream 范例

下面的例子演示了ByteArrayInputStream 和 ByteArrayOutputStream的使用：

    
    
    import java.io.*;
    
    public class ByteStreamTest {
    
       public static void main(String args[])throws IOException {
    
          ByteArrayOutputStream bOutput = new ByteArrayOutputStream(12);
    
          while( bOutput.size()!= 10 ) {
             // 获取用户输入值
             bOutput.write(System.in.read());
          }
    
          byte b [] = bOutput.toByteArray();
          System.out.println("Print the content");
          for(int x= 0 ; x < b.length; x++) {
             // 打印字符
             System.out.print((char)b[x]  + "   ");
          }
          System.out.println("   ");
    
          int c;
    
          ByteArrayInputStream bInput = new ByteArrayInputStream(b);
    
          System.out.println("Converting characters to Upper case " );
          for(int y = 0 ; y < 1; y++ ) {
             while(( c= bInput.read())!= -1) {
                System.out.println(Character.toUpperCase((char)c));
             }
             bInput.reset();
          }
       }
    }
    

以上实例编译运行结果如下：

    
    
    asdfghjkly
    Print the content
    a   s   d   f   g   h   j   k   l   y
    Converting characters to Upper case
    A
    S
    D
    F
    G
    H
    J
    K
    L
    Y
    

