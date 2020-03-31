import pprint
import uuid

from dao.sql_alchemy import db
from model.curso import Curso


def insere_curso(payload):
    try:
        payload = dict(payload)
        if 'curso' in payload['usuario']:
            novo_curso = Curso(
                id=str(uuid.uuid4()),
                curso_public_id=str(uuid.uuid4()),
                nome=payload['usuario']['curso']['nome'],
                turno=payload['usuario']['curso']['turno']
            )
            db.session.add(novo_curso)
            db.session.commit()
            db.session.flush()

            return novo_curso.curso_public_id

    except Exception as e:
        print(f'Erro ao inserir curso. \n{e}')
