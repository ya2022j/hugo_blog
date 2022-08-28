+++
title = "JDBC 事务"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 事务

默认情况下 JDBC 事务处于自动提交模式，每个 SQL 语句都是在完成时自动提交到数据库。

在有些场景下，我们可能想关闭自动提交和管理自己的事务：

  * 为了提高性能；
  * 为了保持业务流程的完整性。
  * 使用分布式事务。

所谓事务就是把单个 SQL 语句或一组 SQL 语句作为一个逻辑单元，如果任何语句失败，整个事务失败。

JDBC驱动程序默认使用 auto-commit 模式，如果要启用手动事务支持，使用 Connection 对象的的 setAutoCommit()
方法。如果传递一个布尔值 false 到 setAutoCommit()，关闭自动提交。可以传递一个布尔值 true 将其重新打开。

例如，如果有一个名为 conn 的 Connection 对象，以下代码来关闭自动提交：

    
    
    conn.setAutoCommit(false);
    



## 1\. 提交和回滚

一旦已经完成了变化，要提交更改，然后调用 commit（在连接对象）方法，如下所示：

    
    
    conn.commit( );
    

否则回滚更新，使用下面的代码：

    
    
    onn.rollback( );
    

下面的例子演示了如何使用一个提交和回滚对象：

    
    
    try{
       //Assume a valid connection object conn
       conn.setAutoCommit(false);
       Statement stmt = conn.createStatement();
       
       String SQL = "INSERT INTO Employees  " +
                    "VALUES (106, 20, 'Rita', 'Tez')";
       stmt.executeUpdate(SQL);  
       //Submit a malformed SQL statement that breaks
       String SQL = "INSERTED IN Employees  " +
                    "VALUES (107, 22, 'Sita', 'Singh')";
       stmt.executeUpdate(SQL);
       // If there is no error.
       conn.commit();
    }catch(SQLException se){
       // If there is any error.
       conn.rollback();
    }
    



## 2\. 使用保存点

JDBC 保存点的接口提供了额外的事务控制。设置一个保存点就是在事务中定义一个逻辑回滚点。如果发生错误，则可以使用 rollback
方法来撤消到上一个保存点。

Connection 对象有两个新的方法，可帮助管理保存点：

  * setSavepoint(String savepointName): 定义了一个新的保存点。它也返回一个Savepoint 对象。
  * releaseSavepoint(Savepoint savepointName): 删除一个保存点。请注意，它需要一个Savepoint 对象作为参数。这个对象通常是由setSavepoint()方法生成一个保存点。

有一个rollback ( String savepointName ) 方法回滚工作到指定的保存点。

下面的例子演示如何使用 Savepoint 对象：

    
    
    try{
       //Assume a valid connection object conn
       conn.setAutoCommit(false);
       Statement stmt = conn.createStatement();
       
       //set a Savepoint
       Savepoint savepoint1 = conn.setSavepoint("Savepoint1");
       String SQL = "INSERT INTO Employees " +
                    "VALUES (106, 20, 'Rita', 'Tez')";
       stmt.executeUpdate(SQL);  
       //Submit a malformed SQL statement that breaks
       String SQL = "INSERTED IN Employees " +
                    "VALUES (107, 22, 'Sita', 'Tez')";
       stmt.executeUpdate(SQL);
       // If there is no error, commit the changes.
       conn.commit();
    
    }catch(SQLException se){
       // If there is any error.
       conn.rollback(savepoint1);
    }
    

在这种情况下如果 INSERT 语句不成功，一切都将被回滚。

