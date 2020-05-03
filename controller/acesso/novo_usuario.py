from locale import str

from flask import jsonify, request, make_response
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from business.cadastro_business import CadastroBusiness
from dao.persiste_curso import insere_curso
from dao.persiste_usuario import insere_usuario


class NovoUsuario(Resource):
    """
    Classe que contém o endpoint de Cadastro.
    URI:5000/api/acesso/novoUsuario
    """

    def post(self):
        payload = request.get_json()

        pswd_cript = generate_password_hash(
            payload['usuario']['password'], method='sha256')

        data = CadastroBusiness.valida_body_request(request)
        if type(data) != str:
            insere_usuario(payload, pswd_cript, insere_curso(payload))

            return make_response(jsonify(dict(
                mensagem='Usuario criado com sucesso.',
                usuario=dict(username=payload['usuario']['username'],
                             email=payload['usuario']['email'],
                             nome=payload['usuario']['nome'],
                             nascimento=payload['usuario']['nascimento'],
                             curso=dict(
                                 nome=payload['usuario']['curso']['nome'],
                                 turno=payload['usuario']['curso']['turno']
                             ))
            )), 201)

        # TODO: validar status code correto para essa situação
        return make_response(jsonify(dict(
            mensagem=f'{data}'
        )), 401)
