+++
title = "Java流程控制"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:11"
categories = [
"Chinese",
]
+++
  

#  Java流程控制

    
    



Java流程控制的语法与 C/C++ 类似，也有 if...else、while、do...while、for、switch...case等，这里不再讲述具体语法，仅举例说明。

```java

  
输出九九乘法表（右上三角）：

    
    
    public class Demo {
        public static void main(String[] args){
            int i, j;
            for(i=1; i<=9; i++){
                for(j=1; j<=9; j++){
                    if(j<i){
                        //打印八个空格，去掉空格就是左上三角形
                        System.out.print("        ");
                    }else{
                        System.out.printf("%d*%d=%2d  ", i, j, i*j);
                    }
                }
                System.out.print("\n"); 
            }
        }
    }
```
运行结果：

    
    
    1*1= 1  1*2= 2  1*3= 3  1*4= 4  1*5= 5  1*6= 6  1*7= 7  1*8= 8  1*9= 9 
            2*2= 4  2*3= 6  2*4= 8  2*5=10  2*6=12  2*7=14  2*8=16  2*9=18 
                    3*3= 9  3*4=12  3*5=15  3*6=18  3*7=21  3*8=24  3*9=27 
                            4*4=16  4*5=20  4*6=24  4*7=28  4*8=32  4*9=36 
                                    5*5=25  5*6=30  5*7=35  5*8=40  5*9=45 
                                            6*6=36  6*7=42  6*8=48  6*9=54 
                                                    7*7=49  7*8=56  7*9=63 
                                                            8*8=64  8*9=72 
                                                                    9*9=81

Java中也有 printf() 语句，用来控制输出格式，不过实际开发中不常用，因为输出到控制台的数据很少要求严格的格式，一般 println() 和
print() 就够了。  
  
println() 输出内容后换行，print() 不换行。  
  
又如，求某一年的某一月有多少天：
```java
    
    
    import java.util.*;
    public class Demo {
        public static void main(String[] args){
            int days = 0;
    
    
        // 获取用户输入
        Scanner sc = new Scanner(System.in);
        System.out.print("输入年份：");
        int year = sc.nextInt();
        System.out.print("输入月份：");
        int month = sc.nextInt();
    
        switch(month){
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                days=31;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                days=30;
                break;
            case 2:
                // 判断闰年
                if(year%4==0 &amp;&amp; year%100!=0 || year%400==0)
                    days=29;
                else
                    days=28;
                break;
            default:
                System.out.println("月份输入错误！");
                System.exit(0);  // 强制结束程序
        }
        System.out.printf("天数：%d\n", days);
    }
    

}


```



运行结果：  
输入年份：2014  
输入月份：02  
天数：28  
  
Java中没有像C语言中的scanf()语句，从控制台获取输入有点麻烦，我推荐使用 Scanner 类，具体语法请大家自行查看API。
