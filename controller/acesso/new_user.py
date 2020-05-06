import datetime
import smtplib
import uuid
from email.message import EmailMessage
from locale import str

from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from dao.persist_course import insert_course
from dao.persist_user import insert_user
from dao.sql_alchemy import db
from model.course import Course
from model.user import User


class NewUser(Resource):
    """
    Classe que contém o endpoint de Cadastro.
    URI:5000/api/acesso/novoUsuario
    """

    def post(self):

        try:

            payload = request.get_json()

            pswd_cript = generate_password_hash(
                payload['user']['password'], method='sha256')

            if 'course' in payload['user']:
                for item in payload['user']['course']:
                    if type(item) == dict:
                        if 'name' not in item and 'shift' not in item:
                            return make_response(jsonify(
                                dict(
                                    message='Dados informados não conferem com os dados de Curso. Visite a documentação.'
                                )), 422)
                                
            elif 'user' in payload:
                for item in payload['user']:
                    if type(item) == dict:
                        if 'username' not in item and 'email' not in item and 'password' not in item and 'name' not in item and 'birthday' not in item:
                            return make_response(jsonify(
                                dict(
                                    message='Dados informados não conferem com os dados de Usuário. Visite a documentação.'
                                )), 422)


            user_id = insert_user(payload, pswd_cript)
            course_user_id = insert_course(payload, user_id)

            if not course_user_id or not user_id:
                return make_response(jsonify(
                    dict(
                        message='Ocorreu um erro ao efetuar um novo cadastro no banco de dados.'
                    )
                ), 500)

            EMAIL_ADDRESS = 'spotted.automaticmail@gmail.com'
            EMAIL_PASSWORD = 'Ab102030#'
            LOGIN = 'spotted.automaticmail'

            msg = EmailMessage()
            msg['Subject'] = 'Confirmação de Cadastro - Spotted'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = payload['user']['email']
            msg.set_content(
                f'Para finalizar o processo de criação de conta no Spotted, acesse o link:\nhttp://localhost:5000/api/access/confirmRegister/{user_id}\n\nEste é um email automático. Não responda.')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

                smtp.login(LOGIN, EMAIL_PASSWORD)

                smtp.send_message(msg)

                return make_response(jsonify(dict(
                    message='Usuario criado com sucesso. Um email para confirmação de criação de conta foi enviado para o seu email.',
                    user=dict(username=payload['user']['username'],
                              email=payload['user']['email'],
                              name=payload['user']['name'],
                              birthday=payload['user']['birthday'],
                              course=dict(
                        name=payload['user']['course']['name'],
                        shift=payload['user']['course']['shift']
                    ))
                )), 201)

        except Exception as e:
             return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
