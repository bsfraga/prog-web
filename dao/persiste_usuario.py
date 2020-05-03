import uuid
from model.usuario import Usuario
from dao.sql_alchemy import db


def insere_usuario(payload, pswd_cript, curso_public_id):
    try:
        payload = dict(payload)
        if 'usuario' in payload:
            novo_usuario = Usuario(
                id=str(uuid.uuid4()),
                usuario_public_id=str(uuid.uuid4()),
                email=payload['usuario']['email'],
                nome=payload['usuario']['nome'],
                nascimento=payload['usuario']['nascimento'],
                username=payload['usuario']['username'],
                password=pswd_cript,
                active=True,
                curso_public_id=curso_public_id
            )
            db.session.add(novo_usuario)
            db.session.commit()
            db.session.flush()
    except Exception as e:
        print(f'Erro ao inserir curso. \n{e}')
