from dao.sql_alchemy import db
from model.usuario import Usuario


class RedesSociais(db.Model):

    __tablename__ = 'redes_sociais'

    id = db.Column(db.Integer(primary_key=True, nullable=False, unique=True))
    pessoa_public_id = db.relationship(Usuario, lazy=True, backref='redes_sociais', uselist=False)
    facebook = db.Column(db.String(120), nullable=True)
    instagram = db.Column(db.String(120), nullable=True)
    twitter = db.Column(db.String(120), nullable=True)
