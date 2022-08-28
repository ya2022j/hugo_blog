# -*- coding: utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class MsgForm(FlaskForm):
    name = StringField('名前', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('メッセージ', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
