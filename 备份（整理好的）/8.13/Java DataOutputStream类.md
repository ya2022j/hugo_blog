+++
title = "Java DataOutputStream类"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java DataOutputStream类

数据输出流允许应用程序以与机器无关方式将Java基本数据类型写到底层输出流。



## 1\. DataOutputStream 创建方式

下面的构造方法用来创建数据输出流对象。

    
    
    DataOutputStream out = new DataOutputStream(OutputStream  out);
    



## 2\. DataOutputStream 操作方法

创建对象成功后，可以参照以下列表给出的方法，对流进行写操作或者其他操作。

序号 | 方法描述  
---|---  
1 | **public final void write(byte[] w, int off, int len)throws IOException**  
将指定字节数组中从偏移量 off 开始的 len 个字节写入此字节数组输出流。  
2 | **Public final int write(byte [] b)throws IOException**  
将指定的字节写入此字节数组输出流。  
3 | **public final void writeBooolean()throws IOException**  
写入一个布尔型数据到输出流。  
4 | **public final void writeByte()throws IOException**  
写入一个字节数据到输出流。  
5 | **public final void writeShort()throws IOException**  
写入一个短整型数据到输出流。  
6 | **public final void writeInt()throws IOException**  
写入一个整型数据到输出流。  
7 | **Public void flush()throws IOException**  
刷新此输出流并强制写出所有缓冲的输出字节。  
8 | **public final void writeBytes(String s) throws IOException**  
将字符串以字节序列写入到底层的输出流，字符串中每个字符都按顺序写入，并丢弃其高八位。  
  


## 3\. DataOutputStream 操作范例

下面的例子演示了 DataInputStream 和 DataOutputStream的使用，该例从文本文件 test.txt
中读取5行，并转换成大写字母，最后保存在另一个文件 test1.txt中。

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
    

