# -*- coding: utf-8 -*-


import os
import sys

from msg import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')




# 同时连接两种数据库，sqlite处理留言，mysql处理博客

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
# 上面是sqlite配置，下面是mysql的配置


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_BINDS'] = {
    'db_sqlite': app.config['SQLALCHEMY_DATABASE_URI'],
    'db_mysql': 'mysql+pymysql://root:123456@localhost:3306/flaskblog'
}





SQLALCHEMY_ECHO = True

# 上传图片配置
MAX_CONTENT_LENGTH = 1 * 1024 * 1024
#$ flask forge
#$ flask run
