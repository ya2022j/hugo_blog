+++
title = "JDBC 教程"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# JDBC 教程

JDBC 即 Java Database Connectivity，是指 Java 数据库连接，在 Java
语言中用来规范客户端程序如何来访问数据库的应用程序接口，提供了诸如查询和更新数据库中数据的方法。

JDBC 提供了一组 API，用于访问任何形式的表格数据，尤其是存储在关系数据库中的数据。

JDBC 使用流程如下：

  * 连接数据源，比如：数据库。
  * 为数据库传递查询和更新指令。
  * 处理数据库响应并返回的结果。



## 1\. JDBC 架构

JDBC API支持两层和三层处理模型进行数据库访问，但在一般的JDBC体系结构由两层组成：

  * JDBC API: 提供了应用程序对JDBC的管理连接。
  * JDBC Driver API: 支持JDBC管理到驱动器连接。

JDBC API 的使用驱动程序管理器和数据库特定的驱动程序提供透明的连接到异构数据库。

DBC驱动程序管理器可确保正确的驱动程序来访问每个数据源。该驱动程序管理器能够支持连接到多个异构数据库的多个并发的驱动程序。

以下是结构图，它显示了驱动程序管理器方面的JDBC驱动程序和Java应用程序的位置：

![](http://static.codebaoku.com/pics/be/a8/bea88cf163c3ec2d6333b81d284396cb.jpg)



## 2\. JDBC 组件

JDBC API 提供了以下接口和类：

  * DriverManager   
这个类管理数据库驱动程序的列表。内容是否符合从Java应用程序使用的通信子协议正确的数据库驱动程序的连接请求。识别JDBC在一定子协议的第一个驱动器将被用来建立数据库连接。

  * Driver   
此接口处理与数据库服务器通信。很少直接与驱动程序对象。相反，使用DriverManager中的对象，它管理此类型的对象。它也抽象与驱动程序对象工作相关的详细信息。

  * Connection   
此接口与接触数据库的所有方法。连接对象表示通信上下文，即，与数据库中的所有的通信是通过唯一的连接对象。

  * Statement   
可以使用这个接口创建的对象的SQL语句提交到数据库。一些派生的接口接受除执行存储过程的参数。

  * ResultSet   
这些对象保存从数据库后，执行使用Statement对象的SQL查询中检索数据。它作为一个迭代器，让您可以通过移动它的数据。

  * SQLException   
这个类处理发生在一个数据库应用程序的任何错误。



## 3\. JDBC 编程步骤

### 1）加载驱动程序

    
    
    Class.forName(driverClass)
    //加载MySql驱动
    Class.forName("com.mysql.jdbc.Driver")
    //加载Oracle驱动
    Class.forName("oracle.jdbc.driver.OracleDriver")
    

### 2）获得数据库连接

    
    
    DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/imooc", "root", "root");
    

### 3）创建 Statement\PreparedStatement 对象

    
    
    conn.createStatement();
    conn.prepareStatement(sql);
    



## 4\. JDBC 完整编程范例

    
    
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.Statement;
    
    public class DbUtil {
    
        public static final String URL = "jdbc:mysql://localhost:3306/imooc";
        public static final String USER = "liulx";
        public static final String PASSWORD = "123456";
    
        public static void main(String[] args) throws Exception {
            //1.加载驱动程序
            Class.forName("com.mysql.jdbc.Driver");
            //2. 获得数据库连接
            Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
            //3.操作数据库，实现增删改查
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT user_name, age FROM imooc_goddess");
            //如果有数据，rs.next()返回true
            while(rs.next()){
                System.out.println(rs.getString("user_name")+" 年龄："+rs.getInt("age"));
            }
        }
    }
    



## 5\. JDBC 增删改查编程范例

    
    
    public class DbUtil {
        public static final String URL = "jdbc:mysql://localhost:3306/imooc";
        public static final String USER = "liulx";
        public static final String PASSWORD = "123456";
        private static Connection conn = null;
        static{
            try {
                //1.加载驱动程序
                Class.forName("com.mysql.jdbc.Driver");
                //2. 获得数据库连接
                conn = DriverManager.getConnection(URL, USER, PASSWORD);
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    
        public static Connection getConnection(){
            return conn;
        }
    }
    
    //模型
    package liulx.model;
    
    import java.util.Date;
    
    public class Goddess {
    
        private Integer id;
        private String user_name;
        private Integer sex;
        private Integer age;
        private Date birthday; //注意用的是java.util.Date
        private String email;
        private String mobile;
        private String create_user;
        private String update_user;
        private Date create_date;
        private Date update_date;
        private Integer isDel;
        //getter setter方法。。。
    }
    
    //---------dao层--------------
    package liulx.dao;
    
    import liulx.db.DbUtil;
    import liulx.model.Goddess;
    
    import java.sql.Connection;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Statement;
    import java.util.ArrayList;
    import java.util.List;
    
    public class GoddessDao {
        //增加
        public void addGoddess(Goddess g) throws SQLException {
            //获取连接
            Connection conn = DbUtil.getConnection();
            //sql
            String sql = "INSERT INTO imooc_goddess(user_name, sex, age, birthday, email, mobile,"+
                "create_user, create_date, update_user, update_date, isdel)"
                    +"values("+"?,?,?,?,?,?,?,CURRENT_DATE(),?,CURRENT_DATE(),?)";
            //预编译
            PreparedStatement ptmt = conn.prepareStatement(sql); //预编译SQL，减少sql执行
    
            //传参
            ptmt.setString(1, g.getUser_name());
            ptmt.setInt(2, g.getSex());
            ptmt.setInt(3, g.getAge());
            ptmt.setDate(4, new Date(g.getBirthday().getTime()));
            ptmt.setString(5, g.getEmail());
            ptmt.setString(6, g.getMobile());
            ptmt.setString(7, g.getCreate_user());
            ptmt.setString(8, g.getUpdate_user());
            ptmt.setInt(9, g.getIsDel());
    
            //执行
            ptmt.execute();
        }
    
        public void updateGoddess(){
            //获取连接
            Connection conn = DbUtil.getConnection();
            //sql, 每行加空格
            String sql = "UPDATE imooc_goddess" +
                    " set user_name=?, sex=?, age=?, birthday=?, email=?, mobile=?,"+
                    " update_user=?, update_date=CURRENT_DATE(), isdel=? "+
                    " where id=?";
            //预编译
            PreparedStatement ptmt = conn.prepareStatement(sql); //预编译SQL，减少sql执行
    
            //传参
            ptmt.setString(1, g.getUser_name());
            ptmt.setInt(2, g.getSex());
            ptmt.setInt(3, g.getAge());
            ptmt.setDate(4, new Date(g.getBirthday().getTime()));
            ptmt.setString(5, g.getEmail());
            ptmt.setString(6, g.getMobile());
            ptmt.setString(7, g.getUpdate_user());
            ptmt.setInt(8, g.getIsDel());
            ptmt.setInt(9, g.getId());
    
            //执行
            ptmt.execute();
        }
    
        public void delGoddess(){
            //获取连接
            Connection conn = DbUtil.getConnection();
            //sql, 每行加空格
            String sql = "delete from imooc_goddess where id=?";
            //预编译SQL，减少sql执行
            PreparedStatement ptmt = conn.prepareStatement(sql);
    
            //传参
            ptmt.setInt(1, id);
    
            //执行
            ptmt.execute();
        }
    
        public List<Goddess> query() throws SQLException {
            Connection conn = DbUtil.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT user_name, age FROM imooc_goddess");
    
            List<Goddess> gs = new ArrayList<Goddess>();
            Goddess g = null;
            while(rs.next()){
                g = new Goddess();
                g.setUser_name(rs.getString("user_name"));
                g.setAge(rs.getInt("age"));
    
                gs.add(g);
            }
            return gs;
        }
    
        public Goddess get(){
            Goddess g = null;
            //获取连接
            Connection conn = DbUtil.getConnection();
            //sql, 每行加空格
            String sql = "select * from  imooc_goddess where id=?";
            //预编译SQL，减少sql执行
            PreparedStatement ptmt = conn.prepareStatement(sql);
            //传参
            ptmt.setInt(1, id);
            //执行
            ResultSet rs = ptmt.executeQuery();
            while(rs.next()){
                g = new Goddess();
                g.setId(rs.getInt("id"));
                g.setUser_name(rs.getString("user_name"));
                g.setAge(rs.getInt("age"));
                g.setSex(rs.getInt("sex"));
                g.setBirthday(rs.getDate("birthday"));
                g.setEmail(rs.getString("email"));
                g.setMobile(rs.getString("mobile"));
                g.setCreate_date(rs.getDate("create_date"));
                g.setCreate_user(rs.getString("create_user"));
                g.setUpdate_date(rs.getDate("update_date"));
                g.setUpdate_user(rs.getString("update_user"));
                g.setIsDel(rs.getInt("isdel"));
            }
            return g;
        }
    }
    

