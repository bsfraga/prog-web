from flask import jsonify, make_response
from flask_jwt_extended import get_raw_jwt, jwt_required
from flask_restful import Resource

from utils.blacklist import BLACKLIST


class Logout(Resource):
    @jwt_required
    def post(cls):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return make_response(jsonify(
            dict(
                message='Usuário desconectado com sucesso.'
            )), 200)
