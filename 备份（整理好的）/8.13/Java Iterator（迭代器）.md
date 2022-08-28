+++
title = "Java Iterator（迭代器）"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java Iterator（迭代器）

[

Java Iterator（迭代器）不是一个集合，它是一种用于访问集合的方法，可用于迭代 ArrayList 和 HashSet 等集合。

Iterator 是 Java 迭代器最简单的实现，ListIterator 是 Collection API 中的接口， 它扩展了 Iterator
接口。

迭代器 it 的两个基本操作是 next 、hasNext 和 remove。

调用 it.next() 会返回迭代器的下一个元素，并且更新迭代器的状态。

调用 it.hasNext() 用于检测集合中是否还有元素。

调用 it.remove() 将迭代器返回的元素删除。

Iterator 类位于 java.util 包中，使用前需要引入它，语法格式如下：

    
    
    import java.util.Iterator; // 引入 Iterator 类



## 1\. 获取一个迭代器

集合想获取一个迭代器可以使用 iterator() 方法:

    
    
    // 引入 ArrayList 和 Iterator 类
    import java.util.ArrayList;
    import java.util.Iterator;
    
    public class CodebaokuTest {
        public static void main(String[] args) {
    
            // 创建集合
            ArrayList sites = new ArrayList();
            sites.add("Google");
            sites.add("Codebaoku");
            sites.add("Taobao");
            sites.add("Zhihu");
    
            // 获取迭代器
            Iterator it = sites.iterator();
    
            // 输出集合中的第一个元素
            System.out.println(it.next());
        }
    }
    

执行以上代码，输出结果如下：

    
    
    Google



## 2\. 循环集合元素

让迭代器 it 逐个返回集合中所有元素最简单的方法是使用 while 循环：

    
    
    while(it.hasNext()) {
        System.out.println(it.next());
    }
    

以下输出集合 sites 中的所有元素：

    
    
    // 引入 ArrayList 和 Iterator 类
    import java.util.ArrayList;
    import java.util.Iterator;
    
    public class CodebaokuTest {
        public static void main(String[] args) {
    
            // 创建集合
            ArrayList sites = new ArrayList();
            sites.add("Google");
            sites.add("Codebaoku");
            sites.add("Taobao");
            sites.add("Zhihu");
    
            // 获取迭代器
            Iterator it = sites.iterator();
    
            // 输出集合中的所有元素
            while(it.hasNext()) {
                System.out.println(it.next());
            }
        }
    }
    

执行以上代码，输出结果如下：

    
    
    Google
    Codebaoku
    Taobao
    Zhihu
    



## 3\. 删除元素

要删除集合中的元素可以使用 remove() 方法。

以下范例我们删除集合中小于 10 的元素：

    
    
    // 引入 ArrayList 和 Iterator 类
    import java.util.ArrayList;
    import java.util.Iterator;
    
    public class CodebaokuTest {
        public static void main(String[] args) {
            ArrayList numbers = new ArrayList();
            numbers.add(12);
            numbers.add(8);
            numbers.add(2);
            numbers.add(23);
            Iterator it = numbers.iterator();
            while(it.hasNext()) {
                Integer i = it.next();
                if(i < 10) {  
                    it.remove();  // 删除小于 10 的元素
                }
            }
            System.out.println(numbers);
        }
    }
    

执行以上代码，输出结果如下：

    
    
    [12, 23]

