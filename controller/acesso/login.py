import datetime

from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from werkzeug.security import check_password_hash

from model.user import User


class Login(Resource):
    def post(self):

        rq_body = request.get_json()

        if not rq_body or not rq_body['username'] or not rq_body['password']:
            return make_response(jsonify(dict(
                message="Parâmetros de login inválidos. Revise as informações."
            )), 401)

        user = User.query.filter_by(username=rq_body['username']).first()

        if not user:
            return make_response(jsonify(dict(
                message="Usuário não está contido na base de dados."
            )), 400)

        if check_password_hash(user.password, rq_body['password']):
            token = create_access_token(
                identity=user.user_public_id, expires_delta=datetime.timedelta(900))
            return make_response(jsonify(dict(
                message="Usuário logado com sucesso.",
                token=token.__str__()
            )), 200)

        if not check_password_hash(user.password, rq_body['password']):
            return make_response(jsonify(
                dict(
                    message='Usuário ou senha inválidos.'
                
            )), 422)

        return make_response(jsonify(dict(
            message="Ocorreu um erro interno."
        )), 500)
