from dao.sql_alchemy import db
from model.usuario import Usuario
import datetime


class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    usuario_public_id = db.relationship(Usuario, lazy=True, backred='log', uselist=False)
    data = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(8), nullable=False)
    pagina = db.Column(db.String(60), nullable=False)
    mensagem = db.Column(db.String(60), nullable=False)
    acao = db.Column(db.String(60), nullable=False)

    @classmethod
    def get_datetime(cls):
        data = datetime.date.isoformat
        hora = datetime.time.hour
        minuto = datetime.time.minute
        segundo = datetime.time.second

        horario = f'{hora}:{minuto}:{segundo}'

        return data, horario

    @classmethod
    def log_event(cls):
        """
        TODO: receber as mensagens da camada business
        TODO: RN [ método deve ser genérico para receber dados de todas as camadas ]
        TODO: criar classe de persistencia na camada dao para log
        TODO: adicionar chamada de persistencia do log junto com os endpoints
        :return:
        """
        pass
