+++
title = "JDBCCallableStatement 使用范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC CallableStatement 对象用来调用数据库存储过程。



## 1\. 存储过程范例

    
    
    DELIMITER $$
    
    DROP PROCEDURE IF EXISTS `EMP`.`getEmpName` $$
    CREATE PROCEDURE `EMP`.`getEmpName` 
       (IN EMP_ID INT, OUT EMP_FIRST VARCHAR(255))
    BEGIN
       SELECT first INTO EMP_FIRST
       FROM Employees
       WHERE ID = EMP_ID;
    END $$
    
    DELIMITER ;



## 2\. CallableStatement 使用范例

    
    
    //STEP 1. Import required packages
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
       CallableStatement stmt = null;
       try{
          //STEP 2: Register JDBC driver
          Class.forName("com.mysql.jdbc.Driver");
    
          //STEP 3: Open a connection
          System.out.println("Connecting to database...");
          conn = DriverManager.getConnection(DB_URL,USER,PASS);
    
          //STEP 4: Execute a query
          System.out.println("Creating statement...");
          String sql = "{call getEmpName (?, ?)}";
          stmt = conn.prepareCall(sql);
          
          //Bind IN parameter first, then bind OUT parameter
          int empID = 102;
          stmt.setInt(1, empID); // This would set ID as 102
          // Because second parameter is OUT so register it
          stmt.registerOutParameter(2, java.sql.Types.VARCHAR);
          
          //Use execute method to run stored procedure.
          System.out.println("Executing stored procedure..." );
          stmt.execute();
    
          //Retrieve employee name with getXXX method
          String empName = stmt.getString(2);
          System.out.println("Emp Name with ID:" + 
                   empID + " is " + empName);
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
    }//end JDBCExample



## 3\. 编译运行

现在来编译上面的例子：

    
    
    C:>javac JDBCExample.java
    C:>

当运行JDBCExample，它会产生以下结果：

    
    
    C:>java JDBCExample
    Connecting to database...
    Creating statement...
    Executing stored procedure...
    Emp Name with ID:102 is Zaid
    Goodbye!
    C:>

