+++
title = "JDBC 创建、删除表范例"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 创建、删除表范例

在本教程将演示如何在 JDBC 应用程序中创建 和 删除表。

删除表后，表中的所有内容都将丢失，所以必须在继续删除表之前作出明确的决定。



## 1\. 创建表范例

复制以下示例代码保存到文件： _CreateTable.java_ 中，然后编译并运行如下:

    
    
    //STEP 1. Import required packages
    
    import java.sql.*;
    
    public class CreateTable {
        // JDBC driver name and database URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";
    
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
                System.out.println("Connecting to a selected database...");
                conn = DriverManager.getConnection(DB_URL, USER, PASS);
                System.out.println("Connected database successfully...");
    
                //STEP 4: Execute a query
                System.out.println("Creating table in given database...");
                stmt = conn.createStatement();
    
                String sql = "CREATE TABLE student " +
                            "(id INTEGER not NULL, " +
                            " first VARCHAR(255), " + 
                            " last VARCHAR(255), " + 
                            " age INTEGER, " + 
                            " PRIMARY KEY ( id ))"; 
    
                stmt.executeUpdate(sql);
                System.out.println("Created table in given database...");
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
                    conn.close();
                }catch(SQLException se){
                }// do nothing
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
    

编译上面代码，如下 -

    
    
    F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs CreateTable.java
    

执行上面代码，如下 -

    
    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs CreateTable
    Connecting to a selected database...
    Thu Jun 01 22:17:34 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
    Connected database successfully...
    Creating table in given database...
    Created table in given database...
    Goodbye!
    



## 2\. 删除表范例

复制以下示例代码保存到文件： _DropTable.java_ 中，然后编译并运行如下:

    
    
    //STEP 1. Import required packages
    import java.sql.*;
    
    public class DropTable {
        // JDBC driver name and database URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";
    
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
                System.out.println("Connecting to a selected database...");
                conn = DriverManager.getConnection(DB_URL, USER, PASS);
                System.out.println("Connected database successfully...");
    
                //STEP 4: Execute a query
                System.out.println("Deleting table in given database...");
                stmt = conn.createStatement();
    
                String sql = "DROP TABLE student ";
    
                stmt.executeUpdate(sql);
                System.out.println("Table  deleted in given database...");
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
                    conn.close();
                }catch(SQLException se){
                }// do nothing
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
    

编译上面代码，如下 -

    
    
    F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs DropTable.java
    

执行上面代码，如下 -

    
    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs DropTable
    
    Connecting to a selected database...
    Thu Jun 01 22:39:01 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
    Connected database successfully...
    Deleting table in given database...
    Table  deleted in given database...
    Goodbye!
    

在执行上面语句后，数据库 jdbc_db 中的 student 表将会被成功地删除了。

