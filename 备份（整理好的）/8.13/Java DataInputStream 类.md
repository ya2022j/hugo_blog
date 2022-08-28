+++
title = "Java DataInputStream 类"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java DataInputStream 类<

数据输入流允许应用程序以与机器无关方式从底层输入流中读取基本 Java 数据类型。



## 1\. DataInputStream 创建方式

下面的构造方法用来创建数据输入流对象。

    
    
    DataInputStream dis = new DataInputStream(InputStream in);
    



## 2\. DataInputStream 操作方法

序号 | 方法描述  
---|---  
1 | **public final int read(byte[] r, int off, int len)throws IOException**  
从所包含的输入流中将 len 个字节读入一个字节数组中。如果len为-1，则返回已读字节数。  
2 | **Public final int read(byte [] b)throws IOException**  
从所包含的输入流中读取一定数量的字节，并将它们存储到缓冲区数组 b 中。  
3 | **public final Boolean readBooolean()throws IOException**  
从所包含的输入流中读取一个布尔型数据。  
4 | **public final byte readByte()throws IOException**  
从所包含的输入流中读取一个字节数据。  
5 | **public final short readShort()throws IOException**  
从所包含的输入流中读取一个短整型数据。  
6 | **public final Int readInt()throws IOException**  
从所包含的输入流中读取一个整型数据。  
7 | **public String readLine() throws IOException**  
从输入流中读取下一文本行。  
  


## 3\. DataInputStream 范例

下面的例子演示了DataInputStream和DataOutputStream的使用，该例从文本文件test.txt中读取5行，并转换成大写字母，最后保存在另一个文件test1.txt中。

test.txt 文件内容如下：

    
    
    codebaoku1
    codebaoku2
    codebaoku3
    codebaoku4
    codebaoku5
    
    
    
    import java.io.*;
    
    public class Test{
        public static void main(String args[])throws IOException{
        
            DataInputStream in = new DataInputStream(new FileInputStream("test.txt"));
            DataOutputStream out = new DataOutputStream(new  FileOutputStream("test1.txt"));
            BufferedReader d  = new BufferedReader(new InputStreamReader(in));
            
            String count;
            while((count = d.readLine()) != null){
                String u = count.toUpperCase();
                System.out.println(u);
                out.writeBytes(u + "  ,");
            }
            d.close();
            out.close();
        }
    }
    

以上实例编译运行结果如下：

    
    
    CODEBAOKU1
    CODEBAOKU2
    CODEBAOKU3
    CODEBAOKU4
    CODEBAOKU5
    

