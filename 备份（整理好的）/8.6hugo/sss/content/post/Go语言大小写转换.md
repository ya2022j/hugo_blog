+++
title = "Go语言大小写转换"
tags = [
"Golang",
"Chinese",
]
date = "2022-08-01 21:22:27"
categories = [
"Chinese",
]
+++



# Go语言大小写转换

Go语言常用的大小写转换方法如下表所示。  
  

表：大小写转换方法 方法 |  功能描述  
---|---  
func Title(s string) string |  将字符串 s 每个单词首字母大写返回  
func ToLower(s string) string |  将字符串 s 转换成小写返回  
func ToLowerSpecial(_case unicode.SpecialCase, s string) string |  将字符串 s
中所有字符按 _case 指定的映射转换成小写返回  
func ToTitle(s string) string |  将字符串 s 转换成大写返回  
func ToTitleSpecial(_case unicode.SpecialCase, s string) string |  将字符串 s
中所有字符按 _case 指定的映射转换成大写返回  
func ToUpper(s string) string |  将字符中 s 转换成大写返回  
func ToUpperSpecial(_case unicode.SpecialCase, s string) string |  将字符串 s
中所有字符按 _case 指定的映射转换成大写返回  
  
接下来通过一个示例来演示部分大小写转换函数的使用，代码如下所示。  

    
```golang
    
    package main
    import(
        "fmt"
        "strings"
    )
    func main(){
        TestTitle()
        TestToTitle()
        TestToLower()
        TestToUpper()
    }
    //将字符串 s 每个单词首字母大写返回
    func TestTitle(){
        fmt.Println(strings.Title("her royal highness"))
    }
    //将字符串 s 转换成大写返回
    func TestToTitle(){
        fmt.Println(strings.ToTitle("louD noises"))
    }
    //将字符串 s 转换成小写返回
    func TestToLower(){
        fmt.Println(strings.ToLower("Gopher"))
    }
    //将字符串s转换成大写返回
    func TestToUpper(){
        fmt.Println(strings.ToUpper("Gopher"))
    }
```

运行结果如下：

Her Royal Highness  
LOUD NOISES  
gopher  
GOPHER

