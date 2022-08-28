+++
title = "JDBC 创建数据库范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 创建数据库范例

在本教程将演示如何在 JDBC 应用程序中创建数据库。在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中创建数据库。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序创建数据库需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 创建数据库范例

复制以下示例代码保存到文件： _CreateDatabase.java_ 中，然后编译并运行如下：

    
    
    //STEP 1. Import required packages
    
    import java.sql.*;
    
    public class CreateDatabase {
       // JDBC driver name and database URL
       static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
       static final String DB_URL = "jdbc:mysql://localhost/";
    
       //  Database credentials
       static final String USER = "root";
       static final String PASS = "123456";
    
       public static void main(String[] args) {
       Connection conn = null;
       Statement stmt = null;
       try{
          //STEP 2: Register JDBC driver
          Class.forName("com.mysql.jdbc.Driver");
    
          //STEP 3: Open a connection
          System.out.println("Connecting to database...");
          conn = DriverManager.getConnection(DB_URL, USER, PASS);
    
          //STEP 4: Execute a query
          System.out.println("Creating database...");
          stmt = conn.createStatement();
    
          String sql = "CREATE DATABASE jdbc_db";
          stmt.executeUpdate(sql);
          System.out.println("Database created successfully...");
       }catch(SQLException se){
          //Handle errors for JDBC
          se.printStackTrace();
       }catch(Exception e){
          //Handle errors for Class.forName
          e.printStackTrace();
       }finally{
          //finally block used to close resources
          try{
             if(stmt!=null)
                stmt.close();
          }catch(SQLException se2){
          }// nothing we can do
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
    

编译上面代码，如下 -

    
    
    F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs CreateDatabase.java
    

执行上面代码，如下 -

    
    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs CreateDatabase
    Connecting to database...
    Thu Jun 01 21:55:55 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
    Creating database...
    Database created successfully...
    Goodbye!
    
    F:\worksp\jdbc>
    

