
from werkzeug.utils import secure_filename
import uuid
import os
import time

from flask import Blueprint, session, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash,generate_password_hash

from functools import wraps
from flask import session, url_for, redirect
from ..models import db
from werkzeug.security import check_password_hash








# # 实例SQLAlchemy类，use_native_unicode='utf8'设置编码，必须设置



# 表——实体类

bg_blue = Blueprint("bg_app",__name__,url_prefix="/bg",template_folder="templates",static_folder="static")
# Blueprint两个参数（'蓝图名字',蓝图所在位置',url前缀)，注意：url前缀对该蓝图下所有route都起作用











class User(db.Model):
    # 设置表名
    __bind_key__ = 'db_mysql'
    __tablename__ = 'tb_user'
    # id，主键并自动递增
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256), nullable=True)
    name = db.Column(db.String(64))

    # 设置只可写入，对密码进行加密
    def password_hash(self, password):
        self.password = generate_password_hash(password)

class Blog(db.Model):
    __bind_key__ = 'db_mysql'
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    text = db.Column(db.TEXT)
    create_time = db.Column(db.String(64))
    #关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    user = db.relationship('User', backref='user')

class Comment(db.Model):
    __bind_key__ = 'db_mysql'
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(256))    # 评论内容
    create_time = db.Column(db.String(64))
    # 关联博客id
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    # 关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey("tb_user.id"))
    blog = db.relationship("Blog", backref="blog")
    user = db.relationship("User", backref="use")

# 创建
def creat():
    db.create_all()

# 删除
def drop():
    db.drop_all()








# 登录限制的装饰器 用于某些只让登录用户查看的网
# func是使用该修饰符的地方是视图函数页
def login_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 我们这里用来区分是否登录的方法很简答，就是查看session中是否赋值了username，如果赋值了，说明已经登录了
        if session.get('username'):
            # 如果登录了，我们就正常的访问函数的功能
            return func(*args, **kwargs)
        else:
            # 如果没登录，我们就将它重定向到登录页面，这里大家也可以写一个权限错误的提示页面进行跳转
            return redirect(url_for('/login'))
    return wrapper




# 上下文处理器，定义用户当前是否登录状态，全局可访问
@bg_blue.context_processor
def login_statue():
    # 获取session中的username
    username = session.get('username')
    # 如果username不为空，则已登录，否则没有登录
    if username:
        try:
            # 登录后，查询用户信息并返回用户信息
            user = User.query.filter(User.username == username).first()
            if user:
                return {"username": username, 'name': user.name, 'password': user.password}
        except Exception as e:
            return e
    # 如果没有登录，返回空
    return {}


# 404页面
@bg_blue.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500页面
@bg_blue.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500








# 写博客页面
@bg_blue.route('/writeBlog', methods=['POST', 'GET'])
@login_limit
def writeblog():
    if request.method == 'GET':
        return render_template('writeBlog.html')
    if request.method == 'POST':
        title = request.form.get("title")
        text = request.form.get("text")
        username = session.get('username')
        # 获取当前系统时间
        create_time = time.strftime("%Y-%m-%d %H:%M:%S")
        user = User.query.filter(User.username == username).first()
        blog = Blog(title=title, text=text, create_time=create_time, user_id=user.id)
        db.session.add(blog)
        db.session.commit()
        blog = Blog.query.filter(Blog.create_time == create_time).first()
        return render_template('blogSuccess.html', title=title, id=blog.id)

# 上传图片
@bg_blue.route('/imgUpload', methods=['POST', 'GET'])
@login_limit
def imgUpload():
    try:
        file = request.files.get('editormd-image-file')
        fname = secure_filename(file.filename)
        ext = fname.rsplit('.')[-1]
        # 生成一个uuid作为文件名
        fileName = str(uuid.uuid4()) + "." + ext
        filePath = os.path.join("static/uploadImg/", fileName)
        file.save(filePath)
        return {
            'success': 1,
            'message': '上传成功!',
            'url': "/" + filePath
        }
    except Exception:
        return {
            'success': 0,
            'message': '上传失败'
        }

# 博客详情页面
@bg_blue.route('/showBlog/<id>')
def showBlog(id):
    blog = Blog.query.filter(Blog.id == id).first()
    comment = Comment.query.filter(Comment.blog_id == blog.id)
    return render_template("showBlog.html", blog=blog, comment=comment)




# 博客详情页面
@bg_blue.route('/showBlogN/1')
def showBlogN(id):
    # blog = Blog.query.filter(Blog.id == id).first()
    # comment = Comment.query.filter(Comment.blog_id == blog.id)
    return render_template("showBlogN.html")


# 博客详情页面
@bg_blue.route('/showBlogN/')
def OneBolg():
    # blog = Blog.query.filter(Blog.id == id).first()
    # comment = Comment.query.filter(Comment.blog_id == blog.id)
    return render_template("test_gitbook.html")


# 展示全部博客
@bg_blue.route("/blogAll")
def blogAllBlog():
    # order_by按照时间倒序
    blogList = Blog.query.order_by(Blog.create_time.desc()).all()
    return render_template('blogAll.html', blogList=blogList)


# 修改密码
@bg_blue.route("/updatePwd", methods=['POST', 'GET'])
@login_limit
def update_passwod():
    if request.method == "GET":
        return render_template("updatePwd.html")
    if request.method == 'POST':
        lodPwd = request.form.get("lodPwd")
        newPwd1 = request.form.get("newPwd1")
        newPwd2 = request.form.get("newPwd2")
        username = session.get("username")
        user = User.query.filter(User.username == username).first()
        if check_password_hash(user.password, lodPwd):
            if newPwd1 != newPwd2:
                flash("两次新密码不一致！")
                return render_template("updatePwd.html")
            else:
                user.password_hash(newPwd2)
                db.session.commit()
                flash("修改成功！")
                return render_template("updatePwd.html")
        else:
            flash("原密码错误！")
            return render_template("updatePwd.html")


# 博客修改
@bg_blue.route("/update/<id>", methods=['POST', 'GET'])
@login_limit
def update_bg(id):
    if request.method == 'GET':
        blog = Blog.query.filter(Blog.id == id).first()
        return render_template('updateBlog.html', blog=blog)
    if request.method == 'POST':
        id = request.form.get("id")
        title = request.form.get("title")
        text = request.form.get("text")
        blog = Blog.query.filter(Blog.id == id).first()
        blog.title = title
        blog.text = text
        db.session.commit()
        return render_template('blogSuccess.html', title=title, id=id)

# 删除博客
@bg_blue.route("/delete/<id>", methods=['POST', 'GET'])
@login_limit
def delete_bg(id):


    blog = Blog.query.filter(Blog.id == id).first()
    db.session.delete(blog)
    db.session.commit()
    print(blog)
    return {
        'state': True,
        'msg': "删除成功！"
    }

# 查看个人博客
@bg_blue.route("/myBlog", methods=['POST', 'GET'])
@login_limit
def show_myBlog():
    username = session.get('username')
    user = User.query.filter(User.username == username).first()
    # order_by按照时间倒序
    blogList = Blog.query.filter(Blog.user_id == user.id).order_by(Blog.create_time.desc()).all()
    return render_template("myBlog.html", blogList=blogList)

# 评论
@bg_blue.route("/comment", methods=['POST', 'GET'])
@login_limit
def Onecomment():
    text = request.values.get('text')
    blogId = request.values.get('blogId')
    username = session.get('username')
    # 获取当前系统时间
    create_time = time.strftime("%Y-%m-%d %H:%M:%S")
    user = User.query.filter(User.username == username).first()
    print(text,blogId,username,create_time,user)
    comment = Comment(text=text, create_time=create_time, blog_id=blogId, user_id=user.id)
    db.session.add(comment)
    db.session.commit()
    return {
        'success': True,
        'message': '评论成功！',
    }

# 用户所有的评论
@bg_blue.route('/myComment')
@login_limit
def showAllComment():
    username = session.get('username')
    user = User.query.filter(User.username == username).first()
    # order_by按照时间倒序
    commentList = Comment.query.filter(Comment.user_id == user.id).order_by(Comment.create_time.desc()).all()
    return render_template("myComment.html", commentList=commentList)

# 删除评论
@bg_blue.route('/deleteCom/<id>', methods=['POST', 'GET'])
def deleteCom(id):
    com = Comment.query.filter(Comment.id == id).first()
    db.session.delete(com)
    db.session.commit()
    return {
        'state': True,
        'msg': "删除成功！"
    }









# 首页
@bg_blue.route('/')
def hello():
    return render_template('bgindex.html')

# 注册请求
@bg_blue.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user is not None:
            flash("该用户名已存在")
            return render_template('register.html')
        else:
            user = User(username=username, name=name)
            # 调用password_hash对密码加密
            user.password_hash(password)
            db.session.add(user)
            db.session.commit()
            flash("注册成功！")
            return render_template('register.html')

# 登录请求
@bg_blue.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        # check_password_hash比较两个密码是否相同
        if (user is not None) and (check_password_hash(user.password, password)):
            session['username'] = user.username
            session.permanent = True
            return redirect(url_for('bg_app.hello'))
        else:
            flash("账号或密码错误")
            return render_template('login.html')



# 关于页面
@bg_blue.route('/about')
def about():
    return render_template('about.html')

# 退出
@bg_blue.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('bg_app.hello'))






