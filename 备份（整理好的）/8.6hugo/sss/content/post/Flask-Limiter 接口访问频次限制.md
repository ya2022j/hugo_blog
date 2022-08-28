
+++
title = "Flask-Limiter 接口访问频次限制"
tags = [
"Python",
"Flask",
"Chinese",
]
date = "2022-07-28 23:20:28"
categories = [
"Chinese",
]
+++


# Flask-Limiter 接口访问频次限制

flask-limiter - 第三方控频插件
官方文档：[FlaskLIMITER](https://flask-limiter.readthedocs.io/en/stable/)
flask-limiter 是一个对客户端的访问速率进行限制的flask扩展.可以自定义一些访问的(速度)限制条件来把那些触发限制的请求拒之门外.一般常用来进行对爬虫的限制.
下面就常见的用法,举了一些例子.更多的例子,请自己查看原始文档.
## 实现方式

``` python

# -*- coding: utf-8 -*-
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    # 每天限制多少次，每小时限制多少次，没分钟限制多少次
    default_limits=["20 per day", "2 per hour", "1 per minute"],
    # 存储位置可以选择 redis 来存储
    storage_uri="redis://:123456@127.0.0.1:6379/0"
)

# 地址 slow 每分钟只能访问一次
@app.route("/slow")
@limiter.limit("1 per minute")
def slow():
    return "24"


# 地址 fast 走全局的配置 default_limits
@app.route("/fast")
def fast():
    return "42"

# 地址 ping 通过
@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
- 在使用 redis 作为存储位置的时候，我们需要值得注意的是，要想让limiter缓存在redis中必须安装相应的支持库，Flask-Limiter并不会自动安装，所以需要我们手动 pip install flask-redis 。