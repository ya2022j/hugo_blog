+++
title = "JDBC PreparedStatement 使用范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC PreparedStatement 使用范例

JDBC PreparedStatement 对象扩展了 Statement 对象，给 Statement 对象增加几个高级功能。

JDBC PreparedStatement 对 SQL 语句进行预编译，效率更高。另外，可以接收动态参数，避免 Statement 中的 SQL
注入问题。



## 1\. PreparedStatement 使用范例

    
    
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
       PreparedStatement stmt = null;
       try{
          //STEP 2: Register JDBC driver
          Class.forName("com.mysql.jdbc.Driver");
    
          //STEP 3: Open a connection
          System.out.println("Connecting to database...");
          conn = DriverManager.getConnection(DB_URL,USER,PASS);
    
          //STEP 4: Execute a query
          System.out.println("Creating statement...");
          String sql = "UPDATE Employees set age=? WHERE id=?";
          stmt = conn.prepareStatement(sql);
          
          //Bind values into the parameters.
          stmt.setInt(1, 35);  // This would set age
          stmt.setInt(2, 102); // This would set ID
          
          // Let us update age of the record with ID = 102;
          int rows = stmt.executeUpdate();
          System.out.println("Rows impacted : " + rows );
    
          // Let us select all the records and display them.
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
    }//end JDBCExample
    



## 2\. 编译运行

现在来编译上面的例子：

    
    
    C:>javac JDBCExample.java
    C:>

当运行 JDBCExample，它会产生以下结果：

    
    
    C:>java JDBCExample
    Connecting to database...
    Creating statement...
    Rows impacted : 1
    ID: 100, Age: 18, First: Zara, Last: Ali
    ID: 101, Age: 25, First: Mahnaz, Last: Fatma
    ID: 102, Age: 35, First: Zaid, Last: Khan
    ID: 103, Age: 30, First: Sumit, Last: Mittal
    Goodbye!
    C:>

