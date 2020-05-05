import datetime

from dao.sql_alchemy import db
from model.user import User
from model.commentary import Commentary

class Post(db.Model):
    
    __tablename__ = 'post'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    post_public_id = db.Column(db.String(120), nullable=False, unique=True)
    content = db.Column(db.Text(150), nullable=False)
    anonymous_post = db.Column(db.Boolean, nullable=False)
    deleted_post = db.Column(db.Boolean, nullable=False)
    post_datetime = datetime.datetime.now()
    
    user_public_id = db.Column(db.String(80), db.ForeignKey('user.user_public_id'), nullable=False)
    commentary_public_id = db.relationship(Commentary, backref='post', lazy=True)