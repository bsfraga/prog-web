from dao.sql_alchemy import db

from model.user import User


class Course(db.Model):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    course_public_id = db.Column(db.String(80), nullable=False, unique=True)
    name = db.Column(db.String(30), nullable=False)
    shift = db.Column(db.String(15), nullable=False)

    user_public_id = db.Column(db.String(80), db.ForeignKey('user.user_public_id'))