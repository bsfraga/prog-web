import datetime

import jwt
from flask import request, jsonify, make_response
from flask_restful import Resource
from werkzeug.security import check_password_hash

from model.usuario import Usuario


class Login(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response(jsonify(dict(
                mensagem="Parâmetros de login inválidos. Revise as informações."
            )), 401)

        usuario = Usuario.query.filter_by(email=auth.username).first()

        if not usuario:
            return make_response(jsonify(dict(
                mensagem="Usuário não está contido na base de dados."
            )), 400)

        if check_password_hash(usuario.password, auth.password):
            token = jwt.encode(dict(identity=usuario.usuario_public_id,
                                    tempo=str(datetime.datetime.utcnow() + datetime.timedelta(60))),
                               key='DontTellAnyone')

            return make_response(jsonify(dict(
                mensagem="Usuário logado com sucesso.",
                token=token.decode('UTF-8'),
                usuario_public_id=usuario.usuario_public_id
            )), 200)

        if not check_password_hash(usuario.password, auth.password):
            return make_response(jsonify(
                {
                    'message':'Usuário ou senha inválidos.'
                }
            ), 422)

        return make_response(jsonify(dict(
            mensagem="Ocorreu um erro interno."
        )), 500)
