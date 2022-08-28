# -*- coding: utf-8 -*-


from flask import flash, redirect, url_for, render_template

from msg import app, db
from msg.forms import MsgForm
from msg.models import Message


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('お疲れ様です！')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages[:6])

@app.route('/baseindex', methods=['GET', 'POST'])
def baseindex():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('お疲れ様です！')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('baseindex.html', form=form, messages=messages[:6])


@app.route('/disclaimer', methods=['GET', 'POST'])
def Disclaimer():
    return render_template('disclaimer.html')








@app.route('/base_title_blog', methods=['GET', 'POST'])
def base_title_logo_msg_footer():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('お疲れ様です！')
        return redirect(url_for('base_title_blog'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('base_title_blog.html', form=form, messages=messages[:6])


@app.route('/onePageBlog', methods=['GET', 'POST'])
def onePageBlog():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('お疲れ様です！')
        return redirect(url_for('onePageBlog'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('onePageBlog.html', form=form, messages=messages[:6])



@app.route('/Ebooklist', methods=['GET', 'POST'])
def Ebooklist():
    return render_template('Ebooklist.html')

