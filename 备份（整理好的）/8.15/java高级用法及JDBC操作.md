# Java Applet 基础

Applet 是一种 Java 程序。它一般运行在支持 Java 的 Web 浏览器内。因为它有完整的 Java API 支持，所以 Applet
是一个全功能的 Java 应用程序。

如下所示是独立的 Java 应用程序和 applet 程序之间重要的不同：

  * Java 中 Applet 类继承了 java.applet.Applet 类。
  * Applet 类没有定义 main()，所以一个 Applet 程序不会调用 main() 方法。
  * Applet 被设计为嵌入在一个 HTML 页面。
  * 当用户浏览包含 Applet 的 HTML 页面，Applet 的代码就被下载到用户的机器上。
  * 要查看一个 Applet 需要 JVM。 JVM 可以是 Web 浏览器的一个插件，或一个独立的运行时环境。
  * 用户机器上的 JVM 创建一个 Applet 类的范例，并调用 Applet 生命周期过程中的各种方法。
  * Applet 有 Web 浏览器强制执行的严格的安全规则，Applet 的安全机制被称为沙箱安全。
  * Applet 需要的其他类可以用 Java 归档（JAR）文件的形式下载下来。



## 1\. Applet 的生命周期

Applet 类中的四个方法给我们提供了一个框架，你可以在该框架上开发小程序：

  * **init:** 该方法的目的是为你的 Applet 提供所需的任何初始化。在 Applet 标记内的 param 标签被处理后调用该方法。
  * **start:** 浏览器调用 init 方法后，该方法被自动调用。每当用户从其他页面返回到包含 Applet 的页面时，则调用该方法。
  * **stop:** 当用户从包含 Applet 的页面移除的时候，该方法自动被调用。因此，可以在相同的 Applet 中反复调用该方法。
  * **destroy:** 此方法仅当浏览器正常关闭时调用。因为 Applet 只有在 HTML 网页上有效，所以你不应该在用户离开包含 Applet 的页面后遗漏任何资源。
  * **paint:** 该方法在 start() 方法之后立即被调用，或者在 Applet 需要重绘在浏览器的时候调用。paint() 方法实际上继承于 java.awt。



## 2\. "Hello, World" Applet:

下面是一个简单的 Applet 程序 HelloWorldApplet.java:


```java
import java.applet.*;
import java.awt.*;
 
    public class HelloWorldApplet extends Applet
    {
        public void paint (Graphics g)
        {
            g.drawString ("Hello World", 25, 50);
        }
    }
```




这些 import 语句将以下类导入到我们的 Applet 类中：


```java
java.applet.Applet.
java.awt.Graphics.
```


没有这些 import 语句，Java 编译器就识别不了 Applet 和 Graphics 类。



## 3\. Applet 类

每一个 Applet 都是 java.applet.Applet 类的子类，基础的 Applet
类提供了供衍生类调用的方法,以此来得到浏览器上下文的信息和服务。

这些方法做了如下事情：

  * 得到 Applet 的参数
  * 得到包含 Applet 的 HTML 文件的网络位置
  * 得到 Applet 类目录的网络位置
  * 打印浏览器的状态信息
  * 获取一张图片
  * 获取一个音频片段
  * 播放一个音频片段
  * 调整此 Applet 的大小

除此之外，Applet 类还提供了一个接口，该接口供 Viewer 或浏览器来获取 Applet 的信息，并且来控制 Applet 的执行。

Viewer 可能是：

  * 请求 Applet 作者、版本和版权的信息
  * 请求 Applet 识别的参数的描述
  * 初始化 Applet
  * 销毁 Applet
  * 开始执行 Applet
  * 结束执行 Applet

Applet 类提供了对这些方法的默认实现，这些方法可以在需要的时候重写。

"Hello，World"applet 都是按标准编写的。唯一被重写的方法是 paint 方法。



## 4\. Applet 的调用

Applet 是一种 Java 程序。它一般运行在支持 Java 的 Web 浏览器内。因为它有完整的 Java API 支持,所以 Applet
是一个全功能的 Java 应用程序。

<applet> 标签是在HTML文件中嵌入 Applet 的基础。以下是一个调用 "Hello World" applet 的例子；

```html
    <html>
        <title>The Hello, World Applet</title>
        <hr>
        <applet code="HelloWorldApplet.class" width="320" height="120">
        If your browser was Java-enabled, a "Hello, World"
        message would appear here.
        </applet>
        <hr>
    </html>
```




**注意:** 你可以参照 HTML Applet 标签来更多的了解从 HTML 中调用 applet 的方法。

<applet> 标签的属性指定了要运行的 Applet 类。width 和 height 用来指定 Applet 运行面板的初始大小。Applet
必须使用 </applet> 标签来关闭。


如果 Applet 接受参数，那么参数的值需要在 <param> 标签里添加，该标签位于 <applet> 和 </applet> 之间。浏览器忽略了
applet 标签之间的文本和其他标签。

不支持 Java 的浏览器不能执行 <applet> 和 </applet>。因此，在标签之间显示并且和 applet 没有关系的任何东西，在不支持的
Java 的浏览器里是可见的。

Viewer 或者浏览器在文档的位置寻找编译过的 Java 代码，要指定文档的路径，得使用 <applet> 标签的 codebase 属性指定。

如下所示：

   ```html
    <applet codebase="http://amrood.com/applets"
       code="HelloWorldApplet.class" width="320" height="120">
   ```






如果 Applet 所在一个包中而不是默认包，那么所在的包必须在 code 属性里指定，例如：

   ```html
     <applet code="mypackage.subpackage.TestApplet.class"
                  width="320" height="120">
   ```






## 5\. 获得applet参数

下面的例子演示了如何使用一个 Applet 响应来设置文件中指定的参数。该 Applet 显示了一个黑色棋盘图案和第二种颜色。

第二种颜色和每一列的大小通过文档中的 Applet 的参数指定。

CheckerApplet 在 init() 方法里得到它的参数。也可以在 paint() 方法里得到它的参数。然而，在 Applet
开始得到值并保存了设置，而不是每一次刷新的时候都得到值，这样是很方便，并且高效的。

Applet viewer 或者浏览器在 Applet 每次运行的时候调用 init() 方法。在加载 Applet 之后，Viewer 立即调用
init() 方法（Applet.init()什么也没做），重写该方法的默认实现，添加一些自定义的初始化代码。

Applet.getParameter() 方法通过给出参数名称得到参数值。如果得到的值是数字或者其他非字符数据，那么必须解析为字符串类型。

```java
mport java.applet.*;
import java.awt.*;
public class CheckerApplet extends Applet
{
    int squareSize = 50;// 初始化默认大小
    public void init () {}
    private void parseSquareSize (String param) {}
    private Color parseColor (String param) {}
    public void paint (Graphics g) {}
}
```


下面是 CheckerApplet 类的 init() 方法和私有的 parseSquareSize() 方法：


​    

```java
public void init ()
{
    String squareSizeParam = getParameter ("squareSize");
    parseSquareSize (squareSizeParam);
    String colorParam = getParameter ("color");
    Color fg = parseColor (colorParam);
    setBackground (Color.black);
    setForeground (fg);
}

private void parseSquareSize (String param)
{
    if (param == null) return;
    try {
        squareSize = Integer.parseInt (param);
    }
    catch (Exception e) {
        // 保留默认值
    }
}
```


该 Applet 调用 parseSquareSize()，来解析 squareSize 参数。parseSquareSize() 调用了库方法
Integer. parseInt() 该方法将一个字符串解析为一个整数，当参数无效的时候，Integer.parseInt() 抛出异常。

因此，parseSquareSize() 方法也是捕获异常的，并不允许 Applet 接受无效的输入。

Applet 调用 parseColor()方法将颜色参数解析为一个 Color 值。parseColor()
方法做了一系列字符串的比较，来匹配参数的值和预定义颜色的名字。你需要实现这些方法来使 Applet 工作。



## 6\. 指定 applet 参数

如下的例子是一个HTML文件，其中嵌入了 CheckerApplet 类。HTML文件通过使用 <param> 标签的方法给 applet 指定了两个参数。

  ```html
      <html>
      <title>Checkerboard Applet</title>
      <hr>
      <applet code="CheckerApplet.class" width="480" height="320">
      <param name="color" value="blue">
      <param name="squaresize" value="30">
      </applet>
      <hr>
      </html>
  ```




**注意:** 参数名字大小写不敏感。



## 7\. 应用程序转换成 Applet

将图形化的 Java 应用程序（是指，使用AWT的应用程序和使用 java 程序启动器启动的程序）转换成嵌入在web页面里的applet是很简单的。

下面是将应用程序转换成 Applet 的几个步骤：

  * 编写一个 HTML 页面，该页面带有能加载 applet 代码的标签。
  * 编写一个 JApplet 类的子类，将该类设置为 public。否则，Applet 不能被加载。
  * 消除应用程序的 main()方法。不要为应用程序构造框架窗口，因为你的应用程序要显示在浏览器中。
  * 将应用程序中框架窗口的构造方法里的初始化代码移到 Applet 的 init() 方法中，你不必显示的构造 Applet 对象，浏览器将通过调用 init() 方法来范例化一个对象。
  * 移除对 setSize() 方法的调用，对于 Applet 来讲，大小已经通过 HTML 文件里的 width 和 height 参数设定好了。
  * 移除对 setDefaultCloseOperation() 方法的调用。Applet 不能被关闭，它随着浏览器的退出而终止。
  * 如果应用程序调用了 setTitle() 方法，消除对该方法的调用。applet 不能有标题栏。（当然你可以给通过 html 的 title 标签给网页自身命名）
  * 不要调用 setVisible(true),Applet 是自动显示的。



## 8\. 事件处理

Applet 类从 Container 类继承了许多事件处理方法。Container 类定义了几个方法，例如：processKeyEvent()
和processMouseEvent()，用来处理特别类型的事件，还有一个捕获所有事件的方法叫做 processEvent。

为了响应一个事件，Applet 必须重写合适的事件处理方法。


​             

```java
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import java.applet.Applet;
    import java.awt.Graphics;
        
    public class ExampleEventHandling extends Applet
                                    implements MouseListener {
StringBuffer strBuffer;
    
    public void init() {
            addMouseListener(this);
            strBuffer = new StringBuffer();
        addItem("initializing the applet ");
    }
    
    public void start() {
        addItem("starting the applet ");
    }
    
    public void stop() {
        addItem("stopping the applet ");
    }
    
    public void destroy() {
        addItem("unloading the applet");
    }
    
    void addItem(String word) {
        System.out.println(word);
        strBuffer.append(word);
        repaint();
    }
    
    public void paint(Graphics g) {
            //Draw a Rectangle around the applet's display area.
        g.drawRect(0, 0,
                        getWidth() - 1,
                        getHeight() - 1);
    
            //display the string inside the rectangle.
        g.drawString(strBuffer.toString(), 10, 20);
    }
    
    public void mouseEntered(MouseEvent event) {
    }
    public void mouseExited(MouseEvent event) {
    }
    public void mousePressed(MouseEvent event) {
    }
    public void mouseReleased(MouseEvent event) {
    }
    public void mouseClicked(MouseEvent event) {
            addItem("mouse clicked! ");
    }
}
```


如下调用该 Applet：


```html
<html>
<title>Event Handling</title>
<hr>
<applet code="ExampleEventHandling.class"
width="300" height="300">
</applet>
<hr>
</html>
```


最开始运行，Applet 显示 "initializing the applet. Starting the applet."，然后你一点击矩形框，就会显示
"mouse clicked" 。



## 9\. 显示图片

Applet 能显示 GIF,JPEG,BMP 等其他格式的图片。为了在 Applet 中显示图片，你需要使用 java.awt.Graphics
类的drawImage()方法。

如下范例演示了显示图片的所有步骤：


​    
```java
import java.applet.*;
import java.awt.*;
import java.net.*;
public class ImageDemo extends Applet
{
    private Image image;
    private AppletContext context;
    public void init()
    {
        context = this.getAppletContext();
        String imageURL = this.getParameter("image");
        if(imageURL == null)
        {
            imageURL = "java.jpg";
        }
        try
        {
            URL url = new URL(this.getDocumentBase(), imageURL);
            image = context.getImage(url);
        }catch(MalformedURLException e)
        {
            e.printStackTrace();
            // Display in browser status bar
            context.showStatus("Could not load image!");
        }
    }
    public void paint(Graphics g)
    {
        context.showStatus("Displaying image");
        g.drawImage(image, 0, 0, 200, 84, null);
    } 
}    
```


如下调用该applet：


​    
```html
<html>
<title>The ImageDemo applet</title>
<hr>
<applet code="ImageDemo.class" width="300" height="200">
<param name="image" value="java.jpg">
</applet>
<hr>
</html>
```




## 10\. 播放音频

Applet 能通过使用 java.applet 包中的 AudioClip 接口播放音频。AudioClip 接口定义了三个方法：

  * **public void play():** 从一开始播放音频片段一次。
  * **public void loop():** 循环播放音频片段
  * **public void stop():** 停止播放音频片段

为了得到 AudioClip 对象，你必须调用 Applet 类的 getAudioClip() 方法。无论 URL
指向的是否是一个真实的音频文件，该方法都会立即返回结果。

直到要播放音频文件时，该文件才会下载下来。

如下范例演示了播放音频的所有步骤：


​    
```java
import java.applet.*;
import java.awt.*;
import java.net.*;
public class AudioDemo extends Applet
{
    private AudioClip clip;
    private AppletContext context;
    public void init()
    {
        context = this.getAppletContext();
        String audioURL = this.getParameter("audio");
        if(audioURL == null)
        {
            audioURL = "default.au";
        }
        try
        {
            URL url = new URL(this.getDocumentBase(), audioURL);
            clip = context.getAudioClip(url);
        }catch(MalformedURLException e)
        {
            e.printStackTrace();
            context.showStatus("Could not load audio file!");
        }
    }
    public void start()
    {
        if(clip != null)
        {
            clip.loop();
        }
    }
    public void stop()
    {
        if(clip != null)
        {
            clip.stop();
        }
    }
}
```


如下调用applet：


​    
```html
<html>
<title>The ImageDemo applet</title>
<hr>
<applet code="ImageDemo.class" width="0" height="0">
<param name="audio" value="test.wav">
</applet>
<hr>
</html>
```


你可以使用你电脑上的 test.wav 来测试上面的范例。



+++

# Java ArrayList

ArrayList 类是一个可以动态修改的数组，与 Java 中的普通数组相比，它的容量可以动态改变，没有固定大小的限制，能够添加或者删除元素。

ArrayList 继承了 AbstractList ，并实现了 List 接口。

ArrayList 类位于 java.util 包中，使用前需要引入它，语法格式如下：


​    
```java
import java.util.ArrayList; // 引入 ArrayList 类

ArrayList<E> objectName =new ArrayList<>();　 // 初始化
```


  * **E** : 泛型数据类型，用于设置 objectName 的数据类型， **只能为引用数据类型** 。
  * **objectName** : 对象名。

ArrayList 是一个数组队列，提供了相关的添加、删除、修改、遍历等功能。



## 1\. 添加元素

ArrayList 类提供了很多有用的方法，添加元素到 ArrayList 可以使用 add() 方法:

  


```java
import java.util.ArrayList;
public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


```java
[Google, Codebaoku, Taobao, Weibo]
```



## 2\. 访问元素

访问 ArrayList 中的元素可以使用 get() 方法：


​    

```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        System.out.println(sites.get(1));  // 访问第二个元素
    }
}
```

**注意** ：数组的索引值从 0 开始。

以上范例，执行输出结果为：


​    
```java
Codebaoku
```



## 3\. 修改元素

如果要修改 ArrayList 中的元素可以使用 set() 方法：


​    
```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        sites.set(2, "Wiki"); // 第一个参数为索引位置，第二个为要修改的值
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    
```java
[Google, Codebaoku, Wiki, Weibo]
```




## 4\. 删除元素

如果要删除 ArrayList 中的元素可以使用 remove() 方法：


​    
```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        sites.remove(3); // 删除第四个元素
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    
```java
[Google, Codebaoku, Taobao]
```




## 5\. 计算大小

如果要计算 ArrayList 中的元素数量可以使用 size() 方法：


​    
```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        System.out.println(sites.size());
    }
}
```


以上范例，执行输出结果为：


​    
```java
4
```



## 6\. 迭代数组列表

我们可以使用 for 来迭代数组列表中的元素：

```java
    import java.util.ArrayList;
 
    public class CodebaokuTest {
        public static void main(String[] args) {
            ArrayList<String> sites = new ArrayList<String>();
            sites.add("Google");
            sites.add("Codebaoku");
            sites.add("Taobao");
            sites.add("Weibo");
            for (int i = 0; i < sites.size(); i++) {
                System.out.println(sites.get(i));
            }
        }
    }

```



以上范例，执行输出结果为：


​    
```java
Google
Codebaoku
Taobao
Weibo
```


也可以使用 for-each 来迭代元素：


```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        for (String i : sites) {
            System.out.println(i);
        }
    }
}
```


以上范例，执行输出结果为：


​    
```java
Google
Codebaoku
Taobao
Weibo
```




## 7\. 其他的引用类型

ArrayList 中的元素实际上是对象，在以上范例中，数组列表元素都是字符串 String 类型。

如果我们要存储其他类型，而 <E> 只能为引用数据类型，这时我们就需要使用到基本类型的包装类。

基本类型对应的包装类表如下：

| 基本类型 | 引用类型  |
| -------- | --------- |
| boolean  | Boolean   |
| byte     | Byte      |
| short    | Short     |
| int      | Integer   |
| long     | Long      |
| float    | Float     |
| double   | Double    |
| char     | Character |

此外，BigInteger、BigDecimal 用于高精度的运算，BigInteger 支持任意精度的整数，也是引用类型，但它们没有相对应的基本类型。


​    
```java
ArrayList<Integer> li=new Arraylist<>();     // 存放整数元素
ArrayList<Character> li=new Arraylist<>();   // 存放字符元素
```

以下范例使用 ArrayList 存储数字(使用 Integer 类型):


​    
```java
import java.util.ArrayList;

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<Integer> myNumbers = new ArrayList<Integer>();
        myNumbers.add(10);
        myNumbers.add(15);
        myNumbers.add(20);
        myNumbers.add(25);
        for (int i : myNumbers) {
            System.out.println(i);
        }
    }
}
```


以上范例，执行输出结果为：


​    
```java
10
15
20
25
```



## 8\. ArrayList 排序

Collections 类也是一个非常有用的类，位于 java.util 包中，提供的 sort() 方法可以对字符或数字列表进行排序。

以下范例对字母进行排序：


​    
```java
import java.util.ArrayList;
import java.util.Collections;  // 引入 Collections 类

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<String> sites = new ArrayList<String>();
        sites.add("Taobao");
        sites.add("Wiki");
        sites.add("Codebaoku");
        sites.add("Weibo");
        sites.add("Google");
        Collections.sort(sites);  // 字母排序
        for (String i : sites) {
            System.out.println(i);
        }
    }
}
```


以上范例，执行输出结果为：


​    
```java
Google
Codebaoku
Taobao
Weibo
Wiki
```


以下范例对数字进行排序：


​    
```java
    import java.util.ArrayList;
import java.util.Collections;  // 引入 Collections 类

public class CodebaokuTest {
    public static void main(String[] args) {
        ArrayList<Integer> myNumbers = new ArrayList<Integer>();
        myNumbers.add(33);
        myNumbers.add(15);
        myNumbers.add(20);
        myNumbers.add(34);
        myNumbers.add(8);
        myNumbers.add(12);

        Collections.sort(myNumbers);  // 数字排序
                for (int i : myNumbers) {
            System.out.println(i);
        }
    }
}
```




以上范例，执行输出结果为：


​    
```java
8
12
15
20
33
34
```




## 10\. Java ArrayList 方法

Java ArrayList 常用方法列表如下：

| 方法             | 描述                                          |
| ---------------- | --------------------------------------------- |
| add()            | 将元素插入到指定位置的 arraylist 中           |
| addAll()         | 添加集合中的所有元素到 arraylist 中           |
| clear()          | 删除 arraylist 中的所有元素                   |
| clone()          | 复制一份 arraylist                            |
| contains()       | 判断元素是否在 arraylist                      |
| get()            | 通过索引值获取 arraylist 中的元素             |
| indexOf()        | 返回 arraylist 中元素的索引值                 |
| removeAll()      | 删除存在于指定集合中的 arraylist 里的所有元素 |
| remove()         | 删除 arraylist 里的单个元素                   |
| size()           | 返回 arraylist 里元素数量                     |
| isEmpty()        | 判断 arraylist 是否为空                       |
| subList()        | 截取部分 arraylist 的元素                     |
| set()            | 替换 arraylist 中指定索引的元素               |
| sort()           | 对 arraylist 元素进行排序                     |
| toArray()        | 将 arraylist 转换为数组                       |
| toString()       | 将 arraylist 转换为字符串                     |
| ensureCapacity() | 设置指定容量大小的 arraylist                  |
| lastIndexOf()    | 返回指定元素在 arraylist 中最后一次出现的位置 |
| retainAll()      | 保留 arraylist 中在指定集合中也存在的那些元素 |
| containsAll()    | 查看 arraylist 是否包含指定集合中的所有元素   |
| trimToSize()     | 将 arraylist 中的容量调整为数组中的元素个数   |
| removeRange()    | 删除 arraylist 中指定索引之间存在的元素       |
| replaceAll()     | 将给定的操作内容替换掉数组中每一个元素        |
| removeIf()       | 删除所有满足特定条件的 arraylist 元素         |
| forEach()        | 遍历 arraylist 中每一个元素并执行特定操作     |



# Java ByteArrayInputStream 类

ByteArrayInputStream 字节数组输入流在内存中创建一个字节数组缓冲区，从输入流读取的数据保存在该字节数组缓冲区中。



## 1\. ByteArrayInputStream 创建方式

创建字节数组输入流对象有以下几种方式。

接收字节数组作为参数创建：


​    
```java
ByteArrayInputStream bArray = new ByteArrayInputStream(byte [] a);
```


另一种创建方式是接收一个字节数组，和两个整形变量 off、len，off表示第一个读取的字节，len表示读取字节的长度。


​    
```java
ByteArrayInputStream bArray = new ByteArrayInputStream(byte []a, int off, int len)
```




## 2\. ByteArrayInputStream 操作方法

成功创建字节数组输入流对象后，可以参见以下列表中的方法，对流进行读操作或其他操作。

| 序号                                          | 方法描述                                        |
| --------------------------------------------- | ----------------------------------------------- |
| 1                                             | **public int read()         **                  |
| 从此输入流中读取下一个数据字节。              |                                                 |
| 2                                             | **public int read(byte[] r, int off, int len)** |
| 将最多 len 个数据字节从此输入流读入字节数组。 |                                                 |
| 3                                             | **public int available()**                      |
| 返回可不发生阻塞地从此输入流读取的字节数。    |                                                 |
| 4                                             | **public void mark(int read)**                  |
| 设置流中的当前标记位置。                      |                                                 |
| 5                                             | **public long skip(long n)**                    |
| 从此输入流中跳过 n 个输入字节。               |                                                 |



## 3\. ByteArrayInputStream 范例

下面的例子演示了ByteArrayInputStream 和 ByteArrayOutputStream的使用：


​    




```java
import java.io.*;
public class ByteStreamTest {

   public static void main(String args[])throws IOException {

      ByteArrayOutputStream bOutput = new ByteArrayOutputStream(12);

      while( bOutput.size()!= 10 ) {
         // 获取用户输入值
         bOutput.write(System.in.read());
      }

      byte b [] = bOutput.toByteArray();
      System.out.println("Print the content");
      for(int x= 0 ; x < b.length; x++) {
         // 打印字符
         System.out.print((char)b[x]  + "   ");
      }
      System.out.println("   ");

      int c;

      ByteArrayInputStream bInput = new ByteArrayInputStream(b);

      System.out.println("Converting characters to Upper case " );
      for(int y = 0 ; y < 1; y++ ) {
         while(( c= bInput.read())!= -1) {
            System.out.println(Character.toUpperCase((char)c));
         }
         bInput.reset();
      }
   }
}
```


以上实例编译运行结果如下：


​    
```java
asdfghjkly
Print the content
a   s   d   f   g   h   j   k   l   y
Converting characters to Upper case
A
S
D
F
G
H
J
K
L
Y
```




# Java ByteArrayOutputStream 类

ByteArrayOutputStream
字节数组输出流在内存中创建一个字节数组缓冲区，所有发送到输出流的数据保存在该字节数组缓冲区中。创建字节数组输出流对象有以下几种方式。



## 1\. ByteArrayOutputStream 创建方式

下面的构造方法创建一个32字节（默认大小）的缓冲区。


​    
```java
OutputStream bOut = new ByteArrayOutputStream();
```


另一个构造方法创建一个大小为 **a** 字节的缓冲区。


​    
```java
OutputStream bOut = new ByteArrayOutputStream(int a)
```




## 2\. ByteArrayOutputStream 操作方法

成功创建字节数组输出流对象后，可以参见以下列表中的方法，对流进行写操作或其他操作。

| 序号                                                         | 方法描述                                          |
| ------------------------------------------------------------ | ------------------------------------------------- |
| 1                                                            | **public void reset()**                           |
| 将此字节数组输出流的 count 字段重置为零，从而丢弃输出流中目前已累积的所有数据输出。 |                                                   |
| 2                                                            | **public byte[] toByteArray()**                   |
| 创建一个新分配的字节数组。数组的大小和当前输出流的大小，内容是当前输出流的拷贝。 |                                                   |
| 3                                                            | **public String toString()**                      |
| 将缓冲区的内容转换为字符串，根据平台的默认字符编码将字节转换成字符。 |                                                   |
| 4                                                            | **public void write(int w)**                      |
| 将指定的字节写入此字节数组输出流。                           |                                                   |
| 5                                                            | **public void write(byte []b, int off, int len)** |
| 将指定字节数组中从偏移量 off 开始的 len 个字节写入此字节数组输出流。 |                                                   |
| 6                                                            | **public void writeTo(OutputStream outSt)**       |
| 将此字节数组输出流的全部内容写入到指定的输出流参数中。       |                                                   |



## 3\. ByteArrayOutputStream 范例

下面的例子演示了 ByteArrayInputStream 和 ByteArrayOutputStream 的使用：


​    

```java
import java.io.*;

public class ByteStreamTest {
   public static void main(String args[])throws IOException {
      ByteArrayOutputStream bOutput = new ByteArrayOutputStream(12);
      while( bOutput.size()!= 10 ) {
         // 获取用户输入
         bOutput.write(System.in.read()); 
      }
      byte b [] = bOutput.toByteArray();
      System.out.println("Print the content");
      for(int x= 0 ; x < b.length; x++) {
         // 打印字符
         System.out.print((char)b[x]  + "   "); 
      }
      System.out.println("   ");
      int c;
      ByteArrayInputStream bInput = new ByteArrayInputStream(b);
      System.out.println("Converting characters to Upper case " );
      for(int y = 0 ; y < 1; y++ ) {
         while(( c= bInput.read())!= -1) {
            System.out.println(Character.toUpperCase((char)c));
         }
         bInput.reset(); 
      }
   }
}
```


以上实例编译运行结果如下：


​    
```java
asdfghjkly
Print the content
a   s   d   f   g   h   j   k   l   y
Converting characters to Upper case
A
S
D
F
G
H
J
K
L
Y
```






# Java Character 类

Character 类用于对单个字符进行操作。

Character 类在对象中包装一个基本类型 **char** 的值


​    

```java
char ch = 'a';
 
// Unicode 字符表示形式
char uniChar = '\u039A'; 
 
// 字符数组
char[] charArray ={ 'a', 'b', 'c', 'd', 'e' };
```


然而，在实际开发过程中，我们经常会遇到需要使用对象，而不是内置数据类型的情况。为了解决这个问题，Java语言为内置数据类型char提供了包装类Character类。

Character类提供了一系列方法来操纵字符。你可以使用Character的构造方法创建一个Character类对象，例如：


​    

```java
Character ch = new Character('a');
```


在某些情况下，Java编译器会自动创建一个Character对象。

例如，将一个char类型的参数传递给需要一个Character类型参数的方法时，那么编译器会自动地将char类型参数转换为Character对象。
这种特征称为装箱，反过来称为拆箱。



## 1\. 使用 Character 对象的范例

下面是一个使用 Integer 对象的范例：


​    

```java
// 原始字符 'a' 装箱到 Character 对象 ch 中
Character ch = 'a';
 
// 原始字符 'x' 用 test 方法装箱
// 返回拆箱的值到 'c'
char c = test('x');
```




## 2\. 字符转义序列

前面有反斜杠（\）的字符代表转义字符，它对编译器来说是有特殊含义的。

下面列表展示了Java的转义序列：

| 转义序列 | 描述                     |
| -------- | ------------------------ |
| \t       | 在文中该处插入一个tab键  |
| \b       | 在文中该处插入一个后退键 |
| \n       | 在文中该处换行           |
| \r       | 在文中该处插入回车       |
| \f       | 在文中该处插入换页符     |
| \'       | 在文中该处插入单引号     |
| \"       | 在文中该处插入双引号     |
| \\\      | 在文中该处插入反斜杠     |

当打印语句遇到一个转义序列时，编译器可以正确地对其进行解释。

以下范例转义双引号并输出：


​    

```java
public class Test {
 
   public static void main(String[] args) {
      System.out.println("访问\"[编程宝库](http://www.0.com)!\"");
   }
}
```


以上范例编译运行结果如下：


​    

```java
访问"[编程宝库](http://www.0.com)!"
```




## 3\. Character 方法

下面是Character类的方法：

| 序号                                    | 方法与描述     |
| --------------------------------------- | -------------- |
| 1                                       | isLetter()     |
| 是否是一个字母                          |                |
| 2                                       | isDigit()      |
| 是否是一个数字字符                      |                |
| 3                                       | isWhitespace() |
| 是否是一个空白字符                      |                |
| 4                                       | isUpperCase()  |
| 是否是大写字母                          |                |
| 5                                       | isLowerCase()  |
| 是否是小写字母                          |                |
| 6                                       | toUpperCase()  |
| 指定字母的大写形式                      |                |
| 7                                       | toLowerCase()  |
| 指定字母的小写形式                      |                |
| 8                                       | toString()     |
| 返回字符的字符串形式，字符串的长度仅为1 |                |







# Java DataInputStream 类<

数据输入流允许应用程序以与机器无关方式从底层输入流中读取基本 Java 数据类型。



## 1\. DataInputStream 创建方式

下面的构造方法用来创建数据输入流对象。


​    

```java
DataInputStream dis = new DataInputStream(InputStream in);
```




## 2\. DataInputStream 操作方法

| 序号                                                         | 方法描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                                                            | **public final int read(byte[] r, int off, int len)throws IOException** |
| 从所包含的输入流中将 len 个字节读入一个字节数组中。如果len为-1，则返回已读字节数。 |                                                              |
| 2                                                            | **Public final int read(byte [] b)throws IOException**       |
| 从所包含的输入流中读取一定数量的字节，并将它们存储到缓冲区数组 b 中。 |                                                              |
| 3                                                            | **public final Boolean readBooolean()throws IOException**    |
| 从所包含的输入流中读取一个布尔型数据。                       |                                                              |
| 4                                                            | **public final byte readByte()throws IOException**           |
| 从所包含的输入流中读取一个字节数据。                         |                                                              |
| 5                                                            | **public final short readShort()throws IOException**         |
| 从所包含的输入流中读取一个短整型数据。                       |                                                              |
| 6                                                            | **public final Int readInt()throws IOException**             |
| 从所包含的输入流中读取一个整型数据。                         |                                                              |
| 7                                                            | **public String readLine() throws IOException**              |
| 从输入流中读取下一文本行。                                   |                                                              |



## 3\. DataInputStream 范例

下面的例子演示了DataInputStream和DataOutputStream的使用，该例从文本文件test.txt中读取5行，并转换成大写字母，最后保存在另一个文件test1.txt中。

test.txt 文件内容如下：


​    

```java
codebaoku1
codebaoku2
codebaoku3
codebaoku4
codebaoku5
```


​    
​    

```java
import java.io.*;

public class Test{
    public static void main(String args[])throws IOException{
    
        DataInputStream in = new DataInputStream(new FileInputStream("test.txt"));
        DataOutputStream out = new DataOutputStream(new  FileOutputStream("test1.txt"));
        BufferedReader d  = new BufferedReader(new InputStreamReader(in));
        
        String count;
        while((count = d.readLine()) != null){
            String u = count.toUpperCase();
            System.out.println(u);
            out.writeBytes(u + "  ,");
        }
        d.close();
        out.close();
    }
}
```


以上实例编译运行结果如下：


​    

```java
CODEBAOKU1
CODEBAOKU2
CODEBAOKU3
CODEBAOKU4
CODEBAOKU5
```




# Java DataOutputStream类

数据输出流允许应用程序以与机器无关方式将Java基本数据类型写到底层输出流。



## 1\. DataOutputStream 创建方式

下面的构造方法用来创建数据输出流对象。


​    

```java
DataOutputStream out = new DataOutputStream(OutputStream  out);
```




## 2\. DataOutputStream 操作方法

创建对象成功后，可以参照以下列表给出的方法，对流进行写操作或者其他操作。

| 序号                                                         | 方法描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                                                            | **public final void write(byte[] w, int off, int len)throws IOException** |
| 将指定字节数组中从偏移量 off 开始的 len 个字节写入此字节数组输出流。 |                                                              |
| 2                                                            | **Public final int write(byte [] b)throws IOException**      |
| 将指定的字节写入此字节数组输出流。                           |                                                              |
| 3                                                            | **public final void writeBooolean()throws IOException**      |
| 写入一个布尔型数据到输出流。                                 |                                                              |
| 4                                                            | **public final void writeByte()throws IOException**          |
| 写入一个字节数据到输出流。                                   |                                                              |
| 5                                                            | **public final void writeShort()throws IOException**         |
| 写入一个短整型数据到输出流。                                 |                                                              |
| 6                                                            | **public final void writeInt()throws IOException**           |
| 写入一个整型数据到输出流。                                   |                                                              |
| 7                                                            | **Public void flush()throws IOException**                    |
| 刷新此输出流并强制写出所有缓冲的输出字节。                   |                                                              |
| 8                                                            | **public final void writeBytes(String s) throws IOException** |
| 将字符串以字节序列写入到底层的输出流，字符串中每个字符都按顺序写入，并丢弃其高八位。 |                                                              |



## 3\. DataOutputStream 操作范例

下面的例子演示了 DataInputStream 和 DataOutputStream的使用，该例从文本文件 test.txt
中读取5行，并转换成大写字母，最后保存在另一个文件 test1.txt中。

test.txt 文件内容如下：


​    

```java
codebaoku1
codebaoku2
codebaoku3
codebaoku4
codebaoku5
```


​    
​    

```java
import java.io.*;

public class Test{
    public static void main(String args[])throws IOException{
    
        DataInputStream in = new DataInputStream(new FileInputStream("test.txt"));
        DataOutputStream out = new DataOutputStream(new  FileOutputStream("test1.txt"));
        BufferedReader d  = new BufferedReader(new InputStreamReader(in));
        
        String count;
        while((count = d.readLine()) != null){
            String u = count.toUpperCase();
            System.out.println(u);
            out.writeBytes(u + "  ,");
        }
        d.close();
        out.close();
    }
}
```


以上实例编译运行结果如下：


​    

```java
CODEBAOKU1
CODEBAOKU2
CODEBAOKU3
CODEBAOKU4
CODEBAOKU5
```





# Java HashMap HashMap 是一个散列表，它存储的内容是键值对(key-value)映射。

HashMap 实现了 Map 接口，根据键的 HashCode 值存储数据，具有很快的访问速度，最多允许一条记录的键为 null，不支持线程同步。

HashMap 是无序的，即不会记录插入的顺序。

HashMap 继承于AbstractMap，实现了 Map、Cloneable、java.io.Serializable 接口。

![](https://www.itbenkyou.com/wp-content/uploads/2020/07/WV9wXLl.png)

HashMap 的 key 与 value 类型可以相同也可以不同，可以是字符串（String）类型的 key 和
value，也可以是整型（Integer）的 key 和字符串（String）类型的 value。

![](https://static.itbenkyou.com/images/mix/java-map.svg)

HashMap 中的元素实际上是对象，一些常见的基本类型可以使用它的包装类。

基本类型对应的包装类表如下：

| 基本类型 | 引用类型  |
| -------- | --------- |
| boolean  | Boolean   |
| byte     | Byte      |
| short    | Short     |
| int      | Integer   |
| long     | Long      |
| float    | Float     |
| double   | Double    |
| char     | Character |

HashMap 类位于 java.util 包中，使用前需要引入它，语法格式如下：

```java import java.util.HashMap; // 引入 HashMap 类 ```

以下实例我们创建一个 HashMap 对象 Sites， 整型（Integer）的 key 和字符串（String）类型的 value：

```java HashMap Sites = new HashMap(); ```

###  添加元素

HashMap 类提供了很多有用的方法，添加键值对(key-value)可以使用 put() 方法:




# Java HashSet

HashSet 基于 HashMap 来实现的，是一个不允许有重复元素的集合，它的元素无序的，允许有 null 值。

HashSet 不是线程安全的，如果多个线程尝试同时修改 HashSet，则最终结果是不确定的。 您必须在多线程访问时显式同步对 HashSet
的并发访问。

HashSet 实现了 Set 接口。

HashSet 中的元素实际上是对象，一些常见的基本类型可以使用它的包装类。

基本类型对应的包装类表如下：

| 基本类型 | 引用类型  |
| -------- | --------- |
| boolean  | Boolean   |
| byte     | Byte      |
| short    | Short     |
| int      | Integer   |
| long     | Long      |
| float    | Float     |
| double   | Double    |
| char     | Character |

HashSet 类位于 java.util 包中，使用前需要引入它，语法格式如下：


​    

```java
import java.util.HashSet; // 引入 HashSet 类
```

以下范例我们创建一个 HashSet 对象 sites，用于保存字符串元素：


​    

```java
HashSet<String> sites = new HashSet<String>();
```



## 1\. 添加元素

HashSet 类提供类很多有用的方法，添加元素可以使用 add() 方法:


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");  // 重复的元素不会被添加
        System.out.println(sites);
    }
}
```


执行以上代码，输出结果如下：


​    

```java
[Google, Codebaoku, Zhihu, Taobao]
```

在上面的范例中，Codebaoku 被添加了两次，它在集合中也只会出现一次，因为集合中的每个元素都必须是唯一的。



## 2\. 判断元素是否存在

我们可以使用 contains() 方法来判断元素是否存在于集合当中:


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");  // 重复的元素不会被添加
        System.out.println(sites.contains("Taobao"));
    }
}
```


执行以上代码，输出结果如下：


​    

```java
true
```



## 3\. 删除元素

我们可以使用 remove() 方法来删除集合中的元素:


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");     // 重复的元素不会被添加
        sites.remove("Taobao");  // 删除元素，删除成功返回 true，否则为 false
        System.out.println(sites);
    }
}
```


执行以上代码，输出结果如下：


​    

```java
[Google, Codebaoku, Zhihu]
```

删除集合中所有元素可以使用 clear 方法：


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");     // 重复的元素不会被添加
        sites.clear();  
        System.out.println(sites);
    }
}    
```


执行以上代码，输出结果如下：


​    

```java
[]
```



## 4\. 计算大小

如果要计算 HashSet 中的元素数量可以使用 size() 方法：


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");     // 重复的元素不会被添加
        System.out.println(sites.size());  
    }
}
```


执行以上代码，输出结果如下：


​    

```java
4
```



## 5\. 迭代 HashSet

可以使用 for-each 来迭代 HashSet 中的元素。


​    

```java
// 引入 HashSet 类      
import java.util.HashSet;

public class CodebaokuTest {
    public static void main(String[] args) {
    HashSet<String> sites = new HashSet<String>();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Zhihu");
        sites.add("Codebaoku");     // 重复的元素不会被添加
        for (String i : sites) {
            System.out.println(i);
        }
    }
}   
```


执行以上代码，输出结果如下：


​    

```java
Google
Codebaoku
Zhihu
Taobao
```





# Java IO 流(Stream)

Java.io 包几乎包含了所有与输入、输出操作相关的类。所有这些流类 Stream 代表了输入源和输出目标。

Java.io 包中的流支持很多种格式，比如：基本类型、对象等。一个流可以理解为一个数据的序列。输入流表示从一个源读取数据，输出流表示向一个目标写数据。

Java 为 I/O 提供了强大的而灵活的支持，使其更广泛地应用到文件传输和网络编程中。



## 1\. Java IO 输入输出流的类层次图



## 2\. 读取控制台输入

Java 的控制台输入由 System.in 完成。

为了获得一个绑定到控制台的字符流，你可以把 System.in 包装在一个 BufferedReader 对象中来创建一个字符流。

### 1）创建 BufferedReader

创建 BufferedReader 的语法：


​    

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```


BufferedReader 对象创建后，我们便可以使用 read() 方法从控制台读取一个字符，或者用 readLine() 方法读取一个字符串。

### 2）从控制台读取多字符输入

从 BufferedReader 对象读取一个字符要使用 read() 方法，它的语法如下：


​    

```java
int read( ) throws IOException
```


每次调用 read() 方法，它从输入流读取一个字符并把该字符作为整数值返回。 当流结束的时候返回 -1。该方法抛出 IOException。

下面的程序示范了用 read() 方法从控制台不断读取字符直到用户输入 q。


​    

```java
//使用 BufferedReader 在控制台读取字符

import java.io.*;
    
public class BRRead {
    public static void main(String[] args) throws IOException {
        char c;
        // 使用 System.in 创建 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("输入字符, 按下 'q' 键退出。");
        // 读取字符
        do {
            c = (char) br.read();
            System.out.println(c);
        } while (c != 'q');
    }
}
```


以上范例编译运行结果如下:


​    

```java
输入字符, 按下 'q' 键退出。
test
t
e
s
t

q
q
```


### 3）从控制台读取字符串

从标准输入读取一个字符串需要使用 BufferedReader 的 readLine() 方法。

它的一般格式是：


​    

```java
String readLine( ) throws IOException    
```


下面的程序读取和显示字符行直到你输入了单词"end"。


​    

```java
//使用 BufferedReader 在控制台读取字符
import java.io.*;
    
public class BRReadLines {
    public static void main(String[] args) throws IOException {
        // 使用 System.in 创建 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        System.out.println("Enter lines of text.");
        System.out.println("Enter 'end' to quit.");
        do {
            str = br.readLine();
            System.out.println(str);
        } while (!str.equals("end"));
    }
}
```


以上范例编译运行结果如下:


​    

```java
Enter lines of text.
Enter 'end' to quit.
This is line one
This is line one
This is line two
This is line two
end
end
```


> JDK 5 后的版本我们也可以使用 Java Scanner 类来获取控制台的输入。



## 3\. 从控制台输出

控制台的输出由 print( ) 和 println() 完成。这些方法都由类 PrintStream 定义，System.out 是该类对象的一个引用。

PrintStream 继承了 OutputStream类，并且实现了方法 write()。这样，write() 也可以用来往控制台写操作。

PrintStream 定义 write() 的最简单格式如下所示：


​    

```java
void write(int byteval)
```


该方法将 byteval 的低八位字节写到流中。

### 1) 输出单个字符

下面的例子用 write() 把字符 "A" 和紧跟着的换行符输出到屏幕：


​    

```java
import java.io.*;
 
//演示 System.out.write().
public class WriteDemo {
    public static void main(String[] args) {
        int b;
        b = 'A';
        System.out.write(b);
        System.out.write('\n');
    }
}
```


运行以上范例在输出窗口输出 "A" 字符


​    

```java
A
```


**注意：** write() 方法不经常使用，因为 print() 和 println() 方法用起来更为方便。

### 2) 输出字符串

在 java 中，System.out.println() 是我们经常会用到的一个语句，它的作用是将内容输出在控制台，常用于打印调试信息。除了
System.out.println() 之外，还有其他的打印结果的方法。

System.out.print()，这个方法与 System.out.println() 很像，区别就在于，System.out.println()
会在标准的输出中显示文字后换行，System.out.print() 输出文字后不会换行。

例如：输出两行字符串。


​    

```java
System.out.println("HelloWord One-------");
System.out.println("HelloWord Two-------");
```




# Java Iterator（迭代器）



Java Iterator（迭代器）不是一个集合，它是一种用于访问集合的方法，可用于迭代 ArrayList 和 HashSet 等集合。

Iterator 是 Java 迭代器最简单的实现，ListIterator 是 Collection API 中的接口， 它扩展了 Iterator
接口。

迭代器 it 的两个基本操作是 next 、hasNext 和 remove。

调用 it.next() 会返回迭代器的下一个元素，并且更新迭代器的状态。

调用 it.hasNext() 用于检测集合中是否还有元素。

调用 it.remove() 将迭代器返回的元素删除。

Iterator 类位于 java.util 包中，使用前需要引入它，语法格式如下：


​    

```java
import java.util.Iterator; // 引入 Iterator 类
```



## 1\. 获取一个迭代器

集合想获取一个迭代器可以使用 iterator() 方法:


​    

```java
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
```


执行以上代码，输出结果如下：


​    

```java
Google
```



## 2\. 循环集合元素

让迭代器 it 逐个返回集合中所有元素最简单的方法是使用 while 循环：


​    

```java
while(it.hasNext()) {
    System.out.println(it.next());
}
```


以下输出集合 sites 中的所有元素：


​    

```java
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
```


执行以上代码，输出结果如下：


​    

```java
Google
Codebaoku
Taobao
Zhihu
```




## 3\. 删除元素

要删除集合中的元素可以使用 remove() 方法。

以下范例我们删除集合中小于 10 的元素：


​    

```java
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
```


执行以上代码，输出结果如下：


​    

```java
[12, 23]
```





# Java JDK、JRE和JVM的区别和联系



## 1\. JDK（java development kit）

JDK 是 Java 的开发工具包，是整个 Java 的核心。

JDK 提供了Java 的开发环境（javac等）和 运行环境（JVM和核心类库）。

JDK的安装目录下有六个文件夹，其中，真正在运行java程序时起作用的是四个文件夹：

  * bin： javac 编译器
  * include：Java 和 jvm交互用的头文件
  * lib： 类库
  * jre： 运行环境



## 2\. JRE（Java runtime environment）

JRE 即 java 运行环境，包括 java 虚拟机（JVM）、Java 平台核心类和支持文件，但是不包括开发工具（编译器、调试器等）。

JRE 面向 Java 程序的使用者。如果只安装 JRE，则系统只能运行 Java 程序。



## 3\. JVM（Java virtual machine）

JVM 即 Java 虚拟机，它是 Java 跨平台的核心。

JVM 的作用是解释由 JDK 生成的指令集（即字节码）给系统，从而运行 Java 应用程序。



## 4\. Java 程序编译原理

源程序由 JDK 的 javac 生成类文件 .class 文件，JVM 将 .class 文件解释给系统。

Java 程序的字节码文件可以放到任意装有 JRE 的计算机运行，再由不同 JRE 的将它们转化成相应的机器代码，这就实现了 Java 程序的可移植性。

传统的编译方法，先转化到字节码（ bytecode ）
这种特殊的中间形式，字节码再转换成机器码或系统调用。生成的机器代码就不可避免地跟特殊的操作系统和特殊的机器结构相关。



## 5\. 三者的联系与区别

JDK 包含 JRE，JRE 包含 JVM。




# Java LinkedList

链表（Linked list）是一种常见的基础数据结构，是一种线性表，但并不是按照线性的顺序存储数据，而是在每一个节点里存到下一个节点的地址。

链表可分为单向链表和双向链表。

一个单向链表包含两个值: 当前节点的值和一个指向下一个节点的链接。

一个双向链表有三个整数值: 数值、向后的节点链接、向前的节点链接。

Java LinkedList（链表） 类似于 ArrayList，是一种常用的数据容器。

与 ArrayList 相比，LinkedList 的增加和删除对操作效率更高，而查找和修改的操作效率较低。

**以下情况使用 ArrayList :**

  * 频繁访问列表中的某一个元素。
  * 只需要在列表末尾进行添加和删除元素操作。

**以下情况使用 LinkedList :**

  * 你需要通过循环迭代来访问列表中的某些元素。
  * 需要频繁的在列表开头、中间、末尾等位置进行添加和删除元素操作。

LinkedList 继承了 AbstractSequentialList 类。

LinkedList 实现了 Queue 接口，可作为队列使用。

LinkedList 实现了 List 接口，可进行列表的相关操作。

LinkedList 实现了 Deque 接口，可作为队列使用。

LinkedList 实现了 Cloneable 接口，可实现克隆。

LinkedList 实现了 java.io.Serializable 接口，即可支持序列化，能通过序列化去传输。

![](http://static.codebaoku.com/pics/c4/0b/c40b77775545f3a2c45b376382c20776.png)



## 1\. 创建链表

LinkedList 类位于 java.util 包中，使用前需要引入它，语法格式如下：


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList; 

LinkedList<E> list = new LinkedList<E>();   // 普通创建方法
或者
LinkedList<E> list = new LinkedList(Collection<? extends E> c); // 使用集合创建链表
```

创建 LinkedList 的范例：


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    

```java
[Google, Codebaoku, Taobao, Weibo]
```

更多的情况下我们使用 ArrayList 访问列表中的随机元素更加高效，但以下几种情况 LinkedList 提供了更高效的方法。



## 2\. 在列表开头添加元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        // 使用 addFirst() 在头部添加元素
        sites.addFirst("Wiki");
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    

```java
[Wiki, Google, Codebaoku, Taobao]
```



## 2\. 在列表结尾添加元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        // 使用 addLast() 在尾部添加元素
        sites.addLast("Wiki");
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    

```java
[Google, Codebaoku, Taobao, Wiki]
```



## 3\. 在列表开头移除元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        // 使用 removeFirst() 移除头部元素
        sites.removeFirst();
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    

```java
[Codebaoku, Taobao, Weibo]
```



## 4\. 在列表结尾移除元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        // 使用 removeLast() 移除尾部元素
        sites.removeLast()<;
        System.out.println(sites);
    }
}
```


以上范例，执行输出结果为：


​    

```java
[Google, Codebaoku, Taobao]
```



## 5\. 获取列表开头的元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        // 使用 getFirst() 获取头部元素
        System.out.println(sites.getFirst());
    }
} 
```


以上范例，执行输出结果为：


​    

```java
Google
```



## 6\. 获取列表结尾的元素


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        // 使用 getLast() 获取尾部元素
        System.out.println(sites.getLast());
    }
}   
```


以上范例，执行输出结果为：


​    

```java
Weibo
```



## 7\. 迭代元素

我们可以使用 for 配合 size() 方法来迭代列表中的元素：


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        for (int size = sites.size(), i = 0; i < size; i++) {
            System.out.println(sites.get(i));
        }
    }
}
```


size() 方法用于计算链表的大小。

以上范例，执行输出结果为：


​    

```java
Google
Codebaoku
Taobao
Weibo
```

也可以使用 for-each 来迭代元素：


​    

```java
// 引入 LinkedList 类
import java.util.LinkedList;

public class CodebaokuTest {
    public static void main(String[] args) {
        LinkedList sites = new LinkedList();
        sites.add("Google");
        sites.add("Codebaoku");
        sites.add("Taobao");
        sites.add("Weibo");
        for (String i : sites) {
            System.out.println(i);
        }
    }
}
```


以上范例，执行输出结果为：


​    

```java
Google
Codebaoku
Taobao
Weibo
```



## 8\. 常用方法

| 方法                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| public boolean add(E e)                                      | 链表末尾添加元素，返回是否成功，成功为 true，失败为 false。  |
| public void add(int index, E element)                        | 向指定位置插入元素。                                         |
| public boolean addAll(Collection extends E> c)               | 将一个集合的所有元素添加到链表后面，返回是否成功，成功为     |
| true，失败为 false。                                         |                                                              |
| public boolean addAll(int index, Collection extends E> c)    |                                                              |
| 将一个集合的所有元素添加到链表的指定位置后面，返回是否成功，成功为 true，失败为 false。 |                                                              |
| public void addFirst(E e)                                    | 元素添加到头部。                                             |
| public void addLast(E e)                                     | 元素添加到尾部。                                             |
| public boolean offer(E e)                                    | 向链表末尾添加元素，返回是否成功，成功为 true，失败为 false。 |
| public boolean offerFirst(E e)                               | 头部插入元素，返回是否成功，成功为 true，失败为 false。      |
| public boolean offerLast(E e)                                | 尾部插入元素，返回是否成功，成功为 true，失败为 false。      |
| public void clear()                                          | 清空链表。                                                   |
| public E removeFirst()                                       | 删除并返回第一个元素。                                       |
| public E removeLast()                                        | 删除并返回最后一个元素。                                     |
| public boolean remove(Object o)                              | 删除某一元素，返回是否成功，成功为 true，失败为 false。      |
| public E remove(int index)                                   | 删除指定位置的元素。                                         |
| public E poll()                                              | 删除并返回第一个元素。                                       |
| public E remove()                                            | 删除并返回第一个元素。                                       |
| public boolean contains(Object o)                            | 判断是否含有某一元素。                                       |
| public E get(int index)                                      | 返回指定位置的元素。                                         |
| public E getFirst()                                          | 返回第一个元素。                                             |
| public E getLast()                                           | 返回最后一个元素。                                           |
| public int indexOf(Object o)                                 | 查找指定元素从前往后第一次出现的索引。                       |
| public int lastIndexOf(Object o)                             | 查找指定元素最后一次出现的索引。                             |
| public E peek()                                              | 返回第一个元素。                                             |
| public E element()                                           | 返回第一个元素。                                             |
| public E peekFirst()                                         | 返回头部元素。                                               |
| public E peekLast()                                          | 返回尾部元素。                                               |
| public E set(int index, E element)                           | 设置指定位置的元素。                                         |
| public Object clone()                                        | 克隆该列表。                                                 |
| public Iterator descendingIterator()                         | 返回倒序迭代器。                                             |
| public int size()                                            | 返回链表元素个数。                                           |
| public ListIterator listIterator(int index)                  | 返回从指定位置开始到末尾的迭代器。                           |
| public Object[] toArray()                                    | 返回一个由链表元素组成的数组。                               |
| public  T[] toArray(T[] a)                                   | 返回一个由链表元素转换类型而成的数组。                       |



# Java MySQL 连接

Java 通过使用 JDBC 来连接 MySQL 数据库。Java 连接 MySQL 需要专用的驱动包，官方下载地址为：
**[http://dev.mysql.com/downloads/connector/j/]()** ，解压后得到 jar
库文件，然后在项目中导入该库文件。

本范例使用的是 Eclipse，导入 jar 包：

> **MySQL 8.0 以上版本的数据库连接有所不同：**
>
>   * 1、MySQL 8.0 以上版本驱动包版本 mysql-connector-java-8.0.16.jar。
>
>   * 2、 **com.mysql.jdbc.Driver** 更换为 com.mysql.cj.jdbc.Driver。
>
>   * MySQL 8.0 以上版本不需要建立 SSL 连接的，需要显式关闭。
>
>   * allowPublicKeyRetrieval=true 允许客户端从服务器获取公钥。
>
>   * 最后还需要设置 CST。
>
> 

>加载驱动与连接数据库方式如下：
>
>
>Class.forName("com.mysql.cj.jdbc.Driver");
>conn =
>DriverManager.getConnection("jdbc:mysql://localhost:3306/test_demo?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC","root","password");



## 1\. 创建测试数据

接下来我们在 MySQL 中创建 CodeBaoku 数据库，并创建 websites 数据表，表结构如下：


​    

```sql
CREATE TABLE `websites` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` char(20) NOT NULL DEFAULT '' COMMENT '站点名称',
    `url` varchar(255) NOT NULL DEFAULT '',
    `alexa` int(11) NOT NULL DEFAULT '0' COMMENT 'Alexa 排名',
    `country` char(10) NOT NULL DEFAULT '' COMMENT '国家',
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
```


插入一些数据：


​    

```sql
INSERT INTO `websites` VALUES ('1', 'Google', 'https://www.google.cm/', '1', 'USA');
INSERT INTO `websites` VALUES ('2', '淘宝', 'https://www.taobao.com/', '13', 'CN'),;
INSERT INTO `websites` VALUES ('3', '[编程宝库](http://www.d.com)', 'http://d.com/', '888', '');
INSERT INTO `websites` VALUES ('4', '微博', 'http://weibo.com/', '20', 'CN');
INSERT INTO `websites` VALUES ('5', 'Facebook', 'https://www.facebook.com/', '3', 'USA');
```


数据表显示如下：



## 2\. 连接数据库

以下范例使用了 JDBC 连接 MySQL 数据库，注意一些数据如用户名，密码需要根据你的开发环境来配置：


​    

```java
package com.itbenkyou.test;

import java.sql.*;
    
public class MySQLDemo {
    
    // MySQL 8.0 以下版本 - JDBC 驱动名及数据库 URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost:3306/Codebaoku";
    
    // MySQL 8.0 以上版本 - JDBC 驱动名及数据库 URL
    //static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";  
    //static final String DB_URL = "jdbc:mysql://localhost:3306/Codebaoku?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC";
```


​        

```java
    // 数据库的用户名与密码，需要根据自己的设置
    static final String USER = "root";
    static final String PASS = "123456";
    
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            // 注册 JDBC 驱动
            Class.forName(JDBC_DRIVER);
        
            // 打开链接
            System.out.println("连接数据库...");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);
        
            // 执行查询
            System.out.println(" 范例化Statement对象...");
            stmt = conn.createStatement();
            String sql;
            sql = "SELECT id, name, url FROM websites";
            ResultSet rs = stmt.executeQuery(sql);
        
            // 展开结果集数据库
            while(rs.next()){
                // 通过字段检索
                int id  = rs.getInt("id");
                String name = rs.getString("name");
                String url = rs.getString("url");
    
                // 输出数据
                System.out.print("ID: " + id);
                System.out.print(", 站点名称: " + name);
                System.out.print(", 站点 URL: " + url);
                System.out.print("\n");
            }
            // 完成后关闭
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            // 处理 JDBC 错误
            se.printStackTrace();
        }catch(Exception e){
            // 处理 Class.forName 错误
            e.printStackTrace();
        }finally{
            // 关闭资源
            try{
                if(stmt!=null) stmt.close();
            }catch(SQLException se2){
            }// 什么都不做
            try{
                if(conn!=null) conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }
        }
        System.out.println("Goodbye!");
    }
}
```





# Java Number & Math 类

一般地，当需要使用数字的时候，我们通常使用内置数据类型，如： **byte、int、long、double** 等。

## 实例

```java int a = 5000; float b = 13.65f; byte c = 0x4a; ```

然而，在实际开发过程中，我们经常会遇到需要使用对象，而不是内置数据类型的情形。为了解决这个问题，Java 语言为每一个内置数据类型提供了对应的包装类。

所有的包装类 **（Integer、Long、Byte、Double、Float、Short）** 都是抽象类 Number 的子类。

| 包装类    | 基本数据类型 |
| --------- | ------------ |
| Boolean   | boolean      |
| Byte      | byte         |
| Short     | short        |
| Integer   | int          |
| Long      | long         |
| Character | char         |
| Float     | float        |
| Double    | double       |

![Java Number类](https://www.itbenkyou.com/wp-
content/uploads/2013/12/OOP_WrapperClass.png)

这种由编译器特别支持的包装称为装箱，所以当内置数据类型被当作对象使用的时候，编译器会把内置类型装箱为包装类。相似的，编译器也可以把一个对象拆箱为内置类型。Number
类属于 java.lang 包。



# Java Number

我们通常使用内置数据类型： **byte、int、long、double** 来使用数字。

有时候，我们需要使用对象，而不是内置数据类型。为了解决这个问题，Java 语言为每一个内置数据类型提供了对应的包装类。

所有的包装类 **（Integer、Long、Byte、Double、Float、Short）** 都是抽象类 Number 的子类。

| 包装类    | 基本数据类型 |
| --------- | ------------ |
| Boolean   | boolean      |
| Byte      | byte         |
| Short     | short        |
| Integer   | int          |
| Long      | long         |
| Character | char         |
| Float     | float        |
| Double    | double       |

这种由编译器特别支持的包装称为装箱，所以当内置数据类型被当作对象使用的时候，编译器会把内置类型装箱为包装类。相似的，编译器也可以把一个对象拆箱为内置类型。Number
类属于 java.lang 包。



## 1\. 使用数字对象的范例

下面是一个使用 Integer 对象的范例：


​    

```java
public class Test{
 
   public static void main(String[] args){
      Integer x = 5;
      x =  x + 10;
      System.out.println(x); 
   }
}
```


以上范例编译运行结果如下：


​    

```java
15
```


当 x 被赋为整型值时，由于x是一个对象，所以编译器要对x进行装箱。然后，为了使x能进行加运算，所以要对x进行拆箱。



## 2\. Java Math 类

Java 的 Math 包含了用于执行基本数学运算的属性和方法，如初等指数、对数、平方根和三角函数。

Math 的方法都被定义为 static 形式，通过 Math 类可以在主函数中直接调用。


​    

```java
public class Test {  
    public static void main (String []args)  
    {  
        System.out.println("90 度的正弦值：" + Math.sin(Math.PI/2));  
        System.out.println("0度的余弦值：" + Math.cos(0));  
        System.out.println("60度的正切值：" + Math.tan(Math.PI/3));  
        System.out.println("1的反正切值： " + Math.atan(1));  
        System.out.println("π/2的角度值：" + Math.toDegrees(Math.PI/2));  
        System.out.println(Math.PI);  
    }  
}
```


以上范例编译运行结果如下：


​    

```java
90 度的正弦值：1.0
0度的余弦值：1.0
60度的正切值：1.7320508075688767
1的反正切值： 0.7853981633974483
π/2的角度值：90.0
3.141592653589793
```




## 3\. Java Math 类方法

下面的表中列出的是 Number & Math 类常用的一些方法：

| 序号                                                         | 方法与描述  |
| ------------------------------------------------------------ | ----------- |
| 1                                                            | xxxValue()  |
| 将 Number 对象转换为xxx数据类型的值并返回。                  |             |
| 2                                                            | compareTo() |
| 将number对象与参数比较。                                     |             |
| 3                                                            | equals()    |
| 判断number对象是否与参数相等。                               |             |
| 4                                                            | valueOf()   |
| 返回一个 Number 对象指定的内置数据类型                       |             |
| 5                                                            | toString()  |
| 以字符串形式返回值。                                         |             |
| 6                                                            | parseInt()  |
| 将字符串解析为int类型。                                      |             |
| 7                                                            | abs()       |
| 返回参数的绝对值。                                           |             |
| 8                                                            | ceil()      |
| 返回大于等于( >= )给定参数的的最小整数，类型为双精度浮点型。 |             |
| 9                                                            | floor()     |
| 返回小于等于（<=）给定参数的最大整数 。                      |             |
| 10                                                           | rint()      |
| 返回与参数最接近的整数。返回类型为double。                   |             |
| 11                                                           | round()     |
| 它表示 **四舍五入** ，算法为 Math.floor(x+0.5)，即将原来的数字加上 0.5 后再向下取整，所以，Math.round(11.5) |             |
| 的结果为12，Math.round(-11.5) 的结果为-11。                  |             |
| 12                                                           | min()       |
| 返回两个参数中的最小值。                                     |             |
| 13                                                           | max()       |
| 返回两个参数中的最大值。                                     |             |
| 14                                                           | exp()       |
| 返回自然数底数e的参数次方。                                  |             |
| 15                                                           | log()       |
| 返回参数的自然数底数的对数值。                               |             |
| 16                                                           | pow()       |
| 返回第一个参数的第二个参数次方。                             |             |
| 17                                                           | sqrt()      |
| 求参数的算术平方根。                                         |             |
| 18                                                           | sin()       |
| 求指定double类型参数的正弦值。                               |             |
| 19                                                           | cos()       |
| 求指定double类型参数的余弦值。                               |             |
| 20                                                           | tan()       |
| 求指定double类型参数的正切值。                               |             |
| 21                                                           | asin()      |
| 求指定double类型参数的反正弦值。                             |             |
| 22                                                           | acos()      |
| 求指定double类型参数的反余弦值。                             |             |
| 23                                                           | atan()      |
| 求指定double类型参数的反正切值。                             |             |
| 24                                                           | atan2()     |
| 将笛卡尔坐标转换为极坐标，并返回极坐标的角度值。             |             |
| 25                                                           | toDegrees() |
| 将参数转化为角度。                                           |             |
| 26                                                           | toRadians() |
| 将角度转换为弧度。                                           |             |
| 27                                                           | random()    |
| 返回一个随机数。                                             |             |




# Java Object 类

Java Object 类是所有类的父类，也就是说 Java 的所有类都继承了 Object，子类可以使用 Object 的所有方法。

Object 类位于 java.lang 包中，编译时会自动导入，我们创建一个类时，如果没有明确继承一个父类，那么它就会自动继承 Object，成为
Object 的子类。

Object 类可以显示继承，也可以隐式继承，以下两种方式时一样的：

显式继承:


​    

```java
public class Runoob extends Object{
}
```


隐式继承:


​    

```java
public class Runoob {
}
```




## 1\. 类的构造函数

| 序号 | 构造方法 & 描述 |
| ---- | --------------- |
| 1    | **Object()**    |

构造一个新对象。  



## 2\. 类的方法

| 序号 | 方法 & 描述              |
| ---- | ------------------------ |
| 1    | protected Object clone() |

创建并返回一个对象的拷贝  

2 | boolean equals(Object obj)

比较两个对象是否相等  

3 | protected void finalize()

当 GC (垃圾回收器)确定不存在对该对象的有更多引用时，由对象的垃圾回收器调用此方法。  

4 | Class<?> getClass()

获取对象的运行时对象的类  

5 | int hashCode()

获取对象的 hash 值  

6 | void notify()

唤醒在该对象上等待的某个线程  

7 | void notifyAll()

唤醒在该对象上等待的所有线程  

8 | String toString()

返回对象的字符串表示形式  

9 | void wait()

让当前线程进入等待状态。直到其他线程调用此对象的 notify() 方法或 notifyAll() 方法。  

10 | void wait(long timeout)

让当前线程处于等待(阻塞)状态，直到其他线程调用此对象的 notify() 方法或 notifyAll() 方法，或者超过参数设置的timeout超时时间。  

11 | void wait(long timeout, int nanos)

与 wait(long timeout) 方法类似，多了一个 nanos 参数，这个参数表示额外时间（以纳秒为单位，范围是 0-999999）。
所以超时的时间还需要加上 nanos 纳秒。。



# Java POJO

POJO（Plain Ordinary Java Object）即简单的Java对象，实际就是普通 JavaBeans，是为了避免和EJB混淆所创造的简称。

使用 POJO 名称是为了避免和 EJB 混淆起来, 而且简称比较直接。POJO 是有一些属性和getter
setter方法的类，但没有业务逻辑，有时可以作为VO(value-object)或dto(Data Transform
Object)来使用。当然，如果你有一个简单的运算属性也是可以的，但不允许有业务方法，也不能携带有connection之类的方法。



## 1\. 自身特点

POJO是Plain OrdinaryJava Object的缩写，但是它通指没有使用Entity
Beans的普通java对象，可以把POJO作为支持业务逻辑的协助类。

POJO实质上可以理解为简单的实体类，顾名思义POJO类的作用是方便程序员使用数据库中的数据表，对于广大的程序员，可以很方便的将POJO类当做对象来进行使用，当然也是可以方便的调用其get,set方法。POJO类也给我们在struts框架中的配置带来了很大的方便。



## 2\. POJO范例

POJO 有一些 private 的参数作为对象的属性。然后针对每个参数定义了get和set方法作为访问的接口。例如：


​    

```java
public class User {
    private long id;
    private String name;
    public void setId(long id) {
        this. id = id;
    }
    public void setName(String name) {
        this. name=name;
    }
    public long getId() {
        return id;
    }
    public String getName() {
        return name;
    }
}
```


POJO对象有时也被称为Data对象，大量应用于表现现实中的对象。如果项目中使用了Hibernate框架，有一个关联的xml文件，使对象与数据库中的表对应，对象的属性与表中的字段相对应。



## 3\. POJO与javabean的区别

POJO 和JavaBean是我们常见的两个关键字，一般容易混淆，POJO全称是Plain Old Java Object / Pure Old Java
Object，中文可以翻译成：普通Java类，具有一部分getter/setter方法的那种类就可以称作POJO，但是JavaBean则比
POJO复杂很多， Java Bean 是可复用的组件，对 Java Bean 并没有严格的规范，理论上讲，任何一个 Java 类都可以是一个 Bean
。但通常情况下，由于 Java Bean 是被容器所创建（如 Tomcat) 的，所以 Java Bean 应具有一个无参的构造器。

另外，通常 Java Bean 还要实现 Serializable 接口用于实现 Bean 的持久性。 Java Bean
是不能被跨进程访问的。JavaBean是一种组件技术，就好像你做了一个扳子，而这个扳子会在很多地方被拿去用，这个扳子也提供多种功能(你可以拿这个扳子扳、锤、撬等等)，而这个扳子就是一个组件。一般在web应用程序中建立一个数据库的映射对象时，我们只能称它为POJO。POJO(Plain
Old Java
Object)这个名字用来强调它是一个普通java对象，而不是一个特殊的对象，其主要用来指代那些没有遵从特定的Java对象模型、约定或框架（如EJB）的Java对象。理想地讲，一个POJO是一个不受任何限制的Java对象（除了Java语言规范）。



### 3.1 错误的认识

POJO是这样的一种“纯粹的”JavaBean，在它里面除了JavaBean规范的方法和属性没有别的东西，即private属性以及对这个属性方法的public的get和set方法。我们会发现这样的JavaBean很“单纯”，它只能装载数据，作为数据存储的载体，而不具有业务逻辑处理的能力。



### 3.2 真正的意思

POJO是MartinFowler等发明的一个术语，用来表示普通的Java对象，不是JavaBean, EntityBean 或者
SessionBean。POJO不担当任何特殊的角色，也不实现任何特殊的Java框架的接口。

POJO是一个简单的普通的Java对象，它不包含业务逻辑或持久逻辑等，但不是JavaBean、EntityBean等，不具有任何特殊角色和不继承或不实现任何其它Java框架的类或接口。

下面是摘自Martin Fowler个人网站的一句话：

"We wondered why people were so against using regular objects in their systems
and concluded that it was because simple objects lacked a fancy name. So we
gave them one, and it's caught on very nicely." －－Martin Fowler

我们疑惑为什么人们不喜欢在他们的系统中使用普通的对象，我们得到的结论是－－普通的对象缺少一个响亮的名字，因此我们给它们起了一个，并且取得了很好的效果。




# Java String 类

字符串广泛应用 在 Java 编程中，在 Java 中字符串属于对象，Java 提供了 String 类来创建和操作字符串。



## 1\. 创建字符串

### 1）通过赋值创建字符串


​    

```java
String str = "0";
```


在代码中遇到字符串常量时，这里的值是 " **0** "，编译器会使用该值创建一个 String 对象。

和其它对象一样，可以使用关键字和构造方法来创建 String 对象。

### 2）通过构造函数创建字符串


​    

```java
String str2=new String("0");
```


**注意:** String 类是不可改变的，所以你一旦创建了 String 对象，那它的值就无法改变了。

如果需要对字符串做很多修改，那么应该选择使用 StringBuffer & StringBuilder 类。



## 2\. 字符串长度

用于获取有关对象的信息的方法称为访问器方法。

String 类的一个访问器方法是 length() 方法，它返回字符串对象包含的字符数。


​    

```java
public class StringDemo {
    public static void main(String args[]) {
        String site = "www.0.com";
        int len = site.length();
        System.out.println( "[编程宝库](http://www.0.com)教程网址长度: " + len );
   }
}
```


以上范例编译运行结果如下：


​    

```java
[编程宝库](http://www.0.com)教程网址长度: 17
```




## 3\. 连接字符串

String 类提供了连接两个字符串的方法：


​    

```java
string1.concat(string2);
```


返回 string2 连接 string1 的新字符串。

更常用的是使用'+'操作符来连接字符串，如：


​    

```java
"Hello," + " 0" + "!"
```

结果如下:


​    

```java
"Hello, 0!"
```



## 4\. 创建格式化字符串

我们知道输出格式化数字可以使用 printf() 和 format() 方法。

String 类使用静态方法 format() 返回一个String 对象而不是 PrintStream 对象。

String 类的静态方法 format() 能用来创建可复用的格式化字符串，而不仅仅是用于一次打印输出。

如下所示：


​    

```java
System.out.printf("浮点型变量的值为 " +
                  "%f, 整型变量的值为 " +
                  " %d, 字符串变量的值为 " +
                  "is %s", floatVar, intVar, stringVar);
```


你也可以这样写：


​    

```java
String fs;
fs = String.format("浮点型变量的值为 " +
                   "%f, 整型变量的值为 " +
                   " %d, 字符串变量的值为 " +
                   " %s", floatVar, intVar, stringVar);
```




## 5\. String 方法

下面是 String 类支持的方法，更多详细，参看 Java String API 文档:

| SN(序号)                                                     | 方法描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                                                            | char charAt(int index)                                       |
| 返回指定索引处的 char 值。                                   |                                                              |
| 2                                                            | int compareTo(Object o)                                      |
| 把这个字符串和另一个对象比较。                               |                                                              |
| 3                                                            | int compareTo(String anotherString)                          |
| 按字典顺序比较两个字符串。                                   |                                                              |
| 4                                                            | int compareToIgnoreCase(String str)                          |
| 按字典顺序比较两个字符串，不考虑大小写。                     |                                                              |
| 5                                                            | String concat(String str)                                    |
| 将指定字符串连接到此字符串的结尾。                           |                                                              |
| 6                                                            | boolean contentEquals(StringBuffer sb)                       |
| 当且仅当字符串与指定的StringBuffer有相同顺序的字符时候返回真。 |                                                              |
| 7                                                            | static String copyValueOf(char[] data)                       |
| 返回指定数组中表示该字符序列的 String。                      |                                                              |
| 8                                                            | static String copyValueOf(char[] data, int offset, int count) |
| 返回指定数组中表示该字符序列的 String。                      |                                                              |
| 9                                                            | boolean endsWith(String suffix)                              |
| 测试此字符串是否以指定的后缀结束。                           |                                                              |
| 10                                                           | boolean equals(Object anObject)                              |
| 将此字符串与指定的对象比较。                                 |                                                              |
| 11                                                           | boolean equalsIgnoreCase(String anotherString)               |
| 将此 String 与另一个 String 比较，不考虑大小写。             |                                                              |
| 12                                                           | byte[] getBytes()                                            |
| 使用平台的默认字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。 |                                                              |
| 13                                                           | byte[] getBytes(String charsetName)                          |
| 使用指定的字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。 |                                                              |
| 14                                                           | void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin) |
| 将字符从此字符串复制到目标字符数组。                         |                                                              |
| 15                                                           | int hashCode()                                               |
| 返回此字符串的哈希码。                                       |                                                              |
| 16                                                           | int indexOf(int ch)                                          |
| 返回指定字符在此字符串中第一次出现处的索引。                 |                                                              |
| 17                                                           | int indexOf(int ch, int fromIndex)                           |
| 返回在此字符串中第一次出现指定字符处的索引，从指定的索引开始搜索。 |                                                              |
| 18                                                           | int indexOf(String str)                                      |
| 返回指定子字符串在此字符串中第一次出现处的索引。             |                                                              |
| 19                                                           | int indexOf(String str, int fromIndex)                       |
| 返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引开始。 |                                                              |
| 20                                                           | String intern()                                              |
| 返回字符串对象的规范化表示形式。                             |                                                              |
| 21                                                           | int lastIndexOf(int ch)                                      |
| 返回指定字符在此字符串中最后一次出现处的索引。               |                                                              |
| 22                                                           | int lastIndexOf(int ch, int fromIndex)                       |
| 返回指定字符在此字符串中最后一次出现处的索引，从指定的索引处开始进行反向搜索。 |                                                              |
| 23                                                           | int lastIndexOf(String str)                                  |
| 返回指定子字符串在此字符串中最右边出现处的索引。             |                                                              |
| 24                                                           | int lastIndexOf(String str, int fromIndex)                   |
| 返回指定子字符串在此字符串中最后一次出现处的索引，从指定的索引开始反向搜索。 |                                                              |
| 25                                                           | int length()                                                 |
| 返回此字符串的长度。                                         |                                                              |
| 26                                                           | boolean matches(String regex)                                |
| 告知此字符串是否匹配给定的正则表达式。                       |                                                              |
| 27                                                           | boolean regionMatches(boolean ignoreCase, int toffset, String other, int |
| ooffset, int len)                                            |                                                              |
| 测试两个字符串区域是否相等。                                 |                                                              |
| 28                                                           | boolean regionMatches(int toffset, String other, int ooffset, int len) |
| 测试两个字符串区域是否相等。                                 |                                                              |
| 29                                                           | String replace(char oldChar, char newChar)                   |
| 返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。 |                                                              |
| 30                                                           | String replaceAll(String regex, String replacement)          |
| 使用给定的 replacement 替换此字符串所有匹配给定的正则表达式的子字符串。 |                                                              |
| 31                                                           | String replaceFirst(String regex, String replacement)        |
| 使用给定的 replacement 替换此字符串匹配给定的正则表达式的第一个子字符串。 |                                                              |
| 32                                                           | String[] split(String regex)                                 |
| 根据给定正则表达式的匹配拆分此字符串。                       |                                                              |
| 33                                                           | String[] split(String regex, int limit)                      |
| 根据匹配给定的正则表达式来拆分此字符串。                     |                                                              |
| 34                                                           | boolean startsWith(String prefix)                            |
| 测试此字符串是否以指定的前缀开始。                           |                                                              |
| 35                                                           | boolean startsWith(String prefix, int toffset)               |
| 测试此字符串从指定索引开始的子字符串是否以指定前缀开始。     |                                                              |
| 36                                                           | CharSequence subSequence(int beginIndex, int endIndex)       |
| 返回一个新的字符序列，它是此序列的一个子序列。               |                                                              |
| 37                                                           | String substring(int beginIndex)                             |
| 返回一个新的字符串，它是此字符串的一个子字符串。             |                                                              |
| 38                                                           | String substring(int beginIndex, int endIndex)               |
| 返回一个新字符串，它是此字符串的一个子字符串。               |                                                              |
| 39                                                           | char[] toCharArray()                                         |
| 将此字符串转换为一个新的字符数组。                           |                                                              |
| 40                                                           | String toLowerCase()                                         |
| 使用默认语言环境的规则将此 String 中的所有字符都转换为小写。 |                                                              |
| 41                                                           | String toLowerCase(Locale locale)                            |
| 使用给定 Locale 的规则将此 String 中的所有字符都转换为小写。 |                                                              |
| 42                                                           | String toString()                                            |
| 返回此对象本身（它已经是一个字符串！）。                     |                                                              |
| 43                                                           | String toUpperCase()                                         |
| 使用默认语言环境的规则将此 String 中的所有字符都转换为大写。 |                                                              |
| 44                                                           | String toUpperCase(Locale locale)                            |
| 使用给定 Locale 的规则将此 String 中的所有字符都转换为大写。 |                                                              |
| 45                                                           | String trim()                                                |
| 返回字符串的副本，忽略前导空白和尾部空白。                   |                                                              |
| 46                                                           | static String valueOf(primitive data type x)                 |
| 返回给定data type类型x参数的字符串表示形式。                 |                                                              |
| 47                                                           | contains(CharSequence chars)                                 |
| 判断是否包含指定的字符系列。                                 |                                                              |
| 48                                                           | isEmpty()                                                    |
| 判断字符串是否为空。                                         |                                                              |




# Java StringBuffer 和 StringBuilder 类

当对字符串进行修改的时候，需要使用 StringBuffer 和 StringBuilder 类。

和 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且不产生新的未使用对象。

在使用 StringBuffer 类时，每次都会对 StringBuffer 对象本身进行操作，而不是生成新的对象，所以如果需要对字符串进行修改推荐使用
StringBuffer。

StringBuilder 和 StringBuffer 之间的最大不同在于 StringBuilder 的方法不是线程安全的。

由于 StringBuilder 比 StringBuffer 有速度优势，所以多数情况下建议使用 StringBuilder 类。



## 1\. StringBuilder 类的范例


​    

```java
public class Test{
    public static void main(String args[]){
        StringBuilder sb = new StringBuilder(10);
        sb.append("0");
        System.out.println(sb);  
        sb.append("!");
        System.out.println(sb); 
        sb.insert(9, " Java");
        System.out.println(sb); 
        sb.delete(4,9);
        System.out.println(sb);  
    }
}
```


以上范例编译运行结果如下：


​    

```java
0
0!
0 Java!
code Java!
```




## 2\. StringBuffer 类的范例

在应用程序要求线程安全的情况下，必须使用 StringBuffer 类。


​    

```java
public class Test{
  public static void main(String args[]){
    StringBuffer sBuffer = new StringBuffer("[编程宝库](http://www.0.com)官网：");
    sBuffer.append("www");
    sBuffer.append(".0");
    sBuffer.append(".com");
    System.out.println(sBuffer);  
  }
}
```


以上范例编译运行结果如下：


​    

```java
[编程宝库](http://www.0.com)官网：www.0.com
```




## 3\. StringBuffer 方法

以下是 StringBuffer 类支持的主要方法：

| 序号                                                   | 方法描述                                |
| ------------------------------------------------------ | --------------------------------------- |
| 1                                                      | public StringBuffer append(String s)    |
| 将指定的字符串追加到此字符序列。                       |                                         |
| 2                                                      | public StringBuffer reverse()           |
| 将此字符序列用其反转形式取代。                         |                                         |
| 3                                                      | public delete(int start, int end)       |
| 移除此序列的子字符串中的字符。                         |                                         |
| 4                                                      | public insert(int offset, int i)        |
| 将 int 参数的字符串表示形式插入此序列中。              |                                         |
| 5                                                      | insert(int offset, String str)          |
| 将 str 参数的字符串插入此序列中。                      |                                         |
| 6                                                      | replace(int start, int end, String str) |
| 使用给定 String 中的字符替换此序列的子字符串中的字符。 |                                         |

下面的列表里的方法和 String 类的方法类似：

| 序号                                                         | 方法描述                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1                                                            | int capacity()                                               |
| 返回当前容量。                                               |                                                              |
| 2                                                            | char charAt(int index)                                       |
| 返回此序列中指定索引处的 char 值。                           |                                                              |
| 3                                                            | void ensureCapacity(int minimumCapacity)                     |
| 确保容量至少等于指定的最小值。                               |                                                              |
| 4                                                            | void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin) |
| 将字符从此序列复制到目标字符数组 dst。                       |                                                              |
| 5                                                            | int indexOf(String str)                                      |
| 返回第一次出现的指定子字符串在该字符串中的索引。             |                                                              |
| 6                                                            | int indexOf(String str, int fromIndex)                       |
| 从指定的索引处开始，返回第一次出现的指定子字符串在该字符串中的索引。 |                                                              |
| 7                                                            | int lastIndexOf(String str)                                  |
| 返回最右边出现的指定子字符串在此字符串中的索引。             |                                                              |
| 8                                                            | int lastIndexOf(String str, int fromIndex)                   |
| 返回 String 对象中子字符串最后出现的位置。                   |                                                              |
| 9                                                            | int length()                                                 |
| 返回长度（字符数）。                                         |                                                              |
| 10                                                           | void setCharAt(int index, char ch)                           |
| 将给定索引处的字符设置为 ch。                                |                                                              |
| 11                                                           | void setLength(int newLength)                                |
| 设置字符序列的长度。                                         |                                                              |
| 12                                                           | CharSequence subSequence(int start, int end)                 |
| 返回一个新的字符序列，该字符序列是此序列的子序列。           |                                                              |
| 13                                                           | String substring(int start)                                  |
| 返回一个新的 String，它包含此字符序列当前所包含的字符子序列。 |                                                              |
| 14                                                           | String substring(int start, int end)                         |
| 返回一个新的 String，它包含此序列当前所包含的字符子序列。    |                                                              |
| 15                                                           | String toString()                                            |
| 返回此序列中数据的字符串表示形式。                           |                                                              |





# Java switch 语句

switch 语句用于基于不同条件执行不同动作。通过判断一个变量与一系列值中某个值是否相等，然后执行对应的分支。



## 1\. Java switch 语句的语法


​    

```java
switch(expression){
    case value :
       //语句
       break; //可选
    case value :
       //语句
       break; //可选
    //你可以有任意数量的case语句
    default : //可选
       //语句
}
```


switch case 语句有如下规则：

  * switch 语句中的变量类型可以是： byte、short、int 或者 char。从 Java SE 7 开始，switch 支持字符串 String 类型了，同时 case 标签必须为字符串常量或字面量。

  * switch 语句可以拥有多个 case 语句。每个 case 后面跟一个要比较的值和冒号。

  * case 语句中的值的数据类型必须与变量的数据类型相同，而且只能是常量或者字面常量。

  * 当变量的值与 case 语句的值相等时，那么 case 语句之后的语句开始执行，直到 break 语句出现才会跳出 switch 语句。

  * 当遇到 break 语句时，switch 语句终止。程序跳转到 switch 语句后面的语句执行。case 语句不必须要包含 break 语句。如果没有 break 语句出现，程序会继续执行下一条 case 语句，直到出现 break 语句。

  * switch 语句可以包含一个 default 分支，该分支一般是 switch 语句的最后一个分支（可以在任何位置，但建议在最后一个）。default 在没有 case 语句的值和变量值相等的时候执行。default 分支不需要 break 语句。

**switch case 执行时，一定会先进行匹配，匹配成功返回当前 case 的值，再根据是否有 break，判断是否继续输出，或是跳出判断。**



## 2\. Java switch 语句的范例


​    

```java
public class Test {
   public static void main(String args[]){
      //char grade = args[0].charAt(0);
      char grade = 'C';
 
      switch(grade)
      {
         case 'A' :
            System.out.println("优秀"); 
            break;
         case 'B' :
         case 'C' :
            System.out.println("良好");
            break;
         case 'D' :
            System.out.println("及格");
            break;
         case 'F' :
            System.out.println("你需要再努力努力");
            break;
         default :
            System.out.println("未知等级");
      }
      System.out.println("你的等级是 " + grade);
   }
}
```


以上代码编译运行结果如下：


​    
```java
良好
你的等级是 C
```


如果 case 语句块中没有 break 语句时，JVM 并不会顺序输出每一个 case 对应的返回值，而是继续匹配，匹配不成功则返回默认 case。


​    
```java
public class Test {
   public static void main(String args[]){
      int i = 5;
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2:
            System.out.println("2");
         default:
            System.out.println("default");
      }
   }
}
```


以上代码编译运行结果如下：


​    
```java
default
```


如果 case 语句块中没有 break 语句时，匹配成功后，从当前 case 开始，后续所有 case 的值都会输出。


​    
```java
public class Test {
   public static void main(String args[]){
      int i = 1;
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2:
            System.out.println("2");
         default:
            System.out.println("default");
      }
   }
}
```


以上代码编译运行结果如下：


​    
```java
1
2
default
```

如果当前匹配成功的 case 语句块没有 break 语句，则从当前 case 开始，后续所有 case 的值都会输出，如果后续的 case 语句块有
break 语句则会跳出判断。


​    
```java
public class Test {
   public static void main(String args[]){
      int i = 1;
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2:
            System.out.println("2");
         case 3:
            System.out.println("3"); break;
         default:
            System.out.println("default");
      }
   }
}
```


以上代码编译运行结果如下：


​    
```java
1
2
3
```





# Java volatile

Java volatile在Java 5之前，是一个备受争议的关键字，因为在程序中使用它往往会导致出人意料的结果。在Java
5之后，volatile关键字才得以重获生机。

Java volatile
关键字是与Java的内存模型有关的，因此在讲述volatile关键之前，我们先来了解一下与内存模型相关的概念和知识，然后分析了volatile关键字的实现原理，最后给出了几个使用volatile关键字的场景。



## 一. 内存模型的相关概念

大家都知道，计算机在执行程序时，每条指令都是在CPU中执行的，而执行指令过程中，势必涉及到数据的读取和写入。由于程序运行过程中的临时数据是存放在主存（物理内存）当中的，这时就存在一个问题，由于CPU执行速度很快，而从内存读取数据和向内存写入数据的过程跟CPU执行指令的速度比起来要慢的多，因此如果任何时候对数据的操作都要通过和内存的交互来进行，会大大降低指令执行的速度。因此在CPU里面就有了高速缓存。

也就是，当程序在运行过程中，会将运算需要的数据从主存复制一份到CPU的高速缓存当中，那么CPU进行计算时就可以直接从它的高速缓存读取数据和向其中写入数据，当运算结束之后，再将高速缓存中的数据刷新到主存当中。举个简单的例子，比如下面的这段代码：


​    

```java
i = i + 1;
```


当线程执行这个语句时，会先从主存当中读取i的值，然后复制一份到高速缓存当中，然后CPU执行指令对i进行加1操作，然后将数据写入高速缓存，最后将高速缓存中i最新的值刷新到主存当中。

这个代码在单线程中运行是没有任何问题的，但是在多线程中运行就会有问题了。在多核CPU中，每条线程可能运行于不同的CPU中，因此每个线程运行时有自己的高速缓存（对单核CPU来说，其实也会出现这种问题，只不过是以线程调度的形式来分别执行的）。本文我们以多核CPU为例。

比如同时有2个线程执行这段代码，假如初始时i的值为0，那么我们希望两个线程执行完之后i的值变为2。但是事实会是这样吗？可能存在下面一种情况：初始时，两个线程分别读取i的值存入各自所在的CPU的高速缓存当中，然后线程1进行加1操作，然后把i的最新值1写入到内存。此时线程2的高速缓存当中i的值还是0，进行加1操作之后，i的值为1，然后线程2把i的值写入内存。

最终结果i的值是1，而不是2。这就是著名的缓存一致性问题。通常称这种被多个线程访问的变量为共享变量。也就是说，如果一个变量在多个CPU中都存在缓存（一般在多线程编程时才会出现），那么就可能存在缓存不一致的问题。

为了解决缓存不一致性问题，通常来说有以下2种解决方法：

  * 1）通过在总线加LOCK#锁的方式
  * 2）通过缓存一致性协议

这2种方式都是硬件层面上提供的方式。

在早期的CPU当中，是通过在总线上加LOCK#锁的形式来解决缓存不一致的问题。因为CPU和其他部件进行通信都是通过总线来进行的，如果对总线加LOCK#锁的话，也就是说阻塞了其他CPU对其他部件访问（如内存），从而使得只能有一个CPU能使用这个变量的内存。比如上面例子中
如果一个线程在执行 i = i
+1，如果在执行这段代码的过程中，在总线上发出了LCOK#锁的信号，那么只有等待这段代码完全执行完毕之后，其他CPU才能从变量i所在的内存读取变量，然后进行相应的操作。这样就解决了缓存不一致的问题。

但是上面的方式会有一个问题，由于在锁住总线期间，其他CPU无法访问内存，导致效率低下。所以就出现了缓存一致性协议。最出名的就是Intel
的MESI协议，MESI协议保证了每个缓存中使用的共享变量的副本是一致的。它核心的思想是：当CPU写数据时，如果发现操作的变量是共享变量，即在其他CPU中也存在该变量的副本，会发出信号通知其他CPU将该变量的缓存行置为无效状态，因此当其他CPU需要读取这个变量时，发现自己缓存中缓存该变量的缓存行是无效的，那么它就会从内存重新读取。

![](http://static.codebaoku.com/pics/42/6f/426f2027958760a00900e738b0e07039.jpg)

##  

## 二. 并发编程中的三个概念

在并发编程中，我们通常会遇到以下三个问题：原子性问题，可见性问题，有序性问题。我们先看具体看一下这三个概念：

**1.原子性**

原子性：即一个操作或者多个操作 要么全部执行并且执行的过程不会被任何因素打断，要么就都不执行。

一个很经典的例子就是银行账户转账问题：比如从账户A向账户B转1000元，那么必然包括2个操作：从账户A减去1000元，往账户B加上1000元。

试想一下，如果这2个操作不具备原子性，会造成什么样的后果。假如从账户A减去1000元之后，操作突然中止。然后又从B取出了500元，取出500元之后，再执行
往账户B加上1000元
的操作。这样就会导致账户A虽然减去了1000元，但是账户B没有收到这个转过来的1000元。所以这2个操作必须要具备原子性才能保证不出现一些意外的问题。

同样地反映到并发编程中会出现什么结果呢？

举个最简单的例子，大家想一下假如为一个32位的变量赋值过程不具备原子性的话，会发生什么后果？


​    

```java
i = 9;
```


假若一个线程执行到这个语句时，我暂且假设为一个32位的变量赋值包括两个过程：为低16位赋值，为高16位赋值。那么就可能发生一种情况：当将低16位数值写入之后，突然被中断，而此时又有一个线程去读取i的值，那么读取到的就是错误的数据。

**2.可见性**

可见性是指当多个线程访问同一个变量时，一个线程修改了这个变量的值，其他线程能够立即看得到修改的值。举个简单的例子，看下面这段代码：


​    

```java
//线程1执行的代码
int i = 0;
i = 10;

//线程2执行的代码
j = i;
```


假若执行线程1的是CPU1，执行线程2的是CPU2。由上面的分析可知，当线程1执行 i
=10这句时，会先把i的初始值加载到CPU1的高速缓存中，然后赋值为10，那么在CPU1的高速缓存当中i的值变为10了，却没有立即写入到主存当中。

此时线程2执行 j =
i，它会先去主存读取i的值并加载到CPU2的缓存当中，注意此时内存当中i的值还是0，那么就会使得j的值为0，而不是10。这就是可见性问题，线程1对变量i修改了之后，线程2没有立即看到线程1修改的值。

**3.有序性**

有序性：即程序执行的顺序按照代码的先后顺序执行。举个简单的例子，看下面这段代码：


​    

```java
int i = 0;               
boolean flag = false;
i = 1;                //语句1   
flag = true;          //语句2
```

上面代码定义了一个int型变量，定义了一个boolean类型变量，然后分别对两个变量进行赋值操作。从代码顺序上看，语句1是在语句2前面的，那么JVM在真正执行这段代码的时候会保证语句1一定会在语句2前面执行吗？不一定，为什么呢？这里可能会发生指令重排序（Instruction
Reorder）。

下面解释一下什么是指令重排序，一般来说，处理器为了提高程序运行效率，可能会对输入代码进行优化，它不保证程序中各个语句的执行先后顺序同代码中的顺序一致，但是它会保证程序最终执行结果和代码顺序执行的结果是一致的。比如上面的代码中，语句1和语句2谁先执行对最终的程序结果并没有影响，那么就有可能在执行过程中，语句2先执行而语句1后执行。

但是要注意，虽然处理器会对指令进行重排序，但是它会保证程序最终结果会和代码顺序执行结果相同，那么它靠什么保证的呢？再看下面一个例子：


​    

```java
int a = 10;    //语句1
int r = 2;    //语句2
a = a + 3;    //语句3
r = a*a;	 //语句4
```


这段代码有4个语句，那么可能的一个执行顺序是：

![](http://static.codebaoku.com/pics/88/0c/880cdda5518b8b0951cf382a37e8c590.jpg)

那么可不可能是这个执行顺序呢： 语句2   语句1    语句4   语句3

不可能，因为处理器在进行重排序时是会考虑指令之间的数据依赖性，如果一个指令Instruction 2必须用到Instruction
1的结果，那么处理器会保证Instruction 1会在Instruction 2之前执行。

虽然重排序不会影响单个线程内程序执行的结果，但是多线程呢？下面看一个例子：


​    

```java
//线程1:
context = loadContext();   //语句1
inited = true;             //语句2

//线程2:
while(!inited ){
  sleep() 
}
doSomethingwithconfig(context);
```


上面代码中，由于语句1和语句2没有数据依赖性，因此可能会被重排序。假如发生了重排序，在线程1执行过程中先执行语句2，而此是线程2会以为初始化工作已经完成，那么就会跳出while循环，去执行doSomethingwithconfig(context)方法，而此时context并没有被初始化，就会导致程序出错。

从上面可以看出，指令重排序不会影响单个线程的执行，但是会影响到线程并发执行的正确性。也就是说，要想并发程序正确地执行，必须要保证原子性、可见性以及有序性。只要有一个没有被保证，就有可能会导致程序运行不正确。



## 三. Java内存模型

在前面谈到了一些关于内存模型以及并发编程中可能会出现的一些问题。下面我们来看一下Java内存模型，研究一下Java内存模型为我们提供了哪些保证以及在java中提供了哪些方法和机制来让我们在进行多线程编程时能够保证程序执行的正确性。

在Java虚拟机规范中试图定义一种Java内存模型（Java Memory
Model，JMM）来屏蔽各个硬件平台和操作系统的内存访问差异，以实现让Java程序在各种平台下都能达到一致的内存访问效果。那么Java内存模型规定了哪些东西呢，它定义了程序中变量的访问规则，往大一点说是定义了程序执行的次序。注意，为了获得较好的执行性能，Java内存模型并没有限制执行引擎使用处理器的寄存器或者高速缓存来提升指令执行速度，也没有限制编译器对指令进行重排序。也就是说，在java内存模型中，也会存在缓存一致性问题和指令重排序的问题。

Java内存模型规定所有的变量都是存在主存当中（类似于前面说的物理内存），每个线程都有自己的工作内存（类似于前面的高速缓存）。线程对变量的所有操作都必须在工作内存中进行，而不能直接对主存进行操作。并且每个线程不能访问其他线程的工作内存。

举个简单的例子：在java中，执行下面这个语句：


​    

```java
i  = 10;
```


执行线程必须先在自己的工作线程中对变量i所在的缓存行进行赋值操作，然后再写入主存当中。而不是直接将数值10写入主存当中。

那么Java语言 本身对 原子性、可见性以及有序性提供了哪些保证呢？

**1.原子性**

在Java中，对基本数据类型的变量的读取和赋值操作是原子性操作，即这些操作是不可被中断的，要么执行，要么不执行。上面一句话虽然看起来简单，但是理解起来并不是那么容易。看下面一个例子i：

请分析以下哪些操作是原子性操作：


​    

```java
x = 10;         //语句1
y = x;         //语句2
x++;           //语句3
x = x + 1;     //语句4
```


有些朋友可能会说上面的4个语句中的操作都是原子性操作。其实只有语句1是原子性操作，其他三个语句都不是原子性操作。

语句1是直接将数值10赋值给x，也就是说线程执行这个语句的会直接将数值10写入到工作内存中。

语句2实际上包含2个操作，它先要去读取x的值，再将x的值写入工作内存，虽然读取x的值以及 将x的值写入工作内存
这2个操作都是原子性操作，但是合起来就不是原子性操作了。

同样的，x++和 x =
x+1包括3个操作：读取x的值，进行加1操作，写入新的值。所以上面4个语句只有语句1的操作具备原子性。也就是说，只有简单的读取、赋值（而且必须是将数字赋值给某个变量，变量之间的相互赋值不是原子操作）才是原子操作。

不过这里有一点需要注意：在32位平台下，对64位数据的读取和赋值是需要通过两个操作来完成的，不能保证其原子性。但是好像在最新的JDK中，JVM已经保证对64位数据的读取和赋值也是原子性操作了。

从上面可以看出，Java内存模型只保证了基本读取和赋值是原子性操作，如果要实现更大范围操作的原子性，可以通过synchronized和Lock来实现。由于synchronized和Lock能够保证任一时刻只有一个线程执行该代码块，那么自然就不存在原子性问题了，从而保证了原子性。

**2.可见性**

对于可见性，Java提供了volatile关键字来保证可见性。当一个共享变量被volatile修饰时，它会保证修改的值会立即被更新到主存，当有其他线程需要读取时，它会去内存中读取新值。

而普通的共享变量不能保证可见性，因为普通共享变量被修改之后，什么时候被写入主存是不确定的，当其他线程去读取时，此时内存中可能还是原来的旧值，因此无法保证可见性。

另外，通过synchronized和Lock也能够保证可见性，synchronized和Lock能保证同一时刻只有一个线程获取锁然后执行同步代码，并且在释放锁之前会将对变量的修改刷新到主存当中。因此可以保证可见性。

**3.有序性**

在Java内存模型中，允许编译器和处理器对指令进行重排序，但是重排序过程不会影响到单线程程序的执行，却会影响到多线程并发执行的正确性。

在Java里面，可以通过volatile关键字来保证一定的“有序性”（具体原理在下一节讲述）。另外可以通过synchronized和Lock来保证有序性，很显然，synchronized和Lock保证每个时刻是有一个线程执行同步代码，相当于是让线程顺序执行同步代码，自然就保证了有序性。

另外，Java内存模型具备一些先天的“有序性”，即不需要通过任何手段就能够得到保证的有序性，这个通常也称为 happens-before
原则。如果两个操作的执行次序无法从happens-before原则推导出来，那么它们就不能保证它们的有序性，虚拟机可以随意地对它们进行重排序。

下面就来具体介绍下happens-before原则（先行发生原则）：

  * 程序次序规则：一个线程内，按照代码顺序，书写在前面的操作先行发生于书写在后面的操作
  * 锁定规则：一个unLock操作先行发生于后面对同一个锁额lock操作
  * volatile变量规则：对一个变量的写操作先行发生于后面对这个变量的读操作
  * 传递规则：如果操作A先行发生于操作B，而操作B又先行发生于操作C，则可以得出操作A先行发生于操作C
  * 线程启动规则：Thread对象的start()方法先行发生于此线程的每个一个动作
  * 线程中断规则：对线程interrupt()方法的调用先行发生于被中断线程的代码检测到中断事件的发生
  * 线程终结规则：线程中所有的操作都先行发生于线程的终止检测，我们可以通过Thread.join()方法结束、Thread.isAlive()的返回值手段检测到线程已经终止执行
  * 对象终结规则：一个对象的初始化完成先行发生于他的finalize()方法的开始

这8条原则摘自《深入理解Java虚拟机》。这8条规则中，前4条规则是比较重要的，后4条规则都是显而易见的。

下面我们来解释一下前4条规则：

对于程序次序规则来说，我的理解就是一段程序代码的执行在单个线程中看起来是有序的。注意，虽然这条规则中提到“书写在前面的操作先行发生于书写在后面的操作”，这个应该是程序看起来执行的顺序是按照代码顺序执行的，因为虚拟机可能会对程序代码进行指令重排序。虽然进行重排序，但是最终执行的结果是与程序顺序执行的结果一致的，它只会对不存在数据依赖性的指令进行重排序。因此，在单个线程中，程序执行看起来是有序执行的，这一点要注意理解。事实上，这个规则是用来保证程序在单线程中执行结果的正确性，但无法保证程序在多线程中执行的正确性。

第二条规则也比较容易理解，也就是说无论在单线程中还是多线程中，同一个锁如果出于被锁定的状态，那么必须先对锁进行了释放操作，后面才能继续进行lock操作。

第三条规则是一条比较重要的规则，也是后文将要重点讲述的内容。直观地解释就是，如果一个线程先去写一个变量，然后一个线程去进行读取，那么写入操作肯定会先行发生于读操作。

第四条规则实际上就是体现happens-before原则具备传递性。



## 四.深入剖析volatile关键字

在前面讲述了很多东西，其实都是为讲述volatile关键字作铺垫，那么接下来我们就进入主题。

**1.volatile关键字的两层语义**

一旦一个共享变量（类的成员变量、类的静态成员变量）被volatile修饰之后，那么就具备了两层语义：

  * 1）保证了不同线程对这个变量进行操作时的可见性，即一个线程修改了某个变量的值，这新值对其他线程来说是立即可见的。
  * 2）禁止进行指令重排序。

先看一段代码，假如线程1先执行，线程2后执行：


​    

```java
//线程1
boolean stop = false;
while(!stop){
	doSomething();
}

//线程2
stop = true;
```


这段代码是很典型的一段代码，很多人在中断线程时可能都会采用这种标记办法。但是事实上，这段代码会完全运行正确么？即一定会将线程中断么？不一定，也许在大多数时候，这个代码能够把线程中断，但是也有可能会导致无法中断线程（虽然这个可能性很小，但是只要一旦发生这种情况就会造成死循环了）。

下面解释一下这段代码为何有可能导致无法中断线程。在前面已经解释过，每个线程在运行过程中都有自己的工作内存，那么线程1在运行的时候，会将stop变量的值拷贝一份放在自己的工作内存当中。

那么当线程2更改了stop变量的值之后，但是还没来得及写入主存当中，线程2转去做其他事情了，那么线程1由于不知道线程2对stop变量的更改，因此还会一直循环下去。

但是用volatile修饰之后就变得不一样了：

第一：使用volatile关键字会强制将修改的值立即写入主存；

第二：使用volatile关键字的话，当线程2进行修改时，会导致线程1的工作内存中缓存变量stop的缓存行无效（反映到硬件层的话，就是CPU的L1或者L2缓存中对应的缓存行无效）；

第三：由于线程1的工作内存中缓存变量stop的缓存行无效，所以线程1再次读取变量stop的值时会去主存读取。

那么在线程2修改stop值时（当然这里包括2个操作，修改线程2工作内存中的值，然后将修改后的值写入内存），会使得线程1的工作内存中缓存变量stop的缓存行无效，然后线程1读取时，发现自己的缓存行无效，它会等待缓存行对应的主存地址被更新之后，然后去对应的主存读取最新的值。

那么线程1读取到的就是最新的正确的值。

**2.volatile保证原子性吗？**

从上面知道volatile关键字保证了操作的可见性，但是volatile能保证对变量的操作是原子性吗？

下面看一个例子：


​    

    public class Test {
    	public volatile int inc = 0;
    	
    	public void increase() {
    		inc++;
    	}
    	
    	public static void main(String[] args) {
    		final Test test = new Test();
    		for(int i=0;i<10;i++){
    			new Thread(){
    				public void run() {
    					for(int j=0;j<1000;j++)
    						test.increase();
    				};
    			}.start();
    		}
    		
    		while(Thread.activeCount()>1)  //保证前面的线程都执行完
    			Thread.yield();
    		System.out.println(test.inc);
    	}
    }


大家想一下这段程序的输出结果是多少？也许有些朋友认为是10000。但是事实上运行它会发现每次运行结果都不一致，都是一个小于10000的数字。可能有的朋友就会有疑问，不对啊，上面是对变量inc进行自增操作，由于volatile保证了可见性，那么在每个线程中对inc自增完之后，在其他线程中都能看到修改后的值啊，所以有10个线程分别进行了1000次操作，那么最终inc的值应该是1000*10=10000。

这里面就有一个误区了，volatile关键字能保证可见性没有错，但是上面的程序错在没能保证原子性。可见性只能保证每次读取的是最新的值，但是volatile没办法保证对变量的操作的原子性。

在前面已经提到过，自增操作是不具备原子性的，它包括读取变量的原始值、进行加1操作、写入工作内存。那么就是说自增操作的三个子操作可能会分割开执行，就有可能导致下面这种情况出现：

假如某个时刻变量inc的值为10，线程1对变量进行自增操作，线程1先读取了变量inc的原始值，然后线程1被阻塞了；然后线程2对变量进行自增操作，线程2也去读取变量inc的原始值，由于线程1只是对变量inc进行读取操作，而没有对变量进行修改操作，所以不会导致线程2的工作内存中缓存变量inc的缓存行无效，所以线程2会直接去主存读取inc的值，发现inc的值时10，然后进行加1操作，并把11写入工作内存，最后写入主存。

然后线程1接着进行加1操作，由于已经读取了inc的值，注意此时在线程1的工作内存中inc的值仍然为10，所以线程1对inc进行加1操作后inc的值为11，然后将11写入工作内存，最后写入主存。那么两个线程分别进行了一次自增操作后，inc只增加了1。

解释到这里，可能有朋友会有疑问，不对啊，前面不是保证一个变量在修改volatile变量时，会让缓存行无效吗？然后其他线程去读就会读到新的值，对，这个没错。这个就是上面的happens-
before规则中的volatile变量规则，但是要注意，线程1对变量进行读取操作之后，被阻塞了的话，并没有对inc值进行修改。然后虽然volatile能保证线程2对变量inc的值读取是从内存中读取的，但是线程1没有进行修改，所以线程2根本就不会看到修改的值。

根源就在这里，自增操作不是原子性操作，而且volatile也无法保证对变量的任何操作都是原子性的。

把上面的代码改成以下任何一种都可以达到效果：

采用synchronized：![](http://static.codebaoku.com/pics/96/1d/961ddebeb323a10fe0623af514929fc1.gif)


​    

```java
public class Test {
    public  int inc = 0;
    
    public synchronized void increase() {
        inc++;
    }
    
    public static void main(String[] args) {
        final Test test = new Test();
        for(int i=0;i<10;i++){
            new Thread(){
                public void run() {
                    for(int j=0;j<1000;j++)
                        test.increase();
                };
            }.start();
        }
        
        while(Thread.activeCount()>1)  //保证前面的线程都执行完
            Thread.yield();
        System.out.println(test.inc);
    }
}
```

采用Lock：![](http://static.codebaoku.com/pics/96/1d/961ddebeb323a10fe0623af514929fc1.gif)


​    

```java
public class Test {
    public  int inc = 0;
    Lock lock = new ReentrantLock();
    
    public  void increase() {
        lock.lock();
        try {
            inc++;
        } finally{
            lock.unlock();
        }
    }
    
    public static void main(String[] args) {
        final Test test = new Test();
        for(int i=0;i<10;i++){
            new Thread(){
                public void run() {
                    for(int j=0;j<1000;j++)
                        test.increase();
                };
            }.start();
        }
        
        while(Thread.activeCount()>1)  //保证前面的线程都执行完
            Thread.yield();
        System.out.println(test.inc);
    }
}
```

采用AtomicInteger：![](http://static.codebaoku.com/pics/96/1d/961ddebeb323a10fe0623af514929fc1.gif)


​    

```java
public class Test {
    public  AtomicInteger inc = new AtomicInteger();
     
    public  void increase() {
        inc.getAndIncrement();
    }
    
    public static void main(String[] args) {
        final Test test = new Test();
        for(int i=0;i<10;i++){
            new Thread(){
                public void run() {
                    for(int j=0;j<1000;j++)
                        test.increase();
                };
            }.start();
        }
        
        while(Thread.activeCount()>1)  //保证前面的线程都执行完
            Thread.yield();
        System.out.println(test.inc);
    }
}
```

在java 1.5的java.util.concurrent.atomic包下提供了一些原子操作类，即对基本数据类型的
自增（加1操作），自减（减1操作）、以及加法操作（加一个数），减法操作（减一个数）进行了封装，保证这些操作是原子性操作。atomic是利用CAS来实现原子性操作的（Compare
And Swap），CAS实际上是利用处理器提供的CMPXCHG指令实现的，而处理器执行CMPXCHG指令是一个原子性操作。

**3.volatile能保证有序性吗？**

在前面提到volatile关键字能禁止指令重排序，所以volatile能在一定程度上保证有序性。

volatile关键字禁止指令重排序有两层意思：

1）当程序执行到volatile变量的读操作或者写操作时，在其前面的操作的更改肯定全部已经进行，且结果已经对后面的操作可见；在其后面的操作肯定还没有进行；

2）在进行指令优化时，不能将在对volatile变量访问的语句放在其后面执行，也不能把volatile变量后面的语句放到其前面执行。

可能上面说的比较绕，举个简单的例子：


​    

```java
//x、y为非volatile变量
//flag为volatile变量

x = 2;        //语句1
y = 0;        //语句2
flag = true;  //语句3
x = 4;         //语句4
y = -1;       //语句5
```


由于flag变量为volatile变量，那么在进行指令重排序的过程的时候，不会将语句3放到语句1、语句2前面，也不会讲语句3放到语句4、语句5后面。但是要注意语句1和语句2的顺序、语句4和语句5的顺序是不作任何保证的。并且volatile关键字能保证，执行到语句3时，语句1和语句2必定是执行完毕了的，且语句1和语句2的执行结果对语句3、语句4、语句5是可见的。

那么我们回到前面举的一个例子：


​    

```java
//线程1:
context = loadContext();   //语句1
inited = true;             //语句2

//线程2:
while(!inited ){
  sleep() 
}
doSomethingwithconfig(context);
```


前面举这个例子的时候，提到有可能语句2会在语句1之前执行，那么久可能导致context还没被初始化，而线程2中就使用未初始化的context去进行操作，导致程序出错。这里如果用volatile关键字对inited变量进行修饰，就不会出现这种问题了，因为当执行到语句2时，必定能保证context已经初始化完毕。

**4.volatile的原理和实现机制**

前面讲述了源于volatile关键字的一些使用，下面我们来探讨一下volatile到底如何保证可见性和禁止指令重排序的。

下面这段话摘自《深入理解Java虚拟机》：

“观察加入volatile关键字和没有加入volatile关键字时所生成的汇编代码发现，加入volatile关键字时，会多出一个lock前缀指令”

lock前缀指令实际上相当于一个内存屏障（也成内存栅栏），内存屏障会提供3个功能：

  * 1）它确保指令重排序时不会把其后面的指令排到内存屏障之前的位置，也不会把前面的指令排到内存屏障的后面；即在执行到内存屏障这句指令时，在它前面的操作已经全部完成；
  * 2）它会强制将对缓存的修改操作立即写入主存；
  * 3）如果是写操作，它会导致其他CPU中对应的缓存行无效。



## 五.使用volatile关键字的场景

synchronized关键字是防止多个线程同时执行一段代码，那么就会很影响程序执行效率，而volatile关键字在某些情况下性能要优于synchronized，但是要注意volatile关键字是无法替代synchronized关键字的，因为volatile关键字无法保证操作的原子性。通常来说，使用volatile必须具备以下2个条件：

  * 1）对变量的写操作不依赖于当前值
  * 2）该变量没有包含在具有其他变量的不变式中

实际上，这些条件表明，可以被写入 volatile
变量的这些有效值独立于任何程序的状态，包括变量的当前状态。事实上，我的理解就是上面的2个条件需要保证操作是原子性操作，才能保证使用volatile关键字的程序在并发时能够正确执行。

下面列举几个Java中使用volatile的几个场景。

**1.状态标记量**


​    

```java
volatile boolean flag = false;

while(!flag){
	doSomething();
}

public void setFlag() {
	flag = true;
}
```




​    
​    

```java
volatile boolean inited = false;
//线程1:
context = loadContext();   
inited = true;             

//线程2:
while(!inited ){
sleep() 
}
doSomethingwithconfig(context);
```




**2.double check**


​    

```java
class Singleton{
	private volatile static Singleton instance = null;
	
	private Singleton() {
		
	}
	
	public static Singleton getInstance() {
		if(instance==null) {
			synchronized (Singleton.class) {
				if(instance==null)
					instance = new Singleton();
			}
		}
		return instance;
	}
}
```





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


​    

```java
Class.forName(driverClass)
//加载MySql驱动
Class.forName("com.mysql.jdbc.Driver")
//加载Oracle驱动
Class.forName("oracle.jdbc.driver.OracleDriver")
```


### 2）获得数据库连接


​    

```java
DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/imooc", "root", "root");
```


### 3）创建 Statement\PreparedStatement 对象


​    

```java
conn.createStatement();
conn.prepareStatement(sql);
```




## 4\. JDBC 完整编程范例


​    

```java
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
```




## 5\. JDBC 增删改查编程范例


​    

```java
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
```



# JDBC PreparedStatement 使用范例

JDBC PreparedStatement 对象扩展了 Statement 对象，给 Statement 对象增加几个高级功能。

JDBC PreparedStatement 对 SQL 语句进行预编译，效率更高。另外，可以接收动态参数，避免 Statement 中的 SQL
注入问题。



## 1\. PreparedStatement 使用范例


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class JDBCExample {
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/EMP";

   //  Database credentials
   static final String USER = "username";
   static final String PASS = "password";
   
   public static void main(String[] args) {
   Connection conn = null;
   PreparedStatement stmt = null;
   try{
      //STEP 2: Register JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      //STEP 3: Open a connection
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);

      //STEP 4: Execute a query
      System.out.println("Creating statement...");
      String sql = "UPDATE Employees set age=? WHERE id=?";
      stmt = conn.prepareStatement(sql);
      
      //Bind values into the parameters.
      stmt.setInt(1, 35);  // This would set age
      stmt.setInt(2, 102); // This would set ID
      
      // Let us update age of the record with ID = 102;
      int rows = stmt.executeUpdate();
      System.out.println("Rows impacted : " + rows );

      // Let us select all the records and display them.
      sql = "SELECT id, first, last, age FROM Employees";
      ResultSet rs = stmt.executeQuery(sql);

      //STEP 5: Extract data from result set
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("id");
         int age = rs.getInt("age");
         String first = rs.getString("first");
         String last = rs.getString("last");

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", Age: " + age);
         System.out.print(", First: " + first);
         System.out.println(", Last: " + last);
      }
      //STEP 6: Clean-up environment
      rs.close();
      stmt.close();
      conn.close();
   }catch(SQLException se){
      //Handle errors for JDBC
      se.printStackTrace();
   }catch(Exception e){
      //Handle errors for Class.forName
      e.printStackTrace();
   }finally{
      //finally block used to close resources
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }// nothing we can do
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }//end finally try
   }//end try
   System.out.println("Goodbye!");
}//end main
}//end JDBCExample
```




## 2\. 编译运行

现在来编译上面的例子：


​    

```java
C:>javac JDBCExample.java
C:>
```

当运行 JDBCExample，它会产生以下结果：


​    

```java
C:>java JDBCExample
Connecting to database...
Creating statement...
Rows impacted : 1
ID: 100, Age: 18, First: Zara, Last: Ali
ID: 101, Age: 25, First: Mahnaz, Last: Fatma
ID: 102, Age: 35, First: Zaid, Last: Khan
ID: 103, Age: 30, First: Sumit, Last: Mittal
Goodbye!
C:>
```



# JDBC Resultset 结果集范例

JDBC ResultSet 通过移动光标的方法浏览结果集。



## 1\. ResultSet 移动光标的方法

| 编号                                                         | 方法                                                 | 描述                       |
| ------------------------------------------------------------ | ---------------------------------------------------- | -------------------------- |
| 1                                                            | public void beforeFirst() throws SQLException        | 将光标移动到第一行之前     |
| 2                                                            | public void afterLast() throws SQLException          | 将光标移动到最后一行之后。 |
| 3                                                            | public boolean first() throws SQLException           | 将光标移动到第一行。       |
| 4                                                            | public void last() throws SQLException               | 将光标移动到最后一行。     |
| 5                                                            | public boolean absolute(int row) throws SQLException | 将光标移动到指定的行。     |
| 6                                                            | public boolean relative(int row) throws SQLException |                            |
| 从当前指向的位置，将光标向前或向后移动给定行数。             |                                                      |                            |
| 7                                                            | public boolean previous() throws SQLException        | 将光标移动到上一行。       |
| 如果上一行关闭结果集，此方法返回false。                      |                                                      |                            |
| 8                                                            | public boolean next() throws SQLException            | 将光标移动到下一行。       |
| 如果结果集中没有更多行，则此方法返回false。                  |                                                      |                            |
| 9                                                            | public int getRow() throws SQLException              | 返回光标指向的行号。       |
| 10                                                           | public void moveToInsertRow() throws SQLException    |                            |
| 将光标移动到结果集中的特殊行，该行可用于将新行插入数据库。当前光标位置被记住。 |                                                      |                            |
| 11                                                           | public void moveToCurrentRow() throws SQLException   |                            |
| 如果光标当前位于插入行，则将光标移回当前行; 否则，此方法什么也不做 |                                                      |                            |



## 2\. ResultSet 浏览结果集范例


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class NavigatingResultSet {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/EMP";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);

            //STEP 4: Execute a query to create statment with
            // required arguments for RS example.
            System.out.println("Creating statement...");
            stmt = conn.createStatement(
                                ResultSet.TYPE_SCROLL_INSENSITIVE,
                                ResultSet.CONCUR_READ_ONLY);
            String sql;
            sql = "SELECT id, first, last, age FROM Employees";
            ResultSet rs = stmt.executeQuery(sql);

            // Move cursor to the last row.
            System.out.println("Moving cursor to the last...");
            rs.last();

            //STEP 5: Extract data from result set
            System.out.println("Displaying record...");
            //Retrieve by column name
            int id  = rs.getInt("id");
            int age = rs.getInt("age");
            String first = rs.getString("first");
            String last = rs.getString("last");

            //Display values
            System.out.print("ID: " + id);
            System.out.print(", Age: " + age);
            System.out.print(", First: " + first);
            System.out.println(", Last: " + last);

            // Move cursor to the first row.
            System.out.println("Moving cursor to the first row...");
            rs.first();

            //STEP 6: Extract data from result set
            System.out.println("Displaying record...");
            //Retrieve by column name
            id  = rs.getInt("id");
            age = rs.getInt("age");
            first = rs.getString("first");
            last = rs.getString("last");

            //Display values
            System.out.print("ID: " + id);
            System.out.print(", Age: " + age);
            System.out.print(", First: " + first);
            System.out.println(", Last: " + last);
            // Move cursor to the first row.

            System.out.println("Moving cursor to the next row...");
            rs.next();

            //STEP 7: Extract data from result set
            System.out.println("Displaying record...");
            id  = rs.getInt("id");
            age = rs.getInt("age");
            first = rs.getString("first");
            last = rs.getString("last");

            //Display values
            System.out.print("ID: " + id);
            System.out.print(", Age: " + age);
            System.out.print(", First: " + first);
            System.out.println(", Last: " + last);

            //STEP 8: Clean-up environment
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                stmt.close();
            }catch(SQLException se2){
            }// nothing we can do
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample
```




## 3\. 编译运行


​    

```java
F:\worksp\jdbc>javac -Djava.ext.dirs=F:\worksp\jdbc\libs NavigatingResultSet.java

F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs NavigatingResultSet
```


运行上面代码，得到以下结果：





# JDBC Statement, PreparedStatement 和 CallableStatement

获得了数据库连接后，我们就可以与数据库进行交互了。JDBC 中的 Statement, CallableStatement 和
PreparedStatement 三个对象，定义了一系列的方法和属性，可以用来向数据库发送 SQL 命令，接收数据。

| 接口              | 使用说明                                                     |
| ----------------- | ------------------------------------------------------------ |
| Statement         | 运行静态 SQL 语句时使用，Statement 不能接收输入参数。        |
| PreparedStatement | 当计划多次使用某条 SQL 语句时使用，并且 PreparedStatement 可以接收输入参数。 |
| CallableStatement | 用来调用数据库的存储过程，CallableStatement 可以接收输入参数。 |



## 1\. Statement 对象

### 1）创建 Statement 对象

Statement 对象由 Connection 对象的 createStatement( ) 方法创建，用来执行静态 SQL 语句，如下所示：


​    

```java
Statement stmt = null;
try {
   stmt = conn.createStatement( );
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   . . .
}
```


一旦创建了一个 Statement 对象，然后可以它的三个执行方法之一执行 SQL 语句。

  * **boolean execute(String SQL)  :**这个方法常用来执行 SQL DDL 语句。
  * **int executeUpdate(String SQL)  :**返回 SQL 语句执行时受影响的行数，常用来执行 INSERT，UPDATE 或 DELETE 语句。 
  * **ResultSet executeQuery(String SQL)  : **返回 ResultSet 对象。常用来执行 SELECT 语句，会得到一个结果集 ResultSet。 

### 2）关闭 Statement 对象

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 Statement 对象。

使用 close() 方法关闭 Statement。


​    

```java
Statement stmt = null;
try {
   stmt = conn.createStatement( );
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   stmt.close();
}
```




## 2\. PreparedStatement 对象

PreparedStatement 接口扩展了 Statement 接口，给 Statement 对象增加几个高级功能。

它对 SQL 语句进行预编译，效率更高。另外，可以接收动态参数，避免 Statement 中的 SQL 注入问题。

### 1）创建 PreparedStatement 对象


​    

```java
PreparedStatement pstmt = null;
try {
   String SQL = "Update Employees SET age = ? WHERE id = ?";
   pstmt = conn.prepareStatement(SQL);
   pstmt.setInt(1, 22);
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   . . .
}
```


在 JDBC 中参数使用 ？代表，在执行 SQL 语句之前，必须提供每一个参数的值。

setXXX() 方法将值绑定到参数，其中 XXX 表示希望绑定到输入参数值的 Java 数据类型。如果忘了提供值，将收到一个SQLException。

每个参数标记是由它的序号位置引用。第一标记表示位置 1，下一个位置为 2 等等。这种方法不同于 Java 数组索引，以 0 开始。

### 2）关闭 PreparedStatement 对象

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 PreparedStatement 对象。

使用 close() 方法关闭 PreparedStatement。


​    

```java
PreparedStatement pstmt = null;
try {
   String SQL = "Update Employees SET age = ? WHERE id = ?";
   pstmt = conn.prepareStatement(SQL);
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   pstmt.close();
}
```




## 3\. CallableStatement 对象

正如一个Connection对象创建Statement和PreparedStatement对象，它也创造了CallableStatement对象这将被用来执行调用数据库存储过程。

### 1）创建 CallableStatement 对象

假设需要执行以下 Oracle 存储过程：


​    

```java
CREATE OR REPLACE PROCEDURE getEmpName 
   (EMP_ID IN NUMBER, EMP_FIRST OUT VARCHAR) AS
BEGIN
   SELECT first INTO EMP_FIRST
   FROM Employees
   WHERE ID = EMP_ID;
END;
```


存储过程有三种类型的参数：IN，OUT和INOUT。 PreparedStatement对象只使用IN参数。
CallableStatement对象可以使用所有三个。

这里是每个的定义：

| 参数  | 描述                                                         |
| ----- | ------------------------------------------------------------ |
| IN    | 它的值是在创建SQL语句时未知的参数。将值绑定到与 setXXX() 方法的参数。 |
| OUT   | 其值由它返回的SQL语句提供的参数。从 OUT 参数的 getXXX() 方法检索值。 |
| INOUT | 同时提供输入和输出值的参数。绑定变量使用 setXXX() 方法，使用 getXXX() 方法检索值。 |

下面的代码显示了使用 Connection.prepareCall() 方法获得存储过程 CallableStatement 对象：


​    

```java
CallableStatement cstmt = null;
try {
   String SQL = "{call getEmpName (?, ?)}";
   cstmt = conn.prepareCall (SQL);
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   . . .
}
```


SQL 表示存储过程，里面使用了参数占位符。

使用 CallableStatement 对象是就像使用 PreparedStatement 对象，执行该语句之前，必须将值绑定到所有的参数，否则将收到一个
SQLException。

如果有 IN 参数，只要按照 PreparedStatement 对象相同的规则，使用 setXXX() 方法绑定的 Java 数据类型。

当使用 OUT 和 INOUT 参数就必须采用额外的 CallableStatement 及 registerOutParameter()
方法。registerOutParameter() 方法绑定数据类型到存储过的返回值。

### 2）关闭 CallableStatement 对象

正如关闭其他 Statement 对象，出于同样的原因，也应该关闭 CallableStatement 对象。

正如关闭一个 Connection 对象来释放数据库资源，出于同样的原因，也应该关闭 CallableStatementv 对象。

使用 close() 方法关闭 CallableStatement。


​    

```java
CallableStatement cstmt = null;
try {
   String SQL = "{call getEmpName (?, ?)}";
   cstmt = conn.prepareCall (SQL);
   . . .
}
catch (SQLException e) {
   . . .
}
finally {
   cstmt.close();
}
```





# JDBC 更新数据范例

在本教程将演示如何在 JDBC 应用程序中，更新数据库的一个表中数据记录。

在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中向数据库插入数据。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序，更新数据库的一个表中数据记录，需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 更新数据范例

复制以下示例代码保存到文件： _UpdateRecords.java_ 中，然后编译并运行如下：


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class UpdateRecords {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Creating statement...");
            stmt = conn.createStatement();
            String sql = "UPDATE student " +
                        "SET age = 22 WHERE id in (100, 101)";
            stmt.executeUpdate(sql);

            // Now you can extract all the records
            // to see the updated records
            sql = "SELECT id, first, last, age FROM student";
            ResultSet rs = stmt.executeQuery(sql);

            while(rs.next()){
                //Retrieve by column name
                int id  = rs.getInt("id");
                int age = rs.getInt("age");
                String first = rs.getString("first");
                String last = rs.getString("last");

                //Display values
                System.out.print("ID: " + id);
                System.out.print(", Age: " + age);
                System.out.print(", First: " + first);
                System.out.println(", Last: " + last);
            }
            rs.close();
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                conn.close();
            }catch(SQLException se){
            }// do nothing
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs UpdateRecords.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs UpdateRecords
Connecting to a selected database...
Thu Jun 01 23:29:03 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Creating statement...
ID: 100, Age: 22, First: C++, Last: Li
ID: 101, Age: 22, First: Python, Last: Py
ID: 102, Age: 30, First: Ruby, Last: Ru
ID: 103, Age: 28, First: Java, Last: Ja
Goodbye!

F:\worksp\jdbc>
```



# JDBC 事务

默认情况下 JDBC 事务处于自动提交模式，每个 SQL 语句都是在完成时自动提交到数据库。

在有些场景下，我们可能想关闭自动提交和管理自己的事务：

  * 为了提高性能；
  * 为了保持业务流程的完整性。
  * 使用分布式事务。

所谓事务就是把单个 SQL 语句或一组 SQL 语句作为一个逻辑单元，如果任何语句失败，整个事务失败。

JDBC驱动程序默认使用 auto-commit 模式，如果要启用手动事务支持，使用 Connection 对象的的 setAutoCommit()
方法。如果传递一个布尔值 false 到 setAutoCommit()，关闭自动提交。可以传递一个布尔值 true 将其重新打开。

例如，如果有一个名为 conn 的 Connection 对象，以下代码来关闭自动提交：


​    

```java
conn.setAutoCommit(false);
```




## 1\. 提交和回滚

一旦已经完成了变化，要提交更改，然后调用 commit（在连接对象）方法，如下所示：


​    

```java
conn.commit( );
```


否则回滚更新，使用下面的代码：


​    

```java
onn.rollback( );
```


下面的例子演示了如何使用一个提交和回滚对象：


​    

```java
try{
   //Assume a valid connection object conn
   conn.setAutoCommit(false);
   Statement stmt = conn.createStatement();
   
   String SQL = "INSERT INTO Employees  " +
                "VALUES (106, 20, 'Rita', 'Tez')";
   stmt.executeUpdate(SQL);  
   //Submit a malformed SQL statement that breaks
   String SQL = "INSERTED IN Employees  " +
                "VALUES (107, 22, 'Sita', 'Singh')";
   stmt.executeUpdate(SQL);
   // If there is no error.
   conn.commit();
}catch(SQLException se){
   // If there is any error.
   conn.rollback();
}
```




## 2\. 使用保存点

JDBC 保存点的接口提供了额外的事务控制。设置一个保存点就是在事务中定义一个逻辑回滚点。如果发生错误，则可以使用 rollback
方法来撤消到上一个保存点。

Connection 对象有两个新的方法，可帮助管理保存点：

  * setSavepoint(String savepointName): 定义了一个新的保存点。它也返回一个Savepoint 对象。
  * releaseSavepoint(Savepoint savepointName): 删除一个保存点。请注意，它需要一个Savepoint 对象作为参数。这个对象通常是由setSavepoint()方法生成一个保存点。

有一个rollback ( String savepointName ) 方法回滚工作到指定的保存点。

下面的例子演示如何使用 Savepoint 对象：


​    

```java
try{
   //Assume a valid connection object conn
   conn.setAutoCommit(false);
   Statement stmt = conn.createStatement();
   
   //set a Savepoint
   Savepoint savepoint1 = conn.setSavepoint("Savepoint1");
   String SQL = "INSERT INTO Employees " +
                "VALUES (106, 20, 'Rita', 'Tez')";
   stmt.executeUpdate(SQL);  
   //Submit a malformed SQL statement that breaks
   String SQL = "INSERTED IN Employees " +
                "VALUES (107, 22, 'Sita', 'Tez')";
   stmt.executeUpdate(SQL);
   // If there is no error, commit the changes.
   conn.commit();

}catch(SQLException se){
   // If there is any error.
   conn.rollback(savepoint1);
}
```


在这种情况下如果 INSERT 语句不成功，一切都将被回滚。





# JDBC 事务提交回滚范例

所谓事务就是把单个 SQL 语句或一组 SQL 语句作为一个逻辑单元，如果任何语句失败，整个事务失败。以下是使用事务教程中描述的提交和回滚的代码示例。



## 1\. JDBC 事务提交回滚范例

复制并将以下示例代码保存到： _CommitAndRollback.java_ 中，编译并运行如下 -


​    

```java
//STEP 1. Import required packages

import java.sql.*;

public class CommitAndRollback {
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/EMP";

   //  Database credentials
   static final String USER = "root";
   static final String PASS = "123456";

 public static void main(String[] args) {
   Connection conn = null;
   Statement stmt = null;
   try{
      //STEP 2: Register JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      //STEP 3: Open a connection
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);

      //STEP 4: Set auto commit as false.
      conn.setAutoCommit(false);

      //STEP 5: Execute a query to create statment with
      // required arguments for RS example.
      System.out.println("Creating statement...");
      stmt = conn.createStatement(
                           ResultSet.TYPE_SCROLL_INSENSITIVE,
                           ResultSet.CONCUR_UPDATABLE);

      //STEP 6: INSERT a row into Employees table
      System.out.println("Inserting one row....");
      String SQL = "INSERT INTO Employees " +
                    "VALUES (106, 28, 'Curry', 'Stephen')";
      stmt.executeUpdate(SQL);  

      //STEP 7: INSERT one more row into Employees table
      SQL = "INSERT INTO Employees " +
                    "VALUES (107, 32, 'Kobe', 'Bryant')";
      stmt.executeUpdate(SQL);

      //STEP 8: Commit data here.
      System.out.println("Commiting data here....");
      conn.commit();

      //STEP 9: Now list all the available records.
      String sql = "SELECT id, first, last, age FROM Employees";
      ResultSet rs = stmt.executeQuery(sql);
      System.out.println("List result set for reference....");
      printRs(rs);

      //STEP 10: Clean-up environment
      rs.close();
      stmt.close();
      conn.close();
   }catch(SQLException se){
      //Handle errors for JDBC
      se.printStackTrace();
      // If there is an error then rollback the changes.
      System.out.println("Rolling back data here....");
      try{
         if(conn!=null)
            conn.rollback();
      }catch(SQLException se2){
         se2.printStackTrace();
      }//end try

   }catch(Exception e){
      //Handle errors for Class.forName
      e.printStackTrace();
   }finally{
      //finally block used to close resources
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }// nothing we can do
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }//end finally try
   }//end try
   System.out.println("Goodbye!");
}//end main

   public static void printRs(ResultSet rs) throws SQLException{
      //Ensure we start with first row
      rs.beforeFirst();
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("id");
         int age = rs.getInt("age");
         String first = rs.getString("first");
         String last = rs.getString("last");

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", Age: " + age);
         System.out.print(", First: " + first);
         System.out.println(", Last: " + last);
     }
     System.out.println();
   }//end printRs()
}//end JDBCExample
```




## 2\. 运行提交回滚范例

编译并运行结果如下 -


​    

```javascript
F:\worksp\jdbc>javac -Djava.ext.dirs=F:\worksp\jdbc\libs CommitAndRollback.java

F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs CommitAndRollback
Connecting to database...
Thu Jun 01 02:30:04 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Creating statement...
Inserting one row....
Commiting data here....
List result set for reference....
ID: 100, Age: 28, First: Max, Last: Su
ID: 101, Age: 25, First: Wei, Last: Wang
ID: 102, Age: 35, First: Xueyou, Last: Zhang
ID: 103, Age: 30, First: Jack, Last: Ma
ID: 106, Age: 28, First: Curry, Last: Stephen
ID: 107, Age: 32, First: Kobe, Last: Bryant

Goodbye!

F:\worksp\jdbc>
```



# JDBC 事务保存点范例

JDBC 保存点的接口提供了额外的事务控制。设置一个保存点就是在事务中定义一个逻辑回滚点。如果发生错误，则可以使用 rollback
方法来撤消到上一个保存点。

复制并将以下示例代码保存到： _JDBCSavepoint.java_ 中，编译并运行如下：



## 1\. JDBC 事务保存点范例


​    

```java
//STEP 1. Import required packages

import java.sql.*;

public class JDBCSavepoint {
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/EMP";

   //  Database credentials
   static final String USER = "root";
   static final String PASS = "123456";

    public static void main(String[] args) {
    Connection conn = null;
    Statement stmt = null;
    try{
        //STEP 2: Register JDBC driver
        Class.forName("com.mysql.jdbc.Driver");

        //STEP 3: Open a connection
        System.out.println("Connecting to database...");
        conn = DriverManager.getConnection(DB_URL,USER,PASS);

        //STEP 4: Set auto commit as false.
        conn.setAutoCommit(false);

        //STEP 5: Execute a query to delete statment with
        // required arguments for RS example.
        System.out.println("Creating statement...");
        stmt = conn.createStatement();

        //STEP 6: Now list all the available records.
        String sql = "SELECT id, first, last, age FROM Employees";
        ResultSet rs = stmt.executeQuery(sql);
        System.out.println("List result set for reference....");
        printRs(rs);

        // STEP 7: delete rows having ID grater than 104
        // But save point before doing so.
        Savepoint savepoint1 = conn.setSavepoint("ROWS_DELETED_1");
        System.out.println("Deleting row....");
        String SQL = "DELETE FROM Employees " +
                    "WHERE ID = 106";
        stmt.executeUpdate(SQL);  
        // oops... we deleted too wrong employees!
        //STEP 8: Rollback the changes afetr save point 2.
        conn.rollback(savepoint1);

        // STEP 9: delete rows having ID grater than 104
        // But save point before doing so.
        Savepoint savepoint2 = conn.setSavepoint("ROWS_DELETED_2");
        System.out.println("Deleting row....");
        SQL = "DELETE FROM Employees " +
                    "WHERE ID = 107";
        stmt.executeUpdate(SQL);  

        //STEP 10: Now list all the available records.
        sql = "SELECT id, first, last, age FROM Employees";
        rs = stmt.executeQuery(sql);
        System.out.println("List result set for reference....");
        printRs(rs);

        //STEP 10: Clean-up environment
        rs.close();
        stmt.close();
        conn.close();
    }catch(SQLException se){
        //Handle errors for JDBC
        se.printStackTrace();
        // If there is an error then rollback the changes.
        System.out.println("Rolling back data here....");
        try{
            if(conn!=null)
                conn.rollback();
        }catch(SQLException se2){
            se2.printStackTrace();
        }//end try

    }catch(Exception e){
        //Handle errors for Class.forName
        e.printStackTrace();
    }finally{
        //finally block used to close resources
        try{
            if(stmt!=null)
                stmt.close();
        }catch(SQLException se2){
        }// nothing we can do
        try{
            if(conn!=null)
                conn.close();
        }catch(SQLException se){
            se.printStackTrace();
        }//end finally try
    }//end try
    System.out.println("Goodbye!");
    }//end main

   public static void printRs(ResultSet rs) throws SQLException{
      //Ensure we start with first row
      rs.beforeFirst();
      while(rs.next()){
         //Retrieve by column name
         int id  = rs.getInt("id");
         int age = rs.getInt("age");
         String first = rs.getString("first");
         String last = rs.getString("last");

         //Display values
         System.out.print("ID: " + id);
         System.out.print(", Age: " + age);
         System.out.print(", First: " + first);
         System.out.println(", Last: " + last);
     }
     System.out.println();
   }//end printRs()
}//end JDBCExample
```




## 2\. 编译运行

编译并运行结果如下 -


​    

```java
F:\worksp\jdbc>javac -Djava.ext.dirs=F:\worksp\jdbc\libs JDBCSavepoint.java

F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs JDBCSavepoint
Connecting to database...
Thu Jun 01 02:35:49 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Creating statement...
List result set for reference....
ID: 100, Age: 28, First: Max, Last: Su
ID: 101, Age: 25, First: Wei, Last: Wang
ID: 102, Age: 35, First: Xueyou, Last: Zhang
ID: 103, Age: 30, First: Jack, Last: Ma
ID: 106, Age: 28, First: Curry, Last: Stephen
ID: 107, Age: 32, First: Kobe, Last: Bryant

Deleting row....
Deleting row....
List result set for reference....
ID: 100, Age: 28, First: Max, Last: Su
ID: 101, Age: 25, First: Wei, Last: Wang
ID: 102, Age: 35, First: Xueyou, Last: Zhang
ID: 103, Age: 30, First: Jack, Last: Ma
ID: 106, Age: 28, First: Curry, Last: Stephen

Goodbye!

F:\worksp\jdbc>
```

`

可以看到，上面代码中只回滚到保存点(ROWS_DELETED_1)，所以ID为 106 的这一行记录没有被删除，而ID 107
的记录因为没有设置回滚点，直接提交删除了。




# JDBC 批量处理

批量处理允许将相关的SQL语句分组到批处理中，并通过对数据库的一次调用来提交它们，一次执行完成与数据库之间的交互。

一次向数据库发送多个SQL语句时，可以减少通信开销，从而提高性能。



## 1\. JDBC 批量处理方法

  * 使用 DatabaseMetaData.supportsBatchUpdates() 方法来确定目标数据库是否支持批量更新处理。如果 JDBC 驱动程序支持此功能，该方法将返回 true。
  * Statement， PreparedStatement 和 CallableStatement 的 addBatch() 方法用于将单个语句添加到批处理。 executeBatch()用于执行组成批量的所有语句。
  * executeBatch() 返回一个整数数组，数组的每个元素表示相应更新语句的更新计数。
  * 就像将批处理语句添加到处理中一样，可以使用 clearBatch() 方法删除它们。此方法将删除所有使用 addBatch() 方法添加的语句。但是，无法指定选择某个要删除的语句。



## 2\. 使用 Statement 批处理步骤

以下是使用 Statement对象的批处理的典型步骤序列 -

  * 使用 createStatement() 方法创建 Statement 对象。
  * 使用 setAutoCommit() 将自动提交设置为 false。
  * 使用 addBatch() 方法在创建的 Statement 对象上添加 SQL 语句到批处理中。
  * 在创建的 Statement 对象上使用 executeBatch() 方法执行所有SQL语句。
  * 最后，使用 commit()方法提交所有更改。



## 3\. 使用 Statement 批处理范例

以下代码片段提供了使用 Statement对象的批量更新示例：


​    

```java
// Create statement object
Statement stmt = conn.createStatement();

// Set auto-commit to false
conn.setAutoCommit(false);

// Create SQL statement
String SQL = "INSERT INTO Employees (id, first, last, age) " +
             "VALUES(200,'Ruby', 'Yang', 30)";
// Add above SQL statement in the batch.
stmt.addBatch(SQL);

// Create one more SQL statement
String SQL = "INSERT INTO Employees (id, first, last, age) " +
             "VALUES(201,'Java', 'Lee', 35)";
// Add above SQL statement in the batch.
stmt.addBatch(SQL);

// Create one more SQL statement
String SQL = "UPDATE Employees SET age = 35 " +
             "WHERE id = 100";
// Add above SQL statement in the batch.
stmt.addBatch(SQL);

// Create an int[] to hold returned values
int[] count = stmt.executeBatch();

//Explicitly commit statements to apply changes
conn.commit();
```




## 4\. 使用 PrepareStatement 批处理步骤

以下是使用 PrepareStatement对象进行批处理的典型步骤顺序：

  * 使用占位符创建SQL语句。
  * 使用 prepareStatement()方法创建 PrepareStatement对象。
  * 使用 setAutoCommit()将自动提交设置为 false。
  * 使用 addBatch()方法在创建的 Statement对象上添加SQL语句到批处理中。
  * 在创建的 Statement对象上使用 executeBatch()方法执行所有SQL语句。
  * 最后，使用 commit()方法提交所有更改。



## 5\. 使用 PreparedStatement 批处理范例

以下代码段提供了使用 PreparedStatement 对象进行批量更新的示例：


​    

```java
// Create SQL statement
String SQL = "INSERT INTO Employees (id, first, last, age) " +
             "VALUES(?, ?, ?, ?)";

// Create PrepareStatement object
PreparedStatemen pstmt = conn.prepareStatement(SQL);

//Set auto-commit to false
conn.setAutoCommit(false);

// Set the variables
pstmt.setInt( 1, 400 );
pstmt.setString( 2, "JDBC" );
pstmt.setString( 3, "Li" );
pstmt.setInt( 4, 33 );
// Add it to the batch
pstmt.addBatch();

// Set the variables
pstmt.setInt( 1, 401 );
pstmt.setString( 2, "CSharp" );
pstmt.setString( 3, "Liang" );
pstmt.setInt( 4, 31 );
// Add it to the batch
pstmt.addBatch();

//add more batches
.
.
.
.
//Create an int[] to hold returned values
int[] count = stmt.executeBatch();

//Explicitly commit statements to apply changes
conn.commit();
```


# JDBC 插入数据范例

在本教程将演示如何在 JDBC 应用程序中向数据库的一个表中插入数据记录。在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中向数据库插入数据。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序插入数据库需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 插入数据范例

复制以下示例代码保存到文件： _InsertRecords.java_ 中，然后编译并运行如下：


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class InsertRecords {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Inserting records into the table...");
            stmt = conn.createStatement();

            String sql = "INSERT INTO student " +
                        "VALUES (100, 'C++', 'Li', 18)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO student " +
                        "VALUES (101, 'Python', 'Py', 25)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO student " +
                        "VALUES (102, 'Ruby', 'Ru', 30)";
            stmt.executeUpdate(sql);
            sql = "INSERT INTO student " +
                        "VALUES(103, 'Java', 'Ja', 28)";
            stmt.executeUpdate(sql);
            System.out.println("Inserted records into the table...");

        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                conn.close();
            }catch(SQLException se){
            }// do nothing
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs InsertRecords.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs InsertRecords
Connecting to a selected database...
Thu Jun 01 22:51:41 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Inserting records into the table...
Inserted records into the table...
Goodbye!

F:\worksp\jdbc>
```


在执行上面语句后，查询 student 表中的数据如下:


​    

```sql
mysql> select * from student;
+-----+--------+------+-----+
| id  | first  | last | age |
+-----+--------+------+-----+
| 100 | C++    | Li   |  18 |
| 101 | Python | Py   |  25 |
| 102 | Ruby   | Ru   |  30 |
| 103 | Java   | Ja   |  28 |
+-----+--------+------+-----+
4 rows in set

mysql>
```





# JDBC 创建、删除表范例

在本教程将演示如何在 JDBC 应用程序中创建 和 删除表。

删除表后，表中的所有内容都将丢失，所以必须在继续删除表之前作出明确的决定。



## 1\. 创建表范例

复制以下示例代码保存到文件： _CreateTable.java_ 中，然后编译并运行如下:


​    

```java
//STEP 1. Import required packages

import java.sql.*;

public class CreateTable {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Creating table in given database...");
            stmt = conn.createStatement();

            String sql = "CREATE TABLE student " +
                        "(id INTEGER not NULL, " +
                        " first VARCHAR(255), " + 
                        " last VARCHAR(255), " + 
                        " age INTEGER, " + 
                        " PRIMARY KEY ( id ))"; 

            stmt.executeUpdate(sql);
            System.out.println("Created table in given database...");
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                conn.close();
            }catch(SQLException se){
            }// do nothing
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}   
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs CreateTable.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs CreateTable
Connecting to a selected database...
Thu Jun 01 22:17:34 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Creating table in given database...
Created table in given database...
Goodbye!
```




## 2\. 删除表范例

复制以下示例代码保存到文件： _DropTable.java_ 中，然后编译并运行如下:


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class DropTable {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Deleting table in given database...");
            stmt = conn.createStatement();

            String sql = "DROP TABLE student ";

            stmt.executeUpdate(sql);
            System.out.println("Table  deleted in given database...");
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                conn.close();
            }catch(SQLException se){
            }// do nothing
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}   
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs DropTable.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs DropTable

Connecting to a selected database...
Thu Jun 01 22:39:01 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Deleting table in given database...
Table  deleted in given database...
Goodbye!
```


在执行上面语句后，数据库 jdbc_db 中的 student 表将会被成功地删除了。



# JDBC 创建数据库范例

在本教程将演示如何在 JDBC 应用程序中创建数据库。在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中创建数据库。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序创建数据库需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 创建数据库范例

复制以下示例代码保存到文件： _CreateDatabase.java_ 中，然后编译并运行如下：


​    
    


    import java.sql.*;
    
    public class CreateDatabase {
       // JDBC driver name and database URL
       static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
       static final String DB_URL = "jdbc:mysql://localhost/";
    
       //  Database credentials
       static final String USER = "root";
       static final String PASS = "123456";
    
       public static void main(String[] args) {
       Connection conn = null;
       Statement stmt = null;
       try{
          //STEP 2: Register JDBC driver
          Class.forName("com.mysql.jdbc.Driver");
    
          //STEP 3: Open a connection
          System.out.println("Connecting to database...");
          conn = DriverManager.getConnection(DB_URL, USER, PASS);
    
          //STEP 4: Execute a query
          System.out.println("Creating database...");
          stmt = conn.createStatement();
    
          String sql = "CREATE DATABASE jdbc_db";
          stmt.executeUpdate(sql);
          System.out.println("Database created successfully...");
       }catch(SQLException se){
          //Handle errors for JDBC
          se.printStackTrace();
       }catch(Exception e){
          //Handle errors for Class.forName
          e.printStackTrace();
       }finally{
          //finally block used to close resources
          try{
             if(stmt!=null)
                stmt.close();
          }catch(SQLException se2){
          }// nothing we can do
          try{
             if(conn!=null)
                conn.close();
          }catch(SQLException se){
             se.printStackTrace();
          }//end finally try
       }//end try
       System.out.println("Goodbye!");
    }//end main
    }//end JDBCExample


编译上面代码，如下 -


​    
    F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs CreateDatabase.java


执行上面代码，如下 -


​    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs CreateDatabase
    Connecting to database...
    Thu Jun 01 21:55:55 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
    Creating database...
    Database created successfully...
    Goodbye!


    F:\worksp\jdbc>



# JDBC 删除数据范例

在本教程将演示如何在 JDBC
应用程序中在数据库的删除表中数据记录。在执行删除数据记录时，需要注意的是数据删除后无法恢复，所以在删除数据之后必须要确认要删除的数据。

在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中向数据库插入数据。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序删除数据需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 删除数据范例

复制以下示例代码保存到文件： _DeleteRecords.java_ 中，然后编译并运行如下：


​    
    //STEP 1. Import required packages
    import java.sql.*;


    public class DeleteRecords {
        // JDBC driver name and database URL
        static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
        static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";
    
        //  Database credentials
        static final String USER = "root";
        static final String PASS = "123456";
    
        public static void main(String[] args) {
            Connection conn = null;
            Statement stmt = null;
            try{
                //STEP 2: Register JDBC driver
                Class.forName("com.mysql.jdbc.Driver");
    
                //STEP 3: Open a connection
                System.out.println("Connecting to a selected database...");
                conn = DriverManager.getConnection(DB_URL, USER, PASS);
                System.out.println("Connected database successfully...");
    
                //STEP 4: Execute a query
                System.out.println("Creating statement...");
                stmt = conn.createStatement();
                String sql = "DELETE FROM student " +
                            "WHERE id = 101";
                stmt.executeUpdate(sql);
    
                // Now you can extract all the records
                // to see the remaining records
                sql = "SELECT id, first, last, age FROM student";
                ResultSet rs = stmt.executeQuery(sql);
    
                while(rs.next()){
                    //Retrieve by column name
                    int id  = rs.getInt("id");
                    int age = rs.getInt("age");
                    String first = rs.getString("first");
                    String last = rs.getString("last");
    
                    //Display values
                    System.out.print("ID: " + id);
                    System.out.print(", Age: " + age);
                    System.out.print(", First: " + first);
                    System.out.println(", Last: " + last);
                }
                rs.close();
            }catch(SQLException se){
                //Handle errors for JDBC
                se.printStackTrace();
            }catch(Exception e){
                //Handle errors for Class.forName
                e.printStackTrace();
            }finally{
                //finally block used to close resources
                try{
                    if(stmt!=null)
                    conn.close();
                }catch(SQLException se){
                }// do nothing
                try{
                    if(conn!=null)
                    conn.close();
                }catch(SQLException se){
                    se.printStackTrace();
                }//end finally try
            }//end try
            System.out.println("Goodbye!");
        }//end main
    }


编译上面代码，如下 -


​    
    F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs DeleteRecords.java


执行上面代码，如下 -


​    
    F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs DeleteRecords
    Connecting to a selected database...
    Thu Jun 01 23:38:33 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
    Connected database successfully...
    Creating statement...
    ID: 100, Age: 22, First: C++, Last: Li
    ID: 102, Age: 30, First: Ruby, Last: Ru
    ID: 103, Age: 28, First: Java, Last: Ja
    Goodbye!


    F:\worksp\jdbc>



# JDBC 删除数据库范例

在本教程将演示如何在 JDBC 应用程序中删除数据库。

在继续删除数据库之前必须要确定是否真的执行删除操作，因为删除了数据库以后，数据库中的所有内容都将丢失，并且无法恢复。

在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中创建数据库。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序创建数据库需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 删除数据库范例

复制以下示例代码保存到文件： _DropDatabase.java_ 中，然后编译并运行如下:


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class DropDatabase {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Deleting database...");
            stmt = conn.createStatement();

            String sql = "DROP DATABASE jdbc_db";
            stmt.executeUpdate(sql);
            System.out.println("Database deleted successfully...");
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                    conn.close();
            }catch(SQLException se){
            }// do nothing

            try{
                if(conn!=null)
                    conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs DropDatabase.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs DropDatabase
Connecting to a selected database...
Thu Jun 01 22:09:06 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Deleting database...
Database deleted successfully...
Goodbye!

F:\worksp\jdbc>
```



# JDBC 异常处理

异常处理，是指可以在一个受控制的方式处理异常情况，如程序定义的错误。

当异常情况发生时，将引发异常，控制被重定向到适用的 catch 子句。如果没有适用 catch 子句存在，那么程序的执行结束。

JDBC 的异常处理非常类似于 Java Excpetion 处理，但对于 JDBC，最常见的异常处理的是
**java.sql.SQLException。**



## 1\. SQLException 方法

SQLException 对象可用于检索有关异常的附加信息：

| 方法                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| getErrorCode( )                                              | 获取与异常关联的错误号。                                     |
| getMessage( )                                                | 获取JDBC驱动程序的错误消息由驱动程序处理错误或获取Oracle错误号和消息的一个数据库错误。 |
| getSQLState( )                                               | 获取XOPEN                                                    |
| SQLSTATE字符串。对于JDBC驱动程序的错误，没有有用的信息从该方法返回。对于一个数据库错误，则返回五位XOPEN |                                                              |
| SQLSTATE代码。这种方法可以返回null。                         |                                                              |
| getNextException()                                           | 获取异常链的下一个Exception对象。                            |
| printStackTrace( )                                           | 打印当前的异常，或者抛出，其回溯到标准错误流。               |
| printStackTrace(PrintStream s)                               | 打印此抛出，其回溯到指定的打印流。                           |
| printStackTrace(PrintWriter w)                               | 打印此抛出，其回溯到指定的打印写入。                         |



## 2\. JDBC 异常处理方法

利用可从 Exception 对象捕获异常的信息，并适当地继续运行程序。

这里是一个 try块的一般形式为：


​    

```java
try {
// Your risky code goes between these curly braces!!!
}
catch(Exception ex) {
// Your exception handling code goes between these 
// curly braces, similar to the exception clause 
// in a PL/SQL block.
}
finally {
// Your must-always-be-executed code goes between these 
// curly braces. Like closing database connection.
}
```

例如：


​    

```java
/STEP 1. Import required packages
import java.sql.*;

public class JDBCExample {
// JDBC driver name and database URL
static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
static final String DB_URL = "jdbc:mysql://localhost/EMP";

//  Database credentials
static final String USER = "username";
static final String PASS = "password";

public static void main(String[] args) {
Connection conn = null;
try{
//STEP 2: Register JDBC driver
Class.forName("com.mysql.jdbc.Driver");

//STEP 3: Open a connection
System.out.println("Connecting to database...");
conn = DriverManager.getConnection(DB_URL,USER,PASS);

//STEP 4: Execute a query
System.out.println("Creating statement...");
Statement stmt = conn.createStatement();
String sql;
sql = "SELECT id, first, last, age FROM Employees";
ResultSet rs = stmt.executeQuery(sql);

//STEP 5: Extract data from result set
while(rs.next()){
//Retrieve by column name
int id  = rs.getInt("id");
int age = rs.getInt("age");
String first = rs.getString("first");
String last = rs.getString("last");

//Display values
System.out.print("ID: " + id);
System.out.print(", Age: " + age);
System.out.print(", First: " + first);
System.out.println(", Last: " + last);
}
//STEP 6: Clean-up environment
rs.close();
stmt.close();
conn.close();
}catch(SQLException se){
//Handle errors for JDBC
se.printStackTrace();
}catch(Exception e){
//Handle errors for Class.forName
e.printStackTrace();
}finally{
//finally block used to close resources
try{
if(conn!=null)
conn.close();
}catch(SQLException se){
se.printStackTrace();
}//end finally try
}//end try
System.out.println("Goodbye!");
}//end main
}//end JDBCExample
```

现在让我们来编译上面的例子如下：


​    

```java
C:>javac JDBCExample.java
C:>
```

当运行JDBCExample，如果没有问题它会产生以下结果，否则相应的错误将被捕获并会显示错误消息：


​    

```java
C:>java JDBCExample
Connecting to database...
Creating statement...
ID: 100, Age: 18, First: Zara, Last: Ali
ID: 101, Age: 25, First: Mahnaz, Last: Fatma
ID: 102, Age: 30, First: Zaid, Last: Khan
ID: 103, Age: 28, First: Sumit, Last: Mittal
C:>
```



# JDBC 查询数据数据范例

在本教程将演示如何在 JDBC 应用程序中，查询数据库的一个表中数据记录。

在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中向数据库插入数据。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序向表中查询数据记录，需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 查询数据数据范例

复制以下示例代码保存到文件： _SelectRecords.java_ 中，然后编译并运行如下：


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class SelectRecords {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");

            //STEP 4: Execute a query
            System.out.println("Creating statement...");
            stmt = conn.createStatement();

            String sql = "SELECT id, first, last, age FROM student";
            ResultSet rs = stmt.executeQuery(sql);
            //STEP 5: Extract data from result set
            while(rs.next()){
                //Retrieve by column name
                int id  = rs.getInt("id");
                int age = rs.getInt("age");
                String first = rs.getString("first");
                String last = rs.getString("last");

                //Display values
                System.out.print("ID: " + id);
                System.out.print(", Age: " + age);
                System.out.print(", First: " + first);
                System.out.println(", Last: " + last);
            }
            rs.close();
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                conn.close();
            }catch(SQLException se){
            }// do nothing
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample    
```


编译上面代码，如下 -


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs SelectRecords.java
```


执行上面代码，如下 -


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs SelectRecords
Connecting to a selected database...
Thu Jun 01 23:11:55 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Creating statement...
ID: 100, Age: 18, First: C++, Last: Li
ID: 101, Age: 25, First: Python, Last: Py
ID: 102, Age: 30, First: Ruby, Last: Ru
ID: 103, Age: 28, First: Java, Last: Ja
Goodbye!

F:\worksp\jdbc>
```





# JDBC 连接数据库范例

本教程提供了如何创建JDBC应用程序的范例，包括：如何打开一个数据库连接，执行 SQL 查询，并显示执行结果。



## 1\. JDBC 连接数据库步骤

构建一个 JDBC 连接数据库应用程序的六个步骤：

### 1）导入数据包

需要包括含有需要进行数据库编程的JDBC类的包。大多数情况下，使用 import java.sql.* 就可以了。

### 2）注册JDBC驱动程序

可以与数据库打开一个通信通道。

### 3）打开连接

需要使用 DriverManager.getConnection() 方法创建一个 Connection 对象，它代表与数据库的物理连接。

### 4）执行查询

需要使用类型声明的对象建立并提交一个SQL语句到数据库。

### 5）从结果集中提取数据

要求使用适当的关于 ResultSet.getXXX() 方法来检索结果集的数据。

### 6）清理环境

需要明确地关闭所有的数据库资源相对依靠JVM的垃圾收集。



## 2\. JDBC 连接数据库实例

这个范例可以作为一个模板，在需要建立JDBC应用程序。


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class FirstExample {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/EMP";

    //  Database credentials
    static final String USER = "username";
    static final String PASS = "password";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);

            //STEP 4: Execute a query
            System.out.println("Creating statement...");
            stmt = conn.createStatement();
            String sql;
            sql = "SELECT id, first, last, age FROM Employees";
            ResultSet rs = stmt.executeQuery(sql);

            //STEP 5: Extract data from result set
            while(rs.next()){
                //Retrieve by column name
                int id  = rs.getInt("id");
                int age = rs.getInt("age");
                String first = rs.getString("first");
                String last = rs.getString("last");

                //Display values
                System.out.print("ID: " + id);
                System.out.print(", Age: " + age);
                System.out.print(", First: " + first);
                System.out.println(", Last: " + last);
            }
            //STEP 6: Clean-up environment
            rs.close();
            stmt.close();
            conn.close();
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(stmt!=null)
                    stmt.close();
            }catch(SQLException se2){
            }// nothing we can do
            try{
                if(conn!=null)
                    conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}
```


现在来编译上面的例子如下：


​    

```java
C:>javac FirstExample.java
C:>
```


当运行FirstExample，它会产生以下结果：


​    

```java
C:>java FirstExample
Connecting to database...
Creating statement...
ID: 100, Age: 18, First: Zara, Last: Ali
ID: 101, Age: 25, First: Mahnaz, Last: Fatma
ID: 102, Age: 30, First: Zaid, Last: Khan
ID: 103, Age: 28, First: Sumit, Last: Mittal
C:>
```



# JDBC 连接数据库步骤

建立一个 JDBC 数据库连接共有四个步骤：

  * **导入 JDBC 包：**  添加 import 语句到 Java 程序导入所需的类在 Java 代码中。
  * **注册 JDBC 驱动程序：** 这一步会导致 JVM 加载所需的驱动程序实现到内存中，因此它可以实现 JDBC 请求。
  * **制定数据库 URL：** 这是创建格式正确的地址指向到要连接的数据库。
  * **创建连接对象：** 最后，代码调用 DriverManager 对象的 getConnection() 方法来建立实际的数据库连接。



## 1\. 导入 JDBC 包

import 语句告诉Java编译器在哪里可以找到在代码中引用，并放置在您的源代码最开始的类。

使用标准的JDBC包，它允许选择，插入，更新和SQL表中删除数据，添加以下进口到您的源代码：


​    

```java
import java.sql.* ;  // for standard JDBC programs
import java.math.* ; // for BigDecimal and BigInteger support
```




## 2\. 注册 JDBC 驱动程序

使用 JDBC 创建连接之前，必须在程序中注册驱动程序。注册过程只能一次，可以通过以下两种方式之一注册一个驱动程序。

### **1）Class.forName()：**

注册一个驱动程序中最常用的方法是使用 Java 的 Class.forName()
方法来动态加载驱动程序的类文件到内存中，它会自动将其注册。这种方法是可取的，因为它允许使驱动注册配置，便于携带。

下面的示例使用 Class.forName() 来注册 Oracle 驱动程序：


​    

```java
try {
   Class.forName("oracle.jdbc.driver.OracleDriver");
}
catch(ClassNotFoundException ex) {
   System.out.println("Error: unable to load driver class!");
   System.exit(1);
}
```


可以使用 getInstance() 方法来解决不兼容的JVM，但要编写了两个额外的例外情况如下：


​    

```java
try {
   Class.forName("oracle.jdbc.driver.OracleDriver").newInstance();
}
catch(ClassNotFoundException ex) {
   System.out.println("Error: unable to load driver class!");
   System.exit(1);
catch(IllegalAccessException ex) {
   System.out.println("Error: access problem while loading!");
   System.exit(2);
catch(InstantiationException ex) {
   System.out.println("Error: unable to instantiate driver!");
   System.exit(3);
}
```


### 2）DriverManager.registerDriver()：

第二种注册驱动程序的方法是使用 static DriverManager.registerDriver() 方法。

下面的示例使用 registerDriver() 来注册Oracle驱动程序：


​    

```java
try {
   Driver myDriver = new oracle.jdbc.driver.OracleDriver();
   DriverManager.registerDriver( myDriver );
}
catch(ClassNotFoundException ex) {
   System.out.println("Error: unable to load driver class!");
   System.exit(1);
}
```



## 3\. 制定数据库 URL

当加载驱动程序完成后，可以使用 DriverManager.getConnection() 方法获得连接。为方便参考，我们列出了三个重载
DriverManager.getConnection() 方法：

  * getConnection(String url)

  * getConnection(String url, Properties prop)

  * getConnection(String url, String user, String password)

在这里，每个方法都需要一个数据库 URL，它指向数据库地址。

下表列出了常用 JDBC 驱动程序名和数据库的 URL。

| RDBMS                                        | JDBC驱动程序的名称              | URL 格式                                |
| -------------------------------------------- | ------------------------------- | --------------------------------------- |
| MySQL                                        | com.mysql.jdbc.Driver           | jdbc:mysql://hostname:port/databaseName |
| ORACLE                                       | oracle.jdbc.driver.OracleDriver |                                         |
| jdbc:oracle:thin:@hostname:port:databaseName |                                 |                                         |
| DB2                                          | COM.ibm.db2.jdbc.net.DB2Driver  | **jdbc:db2:**                           |
| hostname:port/databaseName                   |                                 |                                         |
| Sybase                                       | com.sybase.jdbc.SybDriver       | **jdbc:sybase:Tds:**                    |
| hostname:port/databaseName                   |                                 |                                         |



## 3\. 创建连接对象

### 1）使用数据库URL的用户名和密码：

getConnection() 最常用的形式是 getConnection(String url, String user, String
password)，要求传递数据库 URL，用户名 username和密码 password。

假设有一台主机TCP/IP地址 192.0.0.1 以及主机名和 Oracle 监听器被配置为在端口 1521，数据库名称是 EMP，然后完整的数据库
URL 是：


​    

```java
jdbc:oracle:thin:@192.0.0.1:1521:EMP
```


通过 URL、username 和 password 三个参数来获得一个 Connection 对象：


​    

```java
String URL = "jdbc:oracle:thin:@192.0.0.1:1521:EMP";
String USER = "username";
String PASS = "password"
Connection conn = DriverManager.getConnection(URL, USER, PASS);
```


### 2）只使用一个数据库 URL 的调用方式


​    

```java
DriverManager.getConnection(String url);
```


通过一个参数来获得一个 Connection 对象，在这种情况下，数据库的 URL 中包含用户名和密码：


​    

```java
jdbc:oracle:driver:username/password@database
```


所以上面的连接可以创建如下：


​    

```java
String URL = "jdbc:oracle:thin:username/password@192.0.0.1:1521:EMP";
Connection conn = DriverManager.getConnection(URL);
```


### 3）使用数据库 URL 和 Properties 对象的调用方式


​    

```java
DriverManager.getConnection(String url, Properties info);
```


Properties 对象用来保存一组键值对，调用 getConnection() 方法时，将键值对传递给驱动程序。


​    

```java
import java.util.*;
String URL = "jdbc:oracle:thin:@192.0.0.1:1521:EMP";
Properties info = new Properties( );
info.put( "user", "username" );
info.put( "password", "password" );

Connection conn = DriverManager.getConnection(URL, info);
```




## 4\. 关闭 JDBC 连接

在JDBC程序的结束，需要关闭所有的数据库连接，以结束数据库会话。但是，如果不关闭的话，Java
垃圾收集器会关闭连接，并清除旧对象。但依托垃圾收集，特别是在数据库编程，是非常差的编程习惯，应该显式地关闭数据库连接。为了确保连接被关闭，可以在代码中的
finally 块执行。

要关闭上面打开的连接，应该调用close()方法，如下所示：


​    

```java
conn.close();
```


显式地关闭连接，可以节约系统资源。



# JDBC 选择数据库范例

在本教程将演示如何在 JDBC 应用程序中选择一个数据库。在执行以下示例之前，请确保您已经准备好以下操作：

  * 具有数据库管理员权限，以在给定模式中创建数据库。要执行以下示例，需要用实际用户名和密码替换这里用户名(username)和密码(password)。
  * MySQL或数据库已启动并运行。



## 1\. 所需步骤

使用 JDBC 应用程序选择数据库需要以下步骤：

  * **导入包** ：需要包含包含数据库编程所需的JDBC类的包。大多数情况下，使用import java.sql.*就足够了。
  * **注册JDBC驱动程序** ：需要初始化驱动程序，以便可以程序中打开数据库的通信通道。
  * **打开连接** ：需要使用DriverManager.getConnection()方法来创建一个Connection对象，它表示与数据库服务器的物理连接。要创建一个新的数据库，不需要在准备数据库URL时提供任何数据库名称，如下面的示例所述。
  * **执行查询** ：需要使用类型为Statement的对象来构建和提交SQL语句到数据库。
  * **清理环境** ：需要明确地关闭所有数据库资源，而不依赖于 JVM 的垃圾收集。



## 2\. 选择数据库范例

复制以下示例代码保存到文件： _SelectDatabase.java_ 中，然后编译并运行如下 -


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class SelectDatabase {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
    static final String DB_URL = "jdbc:mysql://localhost/jdbc_db";

    //  Database credentials
    static final String USER = "root";
    static final String PASS = "123456";

    public static void main(String[] args) {
        Connection conn = null;
        try{
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to a selected database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected database successfully...");
        }catch(SQLException se){
            //Handle errors for JDBC
            se.printStackTrace();
        }catch(Exception e){
            //Handle errors for Class.forName
            e.printStackTrace();
        }finally{
            //finally block used to close resources
            try{
                if(conn!=null)
                conn.close();
            }catch(SQLException se){
                se.printStackTrace();
            }//end finally try
        }//end try
        System.out.println("Goodbye!");
    }//end main
}//end JDBCExample
```


编译上面代码，如下:


​    

```java
F:\worksp\jdbc> javac -Djava.ext.dirs=F:\worksp\jdbc\libs SelectDatabase.java
```


执行上面代码，如下:


​    

```java
F:\worksp\jdbc>java -Djava.ext.dirs=F:\worksp\jdbc\libs SelectDatabase
Connecting to a selected database...
Thu Jun 01 22:02:28 CST 2017 WARN: Establishing SSL connection without server's identity verification is not recommended. According to MySQL 5.5.45+, 5.6.26+ and 5.7.6+ requirements SSL connection must be established by default if explicit option isn't set. For compliance with existing applications not using SSL the verifyServerCertificate property is set to 'false'. You need either to explicitly disable SSL by setting useSSL=false, or set useSSL=true and provide truststore for server certificate verification.
Connected database successfully...
Goodbye!

F:\worksp\jdbc>
```


# JDBC CallableStatement 对象用来调用数据库存储过程。



## 1\. 存储过程范例


​    

```sql
DELIMITER $$

DROP PROCEDURE IF EXISTS `EMP`.`getEmpName` $$
CREATE PROCEDURE `EMP`.`getEmpName` 
   (IN EMP_ID INT, OUT EMP_FIRST VARCHAR(255))
BEGIN
   SELECT first INTO EMP_FIRST
   FROM Employees
   WHERE ID = EMP_ID;
END $$

DELIMITER ;
```



## 2\. CallableStatement 使用范例


​    

```java
//STEP 1. Import required packages
import java.sql.*;

public class JDBCExample {
   // JDBC driver name and database URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
   static final String DB_URL = "jdbc:mysql://localhost/EMP";

   //  Database credentials
   static final String USER = "username";
   static final String PASS = "password";
   
   public static void main(String[] args) {
   Connection conn = null;
   CallableStatement stmt = null;
   try{
      //STEP 2: Register JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      //STEP 3: Open a connection
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL,USER,PASS);

      //STEP 4: Execute a query
      System.out.println("Creating statement...");
      String sql = "{call getEmpName (?, ?)}";
      stmt = conn.prepareCall(sql);
      
      //Bind IN parameter first, then bind OUT parameter
      int empID = 102;
      stmt.setInt(1, empID); // This would set ID as 102
      // Because second parameter is OUT so register it
      stmt.registerOutParameter(2, java.sql.Types.VARCHAR);
      
      //Use execute method to run stored procedure.
      System.out.println("Executing stored procedure..." );
      stmt.execute();

      //Retrieve employee name with getXXX method
      String empName = stmt.getString(2);
      System.out.println("Emp Name with ID:" + 
               empID + " is " + empName);
      stmt.close();
      conn.close();
   }catch(SQLException se){
      //Handle errors for JDBC
      se.printStackTrace();
   }catch(Exception e){
      //Handle errors for Class.forName
      e.printStackTrace();
   }finally{
      //finally block used to close resources
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){
      }// nothing we can do
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }//end finally try
   }//end try
   System.out.println("Goodbye!");
}//end main
}//end JDBCExample
```



## 3\. 编译运行

现在来编译上面的例子：


​    

```java
C:>javac JDBCExample.java
C:>
```

当运行JDBCExample，它会产生以下结果：


​    

```java
C:>java JDBCExample
Connecting to database...
Creating statement...
Executing stored procedure...
Emp Name with ID:102 is Zaid
Goodbye!
C:>
```

