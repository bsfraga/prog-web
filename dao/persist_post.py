import datetime
import uuid

from model.post import Post
from model.user import User
from flask import make_response, jsonify
from dao.sql_alchemy import db
import logging

def get_post(post_public_id):
    post = Post.query.filter_by(post_public_id=post_public_id).first()

    if not post:
        return False

    return post

def get_post_by_content(string, user_public_id, post_public_id):
    '''
        TODO

        query que verifica se contém o texto informado
        validar parametros recebidos no método

    '''
    try:
        pass
    except Exception:
        pass


def get_posts(self):
    try:
        
        posts = Post.query.all()

        if not posts:
            return False

        return posts


    except Exception:
        logging.exception('Não foi possível obter listagem de posts.')


def insert_post(payload, user_public_id):
    try:

        post = Post(
            post_public_id=uuid.uuid4().__str__(),
            content=payload['content'],
            anonymous_post=payload['anonymous_post'],
            deleted_post=False,
            post_datetime=datetime.datetime.now(),
            user_public_id=user_public_id
        )
        
        db.session.add(post)
        db.session.commit()
        db.session.flush()

    except Exception:
        logging.exception('Algo deu errado ao persistir post.')


def edit_post(payload, post_public_id, user_public_id):

    try:
        
        post = Post.query.filter_by(post_public_id=post_public_id).first()

        if post.user_public_id != user_public_id:
            return False

        post.content=payload['content']
        post.anonymous_post=payload['anonymous_post']            
        db.session.commit()
        db.session.flush()
        return True


    except Exception:
        logging.exception(f'Ocorreu um erro ao editar o post {post_public_id}')


def remove_post(post_public_id, user_public_id):

    try:
        
        post = Post.query.filter_by(post_public_id=post_public_id).first()

        if not post:
            return False

        post.removed_post = True
        db.session.commit()
        db.session.flush()
        return True


    except Exception:
        logging.exception(f'Erro ao remover post {post_public_id}')