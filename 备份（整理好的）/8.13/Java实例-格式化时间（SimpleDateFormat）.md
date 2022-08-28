+++
title = "Java实例-格式化时间（SimpleDateFormat）"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:37"
categories = [
"Chinese",
]
+++
# Java 实例 - 格式化时间（SimpleDateFormat）

以下实例演示了如何使用 SimpleDateFormat 类的 format(date) 方法来格式化时间

## Main.java 文件

```java import java.text.SimpleDateFormat; import java.util.Date; public class
Main { public static void main(String[] args) { Date date = new Date(); String
strDateFormat = "yyyy-MM-dd HH:mm:ss"; SimpleDateFormat sdf = new
SimpleDateFormat(strDateFormat); System.out.println(sdf.format(date)); } } ```

以上代码运行输出结果为：

```java 2015-03-27 21:13:23 ```

