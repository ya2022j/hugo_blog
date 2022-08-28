
+++
title = "Java泛型详解，通俗易懂只需5分钟"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:10"
categories = [
"Chinese",
]
+++
# Java泛型详解，通俗易懂只需5分钟




我们知道，使用变量之前要定义，定义一个变量时必须要指明它的数据类型，什么样的数据类型赋给什么样的值。

    




  * 泛型是 Java 1.5 的新增特性，它以C++模板为参照，本质是参数化类型(Parameterized Type)的应用。
  * 类型参数只能用来表示引用类型，不能用来表示基本类型，如 int、double、char 等。但是传递基本类型不会报错，因为它们会自动装箱成对应的包装类。

##  泛型方法

除了定义泛型类，还可以定义泛型方法，例如，定义一个打印坐标的泛型方法：

```java

    
    
    public class Demo {
        public static void main(String[] args){
            // 实例化泛型类
            Point<Integer, Integer> p1 = new Point<Integer, Integer>();
            p1.setX(10);
            p1.setY(20);
            p1.printPoint(p1.getX(), p1.getY());
    
    
        Point&lt;Double, String&gt; p2 = new Point&lt;Double, String&gt;();
        p2.setX(25.4);
        p2.setY("东京180度");
        p2.printPoint(p2.getX(), p2.getY());
    }
    

}

// 定义泛型类 class Point<T1, T2>{ T1 x; T2 y; public T1 getX() { return x; }
public void setX(T1 x) { this.x = x; } public T2 getY() { return y; } public
void setY(T2 y) { this.y = y; }

    
    
    // 定义泛型方法
    public &lt;T1, T2&gt; void printPoint(T1 x, T2 y){
        T1 m = x;
        T2 n = y;
        System.out.println("This point is：" + m + ", " + n);
    }
    

}
```



 运行结果：  
This point is：10, 20  
This point is：25.4, 东京180度  
  
上面的代码中定义了一个泛型方法
printPoint()，既有普通参数，也有类型参数，类型参数需要放在修饰符后面、返回值类型前面。一旦定义了类型参数，就可以在参数列表、方法体和返回值类型中使用了。  
  
与使用泛型类不同，使用泛型方法时不必指明参数类型，编译器会根据传递的参数自动查找出具体的类型。泛型方法除了定义不同，调用就像普通方法一样。  
  
注意：泛型方法与泛型类没有必然的联系，泛型方法有自己的类型参数，在普通类中也可以定义泛型方法。泛型方法 printPoint() 中的类型参数 T1, T2
与泛型类 Point 中的 T1, T2 没有必然的联系，也可以使用其他的标识符代替：

    
```java

    public static <V1, V2> void printPoint(V1 x, V2 y){
        V1 m = x;
        V2 n = y;
        System.out.println("This point is：" + m + ", " + n);
    }
```
##  泛型接口

在Java中也可以定义泛型接口，这里不再赘述，仅仅给出示例代码：
```java

    
    public class Demo {
        public static void main(String arsg[]) {
            Info<String> obj = new InfoImp<String>("www.itbenkyou.net");
            System.out.println("Length Of String: " + obj.getVar().length());
        }
    }

//定义泛型接口 interface Info<T> { public T getVar(); }

//实现接口 class InfoImp<T> implements Info<T> { private T var;

    
    
    // 定义泛型构造方法
    public InfoImp(T var) {
        this.setVar(var);
    }
    
    public void setVar(T var) {
        this.var = var;
    }
    
    public T getVar() {
        return this.var;
    }
    

}

```



运行结果：  
Length Of String: 18

##  类型擦除

如果在使用泛型时没有指明数据类型，那么就会擦除泛型类型，请看下面的代码：

```java

    
    public class Demo {
        public static void main(String[] args){
            Point p = new Point();  // 类型擦除
            p.setX(10);
            p.setY(20.8);
            int x = (Integer)p.getX();  // 向下转型
            double y = (Double)p.getY();
            System.out.println("This point is：" + x + ", " + y);
        }
    }

class Point<T1, T2>{ T1 x; T2 y; public T1 getX() { return x; } public void
setX(T1 x) { this.x = x; } public T2 getY() { return y; } public void setY(T2
y) { this.y = y; } }

```


运行结果：  
This point is：10, 20.8  
  
因为在使用泛型时没有指明数据类型，为了不出现错误，编译器会将所有数据向上转型为
Object，所以在取出坐标使用时要向下转型，这与本文一开始不使用泛型没什么两样。  

##  限制泛型的可用类型

在上面的代码中，类型参数可以接受任意的数据类型，只要它是被定义过的。但是，很多时候我们只需要一部分数据类型就够了，用户传递其他数据类型可能会引起错误。例如，编写一个泛型函数用于返回不同类型数组（Integer
数组、Double 数组、Character 数组等）中的最大值：

```java

    public <T> T getMax(T array[]){
        T max = null;
        for(T element : array){
            max = element.doubleValue() > max.doubleValue() ? element : max;
        }
        return max;
    }
```

上面的代码会报错，doubleValue() 是 Number 类的方法，不是所有的类都有该方法，所以我们要限制类型参数 T，让它只能接受 Number
及其子类（Integer、Double、Character 等）。  
  
通过 extends 关键字可以限制泛型的类型，改进上面的代码：

```java
    
    
    public <T extends Number> T getMax(T array[]){
        T max = null;
        for(T element : array){
            max = element.doubleValue() > max.doubleValue() ? element : max;
        }
        return max;
    }
```


<T extends Number> 表示 T 只接受 Number 及其子类，传入其他类型的数据会报错。这里的限定使用关键字
extends，后面可以是类也可以是接口。但这里的 extends 已经不是继承的含义了，应该理解为 T 是继承自 Number 类的类型，或者 T
是实现了 XX 接口的类型。  
  
注意：一般的应用开发中泛型使用较少，多用在框架或者库的设计中，这里不再深入讲解，主要让大家对泛型有所认识，为后面的教程做铺垫。
