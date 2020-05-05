from dao.sql_alchemy import db
from model.user import User


class SocialNetwork(db.Model):

    __tablename__ = 'social'

    id = db.Column(db.Integer(primary_key=True, nullable=False, unique=True))
    pessoa_public_id = db.relationship(User, lazy=True, backref='social', uselist=False)
    facebook = db.Column(db.String(120), nullable=True)
    instagram = db.Column(db.String(120), nullable=True)
    twitter = db.Column(db.String(120), nullable=True)
