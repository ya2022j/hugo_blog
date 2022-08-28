
from flask import Flask,render_template
app = Flask(__name__)#修改静态文件夹的目录


@app.route('/d')
def home():
    return render_template('t.html')#homepage.html在static文件夹下


if __name__ == "__main__":
    app.run(debug=True)