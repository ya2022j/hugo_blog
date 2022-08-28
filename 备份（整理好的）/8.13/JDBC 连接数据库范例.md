+++
title = "JDBC 连接数据库范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 连接数据库范例

本教程提供了如何创建JDBC应用程序的范例，包括：如何打开一个数据库连接，执行 SQL 查询，并显示执行结果。



## 1\. JDBC 连接数据库步骤

构建一个 JDBC 连接数据库应用程序的六个步骤：

### 1）导入数据包

需要包括含有需要进行数据库编程的JDBC类的包。大多数情况下，使用 import java.sql.* 就可以了。

### 2）注册JDBC驱动程序

可以与数据库打开一个通信通道。

### 3）打开连接

需要使用 DriverManager.getConnection() 方法创建一个 Connection 对象，它代表与数据库的物理连接。

### 4）执行查询

需要使用类型声明的对象建立并提交一个SQL语句到数据库。

### 5）从结果集中提取数据

要求使用适当的关于 ResultSet.getXXX() 方法来检索结果集的数据。

### 6）清理环境

需要明确地关闭所有的数据库资源相对依靠JVM的垃圾收集。



## 2\. JDBC 连接数据库实例

这个范例可以作为一个模板，在需要建立JDBC应用程序。

    
    
    //STEP 1. Import required packages
    import java.sql.*;
    
    public class FirstExample {
        // JDBC driver name and database URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost/EMP";
    
        //  Database credentials
        static final String USER = "username";
        static final String PASS = "password";
    
        public static void main(String[] args) {
            Connection conn = null;
            Statement stmt = null;
            try{
                //STEP 2: Register JDBC driver
                Class.forName("com.mysql.jdbc.Driver");
    
                //STEP 3: Open a connection
                System.out.println("Connecting to database...");
                conn = DriverManager.getConnection(DB_URL,USER,PASS);
    
                //STEP 4: Execute a query
                System.out.println("Creating statement...");
                stmt = conn.createStatement();
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
    }
    

现在来编译上面的例子如下：

    
    
    C:>javac FirstExample.java
    C:>
    

当运行FirstExample，它会产生以下结果：

    
    
    C:>java FirstExample
    Connecting to database...
    Creating statement...
    ID: 100, Age: 18, First: Zara, Last: Ali
    ID: 101, Age: 25, First: Mahnaz, Last: Fatma
    ID: 102, Age: 30, First: Zaid, Last: Khan
    ID: 103, Age: 28, First: Sumit, Last: Mittal
    C:>
    

