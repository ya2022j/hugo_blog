+++
title = "JDBC 异常处理"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 异常处理

异常处理，是指可以在一个受控制的方式处理异常情况，如程序定义的错误。

当异常情况发生时，将引发异常，控制被重定向到适用的 catch 子句。如果没有适用 catch 子句存在，那么程序的执行结束。

JDBC 的异常处理非常类似于 Java Excpetion 处理，但对于 JDBC，最常见的异常处理的是
**java.sql.SQLException。**



## 1\. SQLException 方法

SQLException 对象可用于检索有关异常的附加信息：

方法 | 描述  
---|---  
getErrorCode( ) | 获取与异常关联的错误号。  
getMessage( ) | 获取JDBC驱动程序的错误消息由驱动程序处理错误或获取Oracle错误号和消息的一个数据库错误。  
getSQLState( ) | 获取XOPEN
SQLSTATE字符串。对于JDBC驱动程序的错误，没有有用的信息从该方法返回。对于一个数据库错误，则返回五位XOPEN
SQLSTATE代码。这种方法可以返回null。  
getNextException() | 获取异常链的下一个Exception对象。  
printStackTrace( ) | 打印当前的异常，或者抛出，其回溯到标准错误流。  
printStackTrace(PrintStream s) | 打印此抛出，其回溯到指定的打印流。  
printStackTrace(PrintWriter w) | 打印此抛出，其回溯到指定的打印写入。  
  


## 2\. JDBC 异常处理方法

利用可从 Exception 对象捕获异常的信息，并适当地继续运行程序。

这里是一个 try块的一般形式为：

    
    
    try {
    // Your risky code goes between these curly braces!!!
    }
    catch(Exception ex) {
    // Your exception handling code goes between these 
    // curly braces, similar to the exception clause 
    // in a PL/SQL block.
    }
    finally {
    // Your must-always-be-executed code goes between these 
    // curly braces. Like closing database connection.
    }

例如：

    
    
    /STEP 1. Import required packages
    import java.sql.*;
    
    public class JDBCExample {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/EMP";
    
    //  Database credentials
    static final String USER = "username";
    static final String PASS = "password";
    
    public static void main(String[] args) {
    Connection conn = null;
    try{
    //STEP 2: Register JDBC driver
    Class.forName("com.mysql.jdbc.Driver");
    
    //STEP 3: Open a connection
    System.out.println("Connecting to database...");
    conn = DriverManager.getConnection(DB_URL,USER,PASS);
    
    //STEP 4: Execute a query
    System.out.println("Creating statement...");
    Statement stmt = conn.createStatement();
    String sql;
    sql = "SELECT id, first, last, age FROM Employees";
    ResultSet rs = stmt.executeQuery(sql);
    
    //STEP 5: Extract data from result set
    while(rs.next()){
    //Retrieve by column name
    int id  = rs.getInt("id");
    int age = rs.getInt("age");
    String first = rs.getString("first");
    String last = rs.getString("last");
    
    //Display values
    System.out.print("ID: " + id);
    System.out.print(", Age: " + age);
    System.out.print(", First: " + first);
    System.out.println(", Last: " + last);
    }
    //STEP 6: Clean-up environment
    rs.close();
    stmt.close();
    conn.close();
    }catch(SQLException se){
    //Handle errors for JDBC
    se.printStackTrace();
    }catch(Exception e){
    //Handle errors for Class.forName
    e.printStackTrace();
    }finally{
    //finally block used to close resources
    try{
    if(conn!=null)
    conn.close();
    }catch(SQLException se){
    se.printStackTrace();
    }//end finally try
    }//end try
    System.out.println("Goodbye!");
    }//end main
    }//end JDBCExample

现在让我们来编译上面的例子如下：

    
    
    C:>javac JDBCExample.java
    C:>

当运行JDBCExample，如果没有问题它会产生以下结果，否则相应的错误将被捕获并会显示错误消息：

    
    
    C:>java JDBCExample
    Connecting to database...
    Creating statement...
    ID: 100, Age: 18, First: Zara, Last: Ali
    ID: 101, Age: 25, First: Mahnaz, Last: Fatma
    ID: 102, Age: 30, First: Zaid, Last: Khan
    ID: 103, Age: 28, First: Sumit, Last: Mittal
    C:>

