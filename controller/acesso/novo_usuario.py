import datetime
import smtplib
import uuid
from locale import str

from flask import jsonify, make_response, request, url_for
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from business.cadastro_business import CadastroBusiness
from dao.persiste_curso import insere_curso
from dao.persiste_usuario import insere_usuario
from dao.sql_alchemy import db
from model.curso import Curso
from model.usuario import Usuario


class NovoUsuario(Resource):
    """
    Classe que contém o endpoint de Cadastro.
    URI:5000/api/acesso/novoUsuario
    """

    def post(self):

        # try:

        payload = request.get_json()

        pswd_cript = generate_password_hash(
            payload['usuario']['password'], method='sha256')

        data = CadastroBusiness.valida_body_request(request)

        if type(data) != str:

            # new_user = insere_usuario(payload, pswd_cript, insere_curso(payload))

            # send_email_confirmation(new_user.email, new_user.usuario_public_id)

            if 'curso' in payload['usuario']:
                new_course = Curso(
                    curso_public_id=str(uuid.uuid4()),
                    nome=payload['usuario']['curso']['nome'],
                    turno=payload['usuario']['curso']['turno']
                )

            if 'usuario' in payload:
                new_user = Usuario(
                    id=str(uuid.uuid4()),
                    usuario_public_id=str(uuid.uuid4()),
                    email=payload['usuario']['email'],
                    nome=payload['usuario']['nome'],
                    nascimento=payload['usuario']['nascimento'],
                    username=payload['usuario']['username'],
                    password=pswd_cript,
                    active=False,
                    curso_public_id=new_course.curso_public_id,
                    confirmation_datetime=datetime.datetime.now()
                )

            db.session.add(new_user)
            db.session.add(new_course)
            db.session.commit()
            db.session.flush()

            EMAIL_ADDRESS = 'spotted.automaticmail@gmail.com'
            EMAIL_PASSWORD = 'Ab102030#'

            with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:

                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                subject = f'Confirmação de Cadastro - Spotted'
                body = 'Para finalizar o processo de criação de conta no Spotted, acesse o link:\nhttp://localhost:5000/api/confirm_login/'

                msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(new_user.email, EMAIL_ADDRESS, msg)

            # send_email_confirmation(email_target=new_user.email, target_public_id=new_user.usuario_public_id)

            return make_response(jsonify(dict(
                message='Usuario criado com sucesso. Um email para confirmação de criação de conta foi enviado para o seu email.',
                usuario=dict(username=payload['usuario']['username'],
                             email=payload['usuario']['email'],
                             nome=payload['usuario']['nome'],
                             nascimento=payload['usuario']['nascimento'],
                             curso=dict(
                    nome=payload['usuario']['curso']['nome'],
                    turno=payload['usuario']['curso']['turno']
                ))
            )), 201)

        return make_response(jsonify(dict(
            message=f'{data}'
        )), 422)
        # except Exception as e:
        #     return make_response(jsonify(
        #         dict(
        #             message='Ocorreu um erro interno',
        #             Exception=e,
        #         )
        #     ), 500)
