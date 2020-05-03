from dao.sql_alchemy import db


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.String(80), primary_key=True, nullable=False, unique=True)
    usuario_public_id = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    # relação de um para um
    curso_public_id = db.Column(db.String(80), db.ForeignKey('curso.curso_public_id'), nullable=False)

    @classmethod
    def get_json(cls):
        return dict(id=cls.id,
                    usuario_pulic_id=cls.usuario_public_id,
                    email=cls.email,
                    nome=cls.nome,
                    nascimento=cls.nascimento,
                    username=cls.username,
                    active=cls.active)
