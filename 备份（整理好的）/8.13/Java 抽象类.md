+++
title = "Java 抽象类"
tags = [
"Java",
"Chinese",
]
date = "2022-08-11 23:02:36"
categories = [
"Chinese",
]
+++
# Java 抽象类

如果一个类中没有包含足够的信息来描绘一个具体的对象，这样的类称为抽象类。抽象类无法进行范例化，不能直接使用 new 关键字调用其构造器生成该类的对象。

在 Java 语言中由 abstract 修饰的类叫抽象类，由 abstract 修饰的方法叫抽象方法。



## 1\. Java 抽象类的定义语法

    
    
    abstract class 类名
    {
    abstract int 方法名();
    }
    

抽象方法没有方法体，也就是方法后面是没有大括号及其包含的代码。在抽象类中既可以有抽象方法，也可以有普通方法。

凡是继承这个抽象类的实体子类，都必须要实现所有的抽象方法。



## 2\. Java 抽象类的特点

  * （1）抽象类不能被范例化。
  * （2）构造方法 和 static 方法不能抽象。
  * （3）父类的抽象方法需要在子类中实现。
  * （4）抽象类可以具有指向子类对象的对象引用。

## 3\. Java 抽象类的范例

### 1）定义抽象类：Employee

        
                /**
         * 员工类
         */
        public abstract class Employee {
            protected String name;
            protected boolean gender;
            public Employee(String name, boolean gender){
                this.name=name;
                this.gender=gender;
            }
            /**
            * 领工资操作
            */
            public abstract void getSalary();
        
            public void getName(){
                System.out.println("我是" + name);
            }
        }
        

### 2）继承抽象类：Manager

新建一个经理类 Manager，继承抽象类 Employee。我们必须要重写抽象方法 getSalary。

        
                /**
         * 经理类
         */
        public class Manager extends Employee{
            public Manager(String name,boolean gender){
                super(name,gender);
            }
        
            //重写父类的抽象方法
            public void getSalary(){
                System.out.println("经理领9000元工资");
            }
        }
        

### 3）继承抽象类：Accountant

新建一个会计类 Accountant，继承抽象类 Employee。我们必须要重写抽象方法 getSalary。

        
                /**
         * 会计类
         */
        public class Accountant extends Employee{
            public Accountant(String name,boolean gender){
                super(name,gender);
            }
        
            //重写父类的抽象方法
            public void getSalary(){
                System.out.println("会计领7000元工资");
            }
        }
        

### 4）抽象类测试

        
                public class AbstractTest {
            public static void main(String[] args) {
                Manager manager = new Manager("张经理", true);
                manager.getName();
                manager.getSalary();
        
                Accountant accountant = new Accountant("李会计", false);
                accountant.getName();
                accountant.getSalary();
            }
        }
        

运行执行结果：

        
                $ javac AbstractTest.java
        $ java AbstractTest
        
        我是张经理
        经理领9000元工资
        我是李会计
        会计领7000元工资
        

