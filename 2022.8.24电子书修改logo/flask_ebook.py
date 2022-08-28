# -*- coding: utf-8 -*-
import os
import sys


from flask_cors import cross_origin



from flask import flash, redirect, url_for, render_template
from flask import Flask, jsonify,request,make_response,render_template




app = Flask(__name__)
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/todos')
@cross_origin()
def get_list():
    data = [
        {"userId": 1,'id': 1, 'title': 's', 'completed': '2020-01-21 21:25:44'},
        {"userId": 1,'id': 2, 'title': 'as', 'completed': '2020-01-20 21:25:44'},
        {"userId": 1,'id': 3, 'title': 'asdf', 'completed': '2020-01-19 11:25:44'},
        {"userId": 1,'id': 4, 'title': 'asdf', 'completed': '2020-01-18 13:25:44'},
        {"userId": 1,'id': 5, 'title': 'asdf', 'completed': '2020-01-17 15:25:44'}
    ]

    response = make_response(jsonify(data))
    return response



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
# java基础
@app.route('/java1', methods=['GET', 'POST'])
def java1():
    return render_template('java1.html')
# java高级用法及JDBC操作
@app.route('/java2', methods=['GET', 'POST'])
def java2():
    return render_template('java2.html')



if __name__ =="__main__":
    app.run()