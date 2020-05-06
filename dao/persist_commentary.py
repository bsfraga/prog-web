import datetime
import logging
import uuid

from dao.sql_alchemy import db
from model.commentary import Commentary


def insert_commentary(payload, user_public_id, post_public_id):
    try:

        commentary = Commentary(
            user_public_id=user_public_id,
            commentary_public_id=uuid.uuid4().__str__(),
            post_public_id=post_public_id,
            content=payload['content'],
            commentary_removed=False,
            commentary_datetime=datetime.datetime.now()
        )
        return True

    except Exception:
        logging.exception('Erro ao inserir comentário no banco de dados')
        return False


def get_commentaries(commentary_public_id):
    try:

        commentaries = Commentary.query.find_by(
            commentary_public_id=commentary_public_id).all()

        if not commentaries:
            return False

        return commentaries

    except Exception:
        logging.exception('Ocorreu um erro ao obter comentários')


def remove_commentary(user_public_id, commentary_public_id):
    try:

        commentary = Commentary.query.find_by(
            commentary_public_id=commentary_public_id).first()

        if not commentary:
            return False

        if commentary.user_public_id == user_public_id:
            commentary.commentary_removed = True
            db.session.commit()
            return True

    except Exception:
        logging.exception(
            'Ocorreu um erro ao mudar status de comentário para removido.')
        return False


def edit_commentary(payload, commentary_public_id):
    try:

        commentary = Commentary.query.find_by(
            commentary_public_id, commentary_public_id).first()

        if not commentary:
            return False

        commentary.content = payload['content']


    except Exception:
        logging.exception(f'Não foi possivel editar o comentário {commentary_public_id} no banco de dados.')
