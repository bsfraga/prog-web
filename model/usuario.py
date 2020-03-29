from dao.sql_alchemy import db
from model.pessoa import Pessoa

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_public_id = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.Integer, nullable=False, unique=True)
    username = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    # relação de um para um
    pessoa_public_id = db.relationship(Pessoa, lazy=True, backref='usuario', uselist=False)



