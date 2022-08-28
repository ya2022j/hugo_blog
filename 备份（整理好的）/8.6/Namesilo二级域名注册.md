+++
title = "Namesilo二级域名注册"
tags = [
"Namesilo",
"Chinese",
]
date = "2022-08-05 11:20:50"
categories = [
"Chinese",
]
+++


# Namesilo二级域名注册（最新版）

  * 网上有很多关于[Namesilo域名注册教程](https://zhuanlan.zhihu.com/p/411287071)。大家都可以搜来测试使用一下。本文主要整理二级域名的注册和使用远离。

  * 为什么需要二级域名？ 随着网站业务模块的逐渐增加，业务的技术选项也会变多，不在是一种语言或者一种框架。这时就需要从入口处进行分流。网上也有很多使用docker结合nginx进行多个应用的部署。有兴趣的朋友可以去找找看。

以我的经验为例，注册号域名并绑定ip地址后。会出现

TYPE:A --->ip TYPE:CNAME-->域名(itbenkyou.com)
这时的www.itbenkyou.com就是绑定在上面ip的itbenkyou.com主域名下的第一个子域名。
为了区分业务类型有的网站创建二级域名都有业务的特点有关。比如

  * 主域名 itbenkyou.com
  * 博客应用 blog.itbenkyou.com
  * 电子书应用 ebook.itbenkyou.com
  * 云服务应用 cloud.itbenkyou.com ![img1](https://images2.imgbox.com/f3/a2/RWJZyamq_o.jpg)

然后各自的开发团队，再针对不同的应用方向使用自己选择的技术栈进行开发，最终汇聚到服务器处，使用nginx进行反向代理设置即可。
这样就做到了业务分离。所以开始起一个有通用性的域名还是非常关键的。
![img2](https://images2.imgbox.com/ab/5f/Uqac2xFb_o.jpg)

  * 等到Namesilo将绑定的子域名解析完毕之后，就可以拿到生产环境中进行使用了。


