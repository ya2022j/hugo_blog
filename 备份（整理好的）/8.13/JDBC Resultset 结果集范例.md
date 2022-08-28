+++
title = "JDBC Resultset 结果集范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC Resultset 结果集范例

JDBC ResultSet 通过移动光标的方法浏览结果集。



## 1\. ResultSet 移动光标的方法

编号 | 方法 | 描述  
---|---|---  
1 | public void beforeFirst() throws SQLException | 将光标移动到第一行之前  
2 | public void afterLast() throws SQLException | 将光标移动到最后一行之后。  
3 | public boolean first() throws SQLException | 将光标移动到第一行。  
4 | public void last() throws SQLException | 将光标移动到最后一行。  
5 | public boolean absolute(int row) throws SQLException | 将光标移动到指定的行。  
6 | public boolean relative(int row) throws SQLException |
从当前指向的位置，将光标向前或向后移动给定行数。  
7 | public boolean previous() throws SQLException | 将光标移动到上一行。
如果上一行关闭结果集，此方法返回false。  
8 | public boolean next() throws SQLException | 将光标移动到下一行。
如果结果集中没有更多行，则此方法返回false。  
9 | public int getRow() throws SQLException | 返回光标指向的行号。  
10 | public void moveToInsertRow() throws SQLException |
将光标移动到结果集中的特殊行，该行可用于将新行插入数据库。当前光标位置被记住。  
11 | public void moveToCurrentRow() throws SQLException |
如果光标当前位于插入行，则将光标移回当前行; 否则，此方法什么也不做  
  


## 2\. ResultSet 浏览结果集范例

    
    
    //STEP 1. Import required packages
    import java.sql.*;
    
    public class NavigatingResultSet {
        // JDBC driver name and database URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost/EMP";
    
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
                conn = DriverManager.getConnection(DB_URL,USER,PASS);
    
                //STEP 4: Execute a query to create statment with
                // required arguments for RS example.
                System.out.println("Creating statement...");
                stmt = conn.createStatement(
                                    ResultSet.TYPE_SCROLL_INSENSITIVE,
                                    ResultSet.CONCUR_READ_ONLY);
                String sql;
                sql = "SELECT id, first, last, age FROM Employees";
                ResultSet rs = stmt.executeQuery(sql);
    
                // Move cursor to the last row.
                System.out.println("Moving cursor to the last...");
                rs.last();
    
                //STEP 5: Extract data from result set
                System.out.println("Displaying record...");
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
    
                // Move cursor to the first row.
                System.out.println("Moving cursor to the first row...");
                rs.first();
    
                //STEP 6: Extract data from result set
                System.out.println("Displaying record...");
                //Retrieve by column name
                id  = rs.getInt("id");
                age = rs.getInt("age");
                first = rs.getString("first");
                last = rs.getString("last");
    
                //Display values
                System.out.print("ID: " + id);
                System.out.print(", Age: " + age);
                System.out.print(", First: " + first);
                System.out.println(", Last: " + last);
                // Move cursor to the first row.
    
                System.out.println("Moving cursor to the next row...");
                rs.next();
    
                //STEP 7: Extract data from result set
                System.out.println("Displaying record...");
                id  = rs.getInt("id");
                age = rs.getInt("age");
                first = rs.getString("first");
                last = rs.getString("last");
    
                //Display values
                System.out.print("ID: " + id);
                System.out.print(", Age: " + age);
                System.out.print(", First: " + first);
                System.out.println(", Last: " + last);
    
                //STEP 8: Clean-up environment
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
    



## 3\. 编译运行

    
    
    F:\worksp\jdbc>javac -Djava.ext.dirs=F:\worksp\jdbc\libs NavigatingResultSet.java
    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs NavigatingResultSet
    

运行上面代码，得到以下结果：

