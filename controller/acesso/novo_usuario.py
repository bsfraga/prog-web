import uuid
from functools import wraps
from locale import str

import jwt
from flask import jsonify, request, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from werkzeug.security import check_password_hash, generate_password_hash

from dao.sql_alchemy import db
from model.usuario import Usuario
from model.pessoa import Pessoa


class NovoUsuario(Resource):

    """
    Buildar molde de requisição para
    receber os parametros de todos os objetos
    """

    def post(self):
        payload = request.get_json()

        pswd_cript = generate_password_hash(
            payload['password'], method='sha256')

        novo_usuario = Usuario(
            user_public_id=str(uuid.uuid4()),
            username=payload['username'],
            email=payload['email'],
            password=pswd_cript,
            active=True,
        )


        db.session.add(novo_usuario)
        db.session.commit()

        return make_response(jsonify(dict(
            mensagem='Usuario criado com sucesso.',
            usuario=dict(
                # TODO: exibir dados de usuario + pessoa -> validar herança de pessoa+usuario + redes_sociais +
            )
        )), 201)
