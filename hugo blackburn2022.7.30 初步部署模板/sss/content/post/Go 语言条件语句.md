+++
title = "Go 语言条件语句"
tags = [
"Golang",
"Chinese",
]
date = "2022-07-28 18:23:41"
categories = [
"Chinese",
]
+++
  * [ Go 语言教程 ](./)
  * [ Go 语言环境安装 ](Go 语言环境安装.html)
  * [ Go 语言结构 ](Go 语言结构.html)
  * [ Go 语言基础语法 ](Go 语言基础语法.html)
  * [ Go 语言数据类型 ](Go 语言数据类型.html)
  * [ Go 语言变量 ](Go 语言变量.html)
  * [ Go 语言常量 ](Go 语言常量.html)
  * [ Go 语言运算符 ](Go 语言运算符.html)
  * [ Go 语言条件语句 ](Go 语言条件语句.html)
  * [ Go 语言循环语句 ](Go 语言循环语句.html)
  * [ Go 语言函数 ](Go 语言函数.html)
  * [ Go 语言变量作用域 ](Go 语言变量作用域.html)
  * [ Go 语言数组 ](Go 语言数组.html)
  * [ Go 语言指针 ](Go 语言指针.html)
  * [ Go 语言结构体 ](Go 语言结构体.html)
  * [ Go 并发 ](Go 并发.html)
  *   * [ Published with GitBook ](https://www.gitbook.com)

#  __[Go 语言条件语句](.)

# Go 语言条件语句

条件语句需要开发者通过指定一个或多个条件，并通过测试条件是否为 true 来决定是否执行指定语句，并在条件为 false 的情况在执行另外的语句。

Go 语言提供了以下几种条件判断语句：

语句| 描述  
---|---  
[if 语句](go/go-if-statement.html "Go if 语句")|  **if 语句** 由一个布尔表达式后紧跟一个或多个语句组成。  
[if...else 语句](go/go-if-else-statement.html "Go if...else 语句")|  **if 语句**
后可以使用可选的 **else 语句**, else 语句中的表达式在布尔表达式为 false 时执行。  
[ if 嵌套语句](go/go-nested-if-statements.html "Go if 嵌套语句")| 你可以在 **if** 或 **else
if** 语句中嵌入一个或多个 **if** 或 **else if** 语句。  
[switch 语句](go/go-switch-statement.html "Go switch 语句")|  **switch**
语句用于基于不同条件执行不同动作。  
[select 语句](go/go-select-statement.html "Go select 语句")|  **select** 语句类似于
**switch** 语句，但是select会随机执行一个可运行的case。如果没有case可运行，它将阻塞，直到有case可运行。  
  
> 注意：Go 没有三目运算符，所以不支持 **?:** 形式的条件判断。

#  results matching ""

# No results matching ""

[ __](Go 语言运算符.html) [ __](Go 语言循环语句.html)

