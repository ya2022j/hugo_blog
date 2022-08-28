# -*- coding: utf-8 -*-


from datetime import datetime
from werkzeug.security import generate_password_hash

from msg import db

from flask_sqlalchemy import SQLAlchemy





class Message(db.Model):
    __bind_key__ = 'db_sqlite'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)






