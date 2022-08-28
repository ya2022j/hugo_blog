+++
title = "JDBC Statement, PreparedStatement 和 CallableStatement"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC Statement, PreparedStatement 和 CallableStatement

获得了数据库连接后，我们就可以与数据库进行交互了。JDBC 中的 Statement, CallableStatement 和
PreparedStatement 三个对象，定义了一系列的方法和属性，可以用来向数据库发送 SQL 命令，接收数据。

接口 | 使用说明  
---|---  
Statement | 运行静态 SQL 语句时使用，Statement 不能接收输入参数。  
PreparedStatement | 当计划多次使用某条 SQL 语句时使用，并且 PreparedStatement 可以接收输入参数。  
CallableStatement | 用来调用数据库的存储过程，CallableStatement 可以接收输入参数。  
  


## 1\. Statement 对象

### 1）创建 Statement 对象

Statement 对象由 Connection 对象的 createStatement( ) 方法创建，用来执行静态 SQL 语句，如下所示：

    
    
    Statement stmt = null;
    try {
       stmt = conn.createStatement( );
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       . . .
    }
    

一旦创建了一个 Statement 对象，然后可以它的三个执行方法之一执行 SQL 语句。

  * **boolean execute(String SQL)  :**这个方法常用来执行 SQL DDL 语句。
  * **int executeUpdate(String SQL)  :**返回 SQL 语句执行时受影响的行数，常用来执行 INSERT，UPDATE 或 DELETE 语句。 
  * **ResultSet executeQuery(String SQL)  : **返回 ResultSet 对象。常用来执行 SELECT 语句，会得到一个结果集 ResultSet。 

### 2）关闭 Statement 对象

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 Statement 对象。

使用 close() 方法关闭 Statement。

    
    
    Statement stmt = null;
    try {
       stmt = conn.createStatement( );
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       stmt.close();
    }
    



## 2\. PreparedStatement 对象

PreparedStatement 接口扩展了 Statement 接口，给 Statement 对象增加几个高级功能。

它对 SQL 语句进行预编译，效率更高。另外，可以接收动态参数，避免 Statement 中的 SQL 注入问题。

### 1）创建 PreparedStatement 对象

    
    
    PreparedStatement pstmt = null;
    try {
       String SQL = "Update Employees SET age = ? WHERE id = ?";
       pstmt = conn.prepareStatement(SQL);
       pstmt.setInt(1, 22);
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       . . .
    }
    

在 JDBC 中参数使用 ？代表，在执行 SQL 语句之前，必须提供每一个参数的值。

setXXX() 方法将值绑定到参数，其中 XXX 表示希望绑定到输入参数值的 Java 数据类型。如果忘了提供值，将收到一个SQLException。

每个参数标记是由它的序号位置引用。第一标记表示位置 1，下一个位置为 2 等等。这种方法不同于 Java 数组索引，以 0 开始。

### 2）关闭 PreparedStatement 对象

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 PreparedStatement 对象。

使用 close() 方法关闭 PreparedStatement。

    
    
    PreparedStatement pstmt = null;
    try {
       String SQL = "Update Employees SET age = ? WHERE id = ?";
       pstmt = conn.prepareStatement(SQL);
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       pstmt.close();
    }
    



## 3\. CallableStatement 对象

正如一个Connection对象创建Statement和PreparedStatement对象，它也创造了CallableStatement对象这将被用来执行调用数据库存储过程。

### 1）创建 CallableStatement 对象

假设需要执行以下 Oracle 存储过程：

    
    
    CREATE OR REPLACE PROCEDURE getEmpName 
       (EMP_ID IN NUMBER, EMP_FIRST OUT VARCHAR) AS
    BEGIN
       SELECT first INTO EMP_FIRST
       FROM Employees
       WHERE ID = EMP_ID;
    END;
    

存储过程有三种类型的参数：IN，OUT和INOUT。 PreparedStatement对象只使用IN参数。
CallableStatement对象可以使用所有三个。

这里是每个的定义：

参数 | 描述  
---|---  
IN | 它的值是在创建SQL语句时未知的参数。将值绑定到与 setXXX() 方法的参数。  
OUT | 其值由它返回的SQL语句提供的参数。从 OUT 参数的 getXXX() 方法检索值。  
INOUT | 同时提供输入和输出值的参数。绑定变量使用 setXXX() 方法，使用 getXXX() 方法检索值。  
  
下面的代码显示了使用 Connection.prepareCall() 方法获得存储过程 CallableStatement 对象：

    
    
    CallableStatement cstmt = null;
    try {
       String SQL = "{call getEmpName (?, ?)}";
       cstmt = conn.prepareCall (SQL);
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       . . .
    }
    

SQL 表示存储过程，里面使用了参数占位符。

使用 CallableStatement 对象是就像使用 PreparedStatement 对象，执行该语句之前，必须将值绑定到所有的参数，否则将收到一个
SQLException。

如果有 IN 参数，只要按照 PreparedStatement 对象相同的规则，使用 setXXX() 方法绑定的 Java 数据类型。

当使用 OUT 和 INOUT 参数就必须采用额外的 CallableStatement 及 registerOutParameter()
方法。registerOutParameter() 方法绑定数据类型到存储过的返回值。

### 2）关闭 CallableStatement 对象

正如关闭其他 Statement 对象，出于同样的原因，也应该关闭 CallableStatement 对象。

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 CallableStatementv 对象。

使用 close() 方法关闭 CallableStatement。

    
    
    CallableStatement cstmt = null;
    try {
       String SQL = "{call getEmpName (?, ?)}";
       cstmt = conn.prepareCall (SQL);
       . . .
    }
    catch (SQLException e) {
       . . .
    }
    finally {
       cstmt.close();
    }
    

