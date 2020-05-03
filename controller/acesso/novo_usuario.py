from locale import str

from flask import jsonify, make_response, request, url_for
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from business.cadastro_business import CadastroBusiness
from dao.persiste_curso import insere_curso
from dao.persiste_usuario import insere_usuario
from utils.send_email import send_email_confirmation

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

            new_user = insere_usuario(payload, pswd_cript, insere_curso(payload)

            send_email_confirmation(new_user.email, new_user.usuario_public_id)


            if new_user:
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
