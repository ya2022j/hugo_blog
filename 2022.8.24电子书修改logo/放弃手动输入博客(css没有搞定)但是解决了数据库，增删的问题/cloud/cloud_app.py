
from flask import Blueprint,render_template



cloud_blue = Blueprint("cloud_app",__name__,url_prefix="/cloud",template_folder="templates",static_folder="static")
# Blueprint两个参数（'蓝图名字',蓝图所在位置',url前缀)，注意：url前缀对该蓝图下所有route都起作用

@cloud_blue.route('/') #该路由链接变成 /admin/
def admin():
    return "cloud"




@cloud_blue.route('/index') #该路由链接变成 /admin/
def admin1():
    return render_template("cloud.html")