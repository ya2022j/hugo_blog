




+++
title = "Java通过反射获取注解信息"
tags = [
"Java",
"Chinese",
]
date = "2022-07-31 22:23:12"
categories = [
"Chinese",
]
+++

#  Java通过反射获取注解信息


使用注解修饰了类、方法、变量等成员之后，这些注解不会自己生效，必须由开发者提供相应的工具来提取处理。要想获取类、方法或变量的注解信息，必须通过 Java 的反射技术来获取 Annotation 对象，除此之外没有其它方法。




  
下面主要介绍 Java 基于反射机制获取注解的方法，并以结合实例的方式讲解了获取注解信息的具体实现方法与操作事项。  
  
所有 Java 注解类型都继承于 java.lang.annotation.Annotation
接口，该接口代表程序中可以接收注解的程序元素。该接口主要有如下几个实现类。

  * Class：类定义
  * Constructor：构造方法定义
  * Field：类的成员变量定义
  * Method：类的方法定义
  * Package：类的包定义

  
java.lang.reflect 包下主要包含一些实现反射功能的工具类，从 Java 5 开始，java.lang.reflect 包所提供的反射 API
增加了读取运行时注解的能力。只有当定义注解时使用了 @Retention(RetentionPolicy.RUNTIME) 修饰，该注解才会在运行时可见。  
  
AnnotatedElement 接口是所有程序元素（如 Class、Method、Constructor 等）的父接口，所以程序通过反射获取了某个类的
AnnotatedElement 对象（如 Class、Method、 Constructor
等）之后，程序就可以调用该对象的如下几个方法来访问注解信息，方法名称及作用如下表所示。  
  

方法名 |  作用  
---|---  
<A extends Annotation> A getAnnotation(Class<A> annotationClass) |  如果该元素存在
annotationClass 类型的注解，则返回注解，否则返回 null  
<A extends Annotation> A getDeclaredAnnotation(Class<A> annotationClass) |  这是
Java 8 新增的方法，该方法尝试获取直接修饰该程序元素、指定类型的注解。如果该类型的注解不存在，则返回 null  
Annotation[] getAnnotations() |  返回该元素上存在的所有注解  
Annotation[] getDeclaredAnnotations() |  返回直接存在于该元素的所有注解（和 getAnnotations()
的区别在于该方法将不返回继承的注释）  
boolean isAnnotationPresent(Class<? extends Annotation> annotationClass) |
判断该元素上是否存在 annotationClass 类型的注解，如果存在则返回 true，否则返回 false。  
<A extends Annotation> A[] getAnnotationsByType(Class<A> annotationClass) |
该方法与前面介绍的 getAnnotation() 方法基本相似。但由于 Java 8 增加了重复注解功能，因此需要使用该方法获取该元素存在
annotationClass 类型的多个注解。  
<A extends Annotation> A[] getDeclaredAnnotationsByType(Class<A>
annotationClass) |  该方法与前面介绍的 getDeclaredAnnotations() 方法基本相似。但由于 Java 8
增加了重复注解功能，因此需要使用该方法获取该元素存在 annotationClass 类型的多个注解。  
根据官方的命名规则，可以总结出以下几条：

  1. getDeclaredAnnotationXXXX：只可以获取直接存在的注解信息，即直接修饰在某个元素（类、属性和方法）上的注解。
  2. getXXXXByType：可以获取间接存在的注解信息
  3. getAnnotationXXX：可以获取继承的注解信息

  
注意：所有的方法都可以获取直接注解信息

####  示例 1

在 SpringMVC 中，经常使用 <code>@RequestMapping(value="")</code> 注解，这样 Spring
就会将我们填写的 value 值当作路径存放在 map 结构中让我们访问。下面我们使用 getAnnotation() 方法来实现这个功能，代码如下。

    
    
    /**

  * 这是自定义注解的类 */ @Target({ ElementType.TYPE, ElementType.METHOD }) @Retention(RetentionPolicy.RUNTIME) @Documented public @interface MyRequestMapping { String value(); // 这是注解的一个属性字段，也就是在使用注解时填写在括号里的参数 }</pre> 创建 TestController 类，然后在 TestController 类中使用 @MyRequestMapping 注解，代码如下：
    




```java
        @MyRequestMapping("/test")
    public class TestController {
      public void test() {
    
          System.out.println("进入Test方法");
    

} }


```

 
 
 测试类代码如下：

```java
        public class Test {
      public static void main(String[] args) {
    
          Class&lt;?&gt; c = TestController.class;
      MyRequestMapping baseRequestMapping = c.getAnnotation(MyRequestMapping.class);
      System.out.println(baseRequestMapping.value()); // 输出value的值
    

} }


```



输出结果为`/test`。  
  
注意：Class<?> 中的 <?> 是必须写的，你可以把`?`改成要限定的类型，但是必须要写这个泛型限定才行，否则会编译错误。

####  示例 2

下面我们使用 getAnnotations() 方法获取多个注解，并输出。  
  
1）自定义 Person 注解，代码如下：
```java
        @Target({ ElementType.TYPE })
    @Inherited
    @Retention(RetentionPolicy.RUNTIME)
    public @interface Person {
      String value();
    }
```

2）修改例 1 中的 TestController 类，代码如下：
```java
    
        @MyRequestMapping("/test")
    @Person("C")
    public class TestController {
      public void test() {
    
    
    
    
          System.out.println("进入Test方法");
    

} }


```

 
 3）创建测试类，获取 TestController 类里的所有注解，并将这些注解打印出来。代码如下所示：

   ```java 
        public class Test {
      public static void main(String[] args) {
    
          Class&lt;?&gt; c = TestController.class;
      Annotation[] atnsArray = c.getAnnotations();
      for (Annotation an : atnsArray) {
          System.out.println(an);
      }
    

} }

```

 
 输出结果为：

@MyRequestMapping(value=/test)  
@Person(value=C)


