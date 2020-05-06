from dao.sql_alchemy import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_public_id = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    registration_datetime = db.Column(db.String(30), nullable=False)
    confirm_register_datetime = db.Column(db.String(30), nullable=False)
    
    course = db.relationship('Course', backref='user')
    commentary = db.relationship('Commentary', backref='user')
    post = db.relationship('Post', backref='post')