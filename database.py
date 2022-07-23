from flask import current_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
app=current_app
data=SQLAlchemy(app)
data.init_app(app)

class User(data.Model,UserMixin):
    id=data.Column(data.Integer,primary_key=True,autoincrement=True)
    username=data.Column(data.String,nullable=False,unique=True)
    password=data.Column(data.String,nullable=False)
    trackers=data.relationship("tracker",cascade='all',backref="parent")

class tracker(data.Model):
    user_id=data.Column(data.Integer,data.ForeignKey('user.id'),nullable=False)
    tracker_id=data.Column(data.Integer,primary_key=True,autoincrement=True)
    name=data.Column(data.String(30),nullable=False)
    desc=data.Column(data.String)
    type=data.Column(data.String,nullable=False)
    settings=data.Column(data.String)
    logs=data.relationship("log",cascade='all', backref="parent")

class log(data.Model):
    tracker_id=data.Column(data.Integer,data.ForeignKey("tracker.tracker_id"),nullable=False)
    log_id=data.Column(data.Integer,primary_key=True,autoincrement=True)
    log_datetime=data.Column(data.DateTime,nullable=False)
    note=data.Column(data.String)
    log_value=data.Column(data.String,nullable=False)
