+++
title = "JDBC 连接数据库步骤"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 连接数据库步骤

建立一个 JDBC 数据库连接共有四个步骤：

  * **导入 JDBC 包：**  添加 import 语句到 Java 程序导入所需的类在 Java 代码中。
  * **注册 JDBC 驱动程序：** 这一步会导致 JVM 加载所需的驱动程序实现到内存中，因此它可以实现 JDBC 请求。
  * **制定数据库 URL：** 这是创建格式正确的地址指向到要连接的数据库。
  * **创建连接对象：** 最后，代码调用 DriverManager 对象的 getConnection() 方法来建立实际的数据库连接。



## 1\. 导入 JDBC 包

import 语句告诉Java编译器在哪里可以找到在代码中引用，并放置在您的源代码最开始的类。

使用标准的JDBC包，它允许选择，插入，更新和SQL表中删除数据，添加以下进口到您的源代码：

    
    
    import java.sql.* ;  // for standard JDBC programs
    import java.math.* ; // for BigDecimal and BigInteger support
    



## 2\. 注册 JDBC 驱动程序

使用 JDBC 创建连接之前，必须在程序中注册驱动程序。注册过程只能一次，可以通过以下两种方式之一注册一个驱动程序。

### **1）Class.forName()：**

注册一个驱动程序中最常用的方法是使用 Java 的 Class.forName()
方法来动态加载驱动程序的类文件到内存中，它会自动将其注册。这种方法是可取的，因为它允许使驱动注册配置，便于携带。

下面的示例使用 Class.forName() 来注册 Oracle 驱动程序：

    
    
    try {
       Class.forName("oracle.jdbc.driver.OracleDriver");
    }
    catch(ClassNotFoundException ex) {
       System.out.println("Error: unable to load driver class!");
       System.exit(1);
    }
    

可以使用 getInstance() 方法来解决不兼容的JVM，但要编写了两个额外的例外情况如下：

    
    
    try {
       Class.forName("oracle.jdbc.driver.OracleDriver").newInstance();
    }
    catch(ClassNotFoundException ex) {
       System.out.println("Error: unable to load driver class!");
       System.exit(1);
    catch(IllegalAccessException ex) {
       System.out.println("Error: access problem while loading!");
       System.exit(2);
    catch(InstantiationException ex) {
       System.out.println("Error: unable to instantiate driver!");
       System.exit(3);
    }
    

### 2）DriverManager.registerDriver()：

第二种注册驱动程序的方法是使用 static DriverManager.registerDriver() 方法。

下面的示例使用 registerDriver() 来注册Oracle驱动程序：

    
    
    try {
       Driver myDriver = new oracle.jdbc.driver.OracleDriver();
       DriverManager.registerDriver( myDriver );
    }
    catch(ClassNotFoundException ex) {
       System.out.println("Error: unable to load driver class!");
       System.exit(1);
    }



## 3\. 制定数据库 URL

当加载驱动程序完成后，可以使用 DriverManager.getConnection() 方法获得连接。为方便参考，我们列出了三个重载
DriverManager.getConnection() 方法：

  * getConnection(String url)

  * getConnection(String url, Properties prop)

  * getConnection(String url, String user, String password)

在这里，每个方法都需要一个数据库 URL，它指向数据库地址。

下表列出了常用 JDBC 驱动程序名和数据库的 URL。

RDBMS | JDBC驱动程序的名称 | URL 格式  
---|---|---  
MySQL | com.mysql.jdbc.Driver | jdbc:mysql://hostname:port/databaseName  
ORACLE | oracle.jdbc.driver.OracleDriver |
jdbc:oracle:thin:@hostname:port:databaseName  
DB2 | COM.ibm.db2.jdbc.net.DB2Driver | **jdbc:db2:**
hostname:port/databaseName  
Sybase | com.sybase.jdbc.SybDriver | **jdbc:sybase:Tds:**
hostname:port/databaseName  
  


## 3\. 创建连接对象

### 1）使用数据库URL的用户名和密码：

getConnection() 最常用的形式是 getConnection(String url, String user, String
password)，要求传递数据库 URL，用户名 username和密码 password。

假设有一台主机TCP/IP地址 192.0.0.1 以及主机名和 Oracle 监听器被配置为在端口 1521，数据库名称是 EMP，然后完整的数据库
URL 是：

    
    
    jdbc:oracle:thin:@192.0.0.1:1521:EMP
    

通过 URL、username 和 password 三个参数来获得一个 Connection 对象：

    
    
    String URL = "jdbc:oracle:thin:@192.0.0.1:1521:EMP";
    String USER = "username";
    String PASS = "password"
    Connection conn = DriverManager.getConnection(URL, USER, PASS);
    

### 2）只使用一个数据库 URL 的调用方式

    
    
    DriverManager.getConnection(String url);
    

通过一个参数来获得一个 Connection 对象，在这种情况下，数据库的 URL 中包含用户名和密码：

    
    
    jdbc:oracle:driver:username/password@database
    

所以上面的连接可以创建如下：

    
    
    String URL = "jdbc:oracle:thin:username/password@192.0.0.1:1521:EMP";
    Connection conn = DriverManager.getConnection(URL);
    

### 3）使用数据库 URL 和 Properties 对象的调用方式

    
    
    DriverManager.getConnection(String url, Properties info);
    

Properties 对象用来保存一组键值对，调用 getConnection() 方法时，将键值对传递给驱动程序。

    
    
    import java.util.*;
    String URL = "jdbc:oracle:thin:@192.0.0.1:1521:EMP";
    Properties info = new Properties( );
    info.put( "user", "username" );
    info.put( "password", "password" );
    
    Connection conn = DriverManager.getConnection(URL, info);
    



## 4\. 关闭 JDBC 连接

在JDBC程序的结束，需要关闭所有的数据库连接，以结束数据库会话。但是，如果不关闭的话，Java
垃圾收集器会关闭连接，并清除旧对象。但依托垃圾收集，特别是在数据库编程，是非常差的编程习惯，应该显式地关闭数据库连接。为了确保连接被关闭，可以在代码中的
finally 块执行。

要关闭上面打开的连接，应该调用close()方法，如下所示：

    
    
    conn.close();
    

显式地关闭连接，可以节约系统资源。

