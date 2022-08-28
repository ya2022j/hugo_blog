+++
title = "Java MySQL 连接"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java MySQL 连接

Java 通过使用 JDBC 来连接 MySQL 数据库。Java 连接 MySQL 需要专用的驱动包，官方下载地址为：
**[http://dev.mysql.com/downloads/connector/j/]()** ，解压后得到 jar
库文件，然后在项目中导入该库文件。

本范例使用的是 Eclipse，导入 jar 包：

> **MySQL 8.0 以上版本的数据库连接有所不同：**
>
>   * 1、MySQL 8.0 以上版本驱动包版本 mysql-connector-java-8.0.16.jar。
>
>   * 2、 **com.mysql.jdbc.Driver** 更换为 com.mysql.cj.jdbc.Driver。
>
>   * MySQL 8.0 以上版本不需要建立 SSL 连接的，需要显式关闭。
>
>   * allowPublicKeyRetrieval=true 允许客户端从服务器获取公钥。
>
>   * 最后还需要设置 CST。
>
>

>
> 加载驱动与连接数据库方式如下：
>  
>  
>     Class.forName("com.mysql.cj.jdbc.Driver");
>     conn =
> DriverManager.getConnection("jdbc:mysql://localhost:3306/test_demo?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC","root","password");



## 1\. 创建测试数据

接下来我们在 MySQL 中创建 CodeBaoku 数据库，并创建 websites 数据表，表结构如下：

    
    
    CREATE TABLE `websites` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
        `url` varchar(255) NOT NULL DEFAULT '',
        `alexa` int(11) NOT NULL DEFAULT '0' COMMENT 'Alexa 排名',
        `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
    

插入一些数据：

    
    
    INSERT INTO `websites` VALUES ('1', 'Google', 'https://www.google.cm/', '1', 'USA');
    INSERT INTO `websites` VALUES ('2', '淘宝', 'https://www.taobao.com/', '13', 'CN'),;
    INSERT INTO `websites` VALUES ('3', '[编程宝库](http://www.codebaoku.com)', 'http://www.codebaoku.com/', '888', '');
    INSERT INTO `websites` VALUES ('4', '微博', 'http://weibo.com/', '20', 'CN');
    INSERT INTO `websites` VALUES ('5', 'Facebook', 'https://www.facebook.com/', '3', 'USA');
    

数据表显示如下：



## 2\. 连接数据库

以下范例使用了 JDBC 连接 MySQL 数据库，注意一些数据如用户名，密码需要根据你的开发环境来配置：

    
    
    package com.itbenkyou.test;
    
    import java.sql.*;
        
    public class MySQLDemo {
        
        // MySQL 8.0 以下版本 - JDBC 驱动名及数据库 URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost:3306/Codebaoku";
        
        // MySQL 8.0 以上版本 - JDBC 驱动名及数据库 URL
        //static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";  
        //static final String DB_URL = "jdbc:mysql://localhost:3306/Codebaoku?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
        
        
        // 数据库的用户名与密码，需要根据自己的设置
        static final String USER = "root";
        static final String PASS = "123456";
        
        public static void main(String[] args) {
            Connection conn = null;
            Statement stmt = null;
            try{
                // 注册 JDBC 驱动
                Class.forName(JDBC_DRIVER);
            
                // 打开链接
                System.out.println("连接数据库...");
                conn = DriverManager.getConnection(DB_URL,USER,PASS);
            
                // 执行查询
                System.out.println(" 范例化Statement对象...");
                stmt = conn.createStatement();
                String sql;
                sql = "SELECT id, name, url FROM websites";
                ResultSet rs = stmt.executeQuery(sql);
            
                // 展开结果集数据库
                while(rs.next()){
                    // 通过字段检索
                    int id  = rs.getInt("id");
                    String name = rs.getString("name");
                    String url = rs.getString("url");
        
                    // 输出数据
                    System.out.print("ID: " + id);
                    System.out.print(", 站点名称: " + name);
                    System.out.print(", 站点 URL: " + url);
                    System.out.print("\n");
                }
                // 完成后关闭
                rs.close();
                stmt.close();
                conn.close();
            }catch(SQLException se){
                // 处理 JDBC 错误
                se.printStackTrace();
            }catch(Exception e){
                // 处理 Class.forName 错误
                e.printStackTrace();
            }finally{
                // 关闭资源
                try{
                    if(stmt!=null) stmt.close();
                }catch(SQLException se2){
                }// 什么都不做
                try{
                    if(conn!=null) conn.close();
                }catch(SQLException se){
                    se.printStackTrace();
                }
            }
            System.out.println("Goodbye!");
        }
    }
    

