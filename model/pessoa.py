from dao.sql_alchemy import db


class Pessoa(db.Model):
    """
    Objeto pessoa e seus atributos.

    """

    __tablename__ = 'pessoa'

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    person_public_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)

    user_public_id = db.Column(db.String(80), db.ForeignKey('usuario.user_public_id'), nullable=False)
