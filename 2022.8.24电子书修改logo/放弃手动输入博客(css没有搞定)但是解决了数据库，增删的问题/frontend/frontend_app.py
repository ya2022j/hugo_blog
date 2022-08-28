




from flask import Blueprint,render_template

frontend_blue = Blueprint("frontend",__name__,url_prefix="/frontend",template_folder="templates",static_folder="static")


@frontend_blue.route('/') #该路由链接变成 /admin/
def admin():
    return "frontend"




@frontend_blue.route('/index') #该路由链接变成 /admin/
def admin1():
    return render_template("frontend.html")