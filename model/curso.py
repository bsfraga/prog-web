from dao.sql_alchemy import db

from model.usuario import Usuario


class Curso(db.Model):

    __tablename__ = 'curso'

    id = db.Column(db.String(80), primary_key=True, nullable=False, unique=True)
    curso_public_id = db.Column(db.String(80), nullable=False, unique=True)
    curso_usuario = db.relationship(Usuario, backref='curso', lazy=True, uselist=False)
    nome = db.Column(db.String(30), nullable=False)
    turno = db.Column(db.String(15), nullable=False)

    @classmethod
    def get_json(cls):
        return dict(id=cls.id,
                    curso_public_id=cls.curso_public_id,
                    nome=cls.nome,
                    turno=cls.turno)
