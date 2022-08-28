+++
title = "Go 语言指针"
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

#  __[Go 语言指针](.)

# Go 语言指针

Go 语言中指针是很容易学习的，Go 语言中使用指针可以更简单的执行一些任务。

接下来让我们来一步步学习 Go 语言指针。

我们都知道，变量是一种使用方便的占位符，用于引用计算机内存地址。

Go 语言的取地址符是 &，放到一个变量前使用就会返回相应变量的内存地址。

以下实例演示了变量在内存中地址：

## 实例

package main  
  
import "fmt"  
  
func main() {  
var a int = 10  
  
fmt.Printf("变量的地址: %x\n", &a  )  
}  

执行以上代码输出结果为：

    
    
    变量的地址: 20818a220

现在我们已经了解了什么是内存地址和如何去访问它。接下来我们将具体介绍指针。

* * *

## 什么是指针

一个指针变量指向了一个值的内存地址。

类似于变量和常量，在使用指针前你需要声明指针。指针声明格式如下：

    
    
    var var_name *var-type

var-type 为指针类型，var_name 为指针变量名，* 号用于指定变量是作为一个指针。以下是有效的指针声明：

    
    
    var ip *int        /* 指向整型*/
    var fp *float32    /* 指向浮点型 */

本例中这是一个指向 int 和 float32 的指针。

* * *

## 如何使用指针

指针使用流程：

  * 定义指针变量。
  * 为指针变量赋值。
  * 访问指针变量中指向地址的值。

在指针类型前面加上 * 号（前缀）来获取指针所指向的内容。

## 实例

package main  
  
import "fmt"  
  
func main() {  
var a int= 20 /* 声明实际变量 */  
var ip *int /* 声明指针变量 */  
  
ip = &a  /* 指针变量的存储地址 */  
  
fmt.Printf("a 变量的地址是: %x\n", &a  )  
  
/* 指针变量的存储地址 */  
fmt.Printf("ip 变量储存的指针地址: %x\n", ip )  
  
/* 使用指针访问值 */  
fmt.Printf("*ip 变量的值: %d\n", *ip )  
}  

以上实例执行输出结果为：

    
    
    a 变量的地址是: 20818a220
    ip 变量储存的指针地址: 20818a220
    *ip 变量的值: 20

* * *

## Go 空指针

当一个指针被定义后没有分配到任何变量时，它的值为 nil。

nil 指针也称为空指针。

nil在概念上和其它语言的null、None、nil、NULL一样，都指代零值或空值。

一个指针变量通常缩写为 ptr。

查看以下实例：

## 实例

package main  
  
import "fmt"  
  
func main() {  
var ptr *int  
  
fmt.Printf("ptr 的值为 : %x\n", ptr  )  
}  

以上实例输出结果为：

    
    
    ptr 的值为 : 0

空指针判断：

    
    
    if(ptr != nil)     /* ptr 不是空指针 */
    if(ptr == nil)    /* ptr 是空指针 */

* * *

## Go指针更多内容

接下来我们将为大家介绍Go语言中更多的指针应用：

内容 |  描述  
---|---  
[Go 指针数组](go-array-of-pointers.html) |  你可以定义一个指针数组来存储地址  
[Go 指向指针的指针](go-pointer-to-pointer.html) |  Go 支持指向指针的指针  
[Go 向函数传递指针参数](go-passing-pointers-to-functions.html) | 通过引用或地址传参，在函数调用时可以改变其值  
  
#  results matching ""

# No results matching ""

[ __](Go 语言数组.html) [ __](Go 语言结构体.html)

