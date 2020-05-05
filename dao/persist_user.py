import uuid
from model.user import User
from dao.sql_alchemy import db
import datetime
import logging


def get_user(user_public_id):
    try:

        user = User.query.filter_by(user_public_id=user_public_id).first()

        if not user:
            return False

        return user


    except Exception:
        logging.exception('Erro ao obter usuário pelo public_id.')



def get_user_by_username(username):
    try:

        user = User.query.filter_by(username=username).first()

        if not user:
            return False

        return user

    except Exception:
        logging.exception('Erro ao obter usuário pelo username.')

def insert_user(payload, pswd_cript, course_public_id):
    try:
        payload = dict(payload)
        if 'user' in payload:
            new_user = User(
                user_public_id=uuid.uuid4().__str__(),
                email=payload['user']['email'],
                name=payload['user']['name'],
                birthday=payload['user']['birthday'],
                username=payload['user']['username'],
                password=pswd_cript,
                active=False,
                course_public_id=course_public_id,
                registration_datetime=datetime.datetime.now(),
                confirm_register_datetime=""
            )
            db.session.add(new_user)
            db.session.commit()
            db.session.flush()
            return new_user.user_public_id
    except Exception:
        logging.exception(f'Erro ao inserir usuario no banco de dados.')


def user_change_password(user_public_id, cript_pwd):
    try:

        pass

    except Exception:
        logging.exception(
            f'Erro ao modificar senha de usuário no banco de dados.')


def activate_account(user_public_id):
    try:

        user = User.query.filter_by(user_public_id=user_public_id).first()

        if not user:
            return False

        user.active = True
        user.confirm_register_datetime = datetime.datetime.now()
        db.session.commit()
        db.session.flush()

        return True

    except Exception:
        logging.exception(f'Erro ao ativar conta.')
