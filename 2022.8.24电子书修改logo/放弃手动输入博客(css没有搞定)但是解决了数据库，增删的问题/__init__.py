# -*- coding: utf-8 -*-



# 2022.7.22
# 1 使用蓝图实现了根据应用的路由管理 app.py文件中只进行蓝图注册
# 2 在各个应用下创建初始包文件，目前只有一个视图函数，在该视图函数中声明注册蓝图，再在app.py中引入并注册到app上面
# 3 在各个应用的蓝图注册时，应用的路由，静态文件设置的也就注册完毕。同时html文件 整个项目中要保持唯一性
# 这样就做到了根据应用分类，并区别管理业务代码（无非就是视图函数，数据库，静态文件）
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


from .frontend import frontend_app
from .cloud import cloud_app
from .backend import backend_app



app = Flask('msg')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.register_blueprint(backend_app.backend_blue)
app.register_blueprint(cloud_app.cloud_blue)
app.register_blueprint(frontend_app.frontend_blue)


# # 实例SQLAlchemy类，use_native_unicode='utf8'设置编码，必须设置
db = SQLAlchemy(app,use_native_unicode='utf8')
bootstrap = Bootstrap(app)
moment = Moment(app)



#  使用数据库的蓝图在这里注册
from .blog import blog_app
app.register_blueprint(blog_app.bg_blue)

from msg import views, commands