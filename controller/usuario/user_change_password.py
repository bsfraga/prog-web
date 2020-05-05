from flask import jsonify, make_response, request
from flask_jwt_extended import (get_jwt_identity, jwt_refresh_token_required,
                                jwt_required)
from flask_restful import Resource
from werkzeug.security import check_password_hash, generate_password_hash

from dao.persist_user import user_change_password
from model.user import User


class ChangeUserPassword(Resource):

    @jwt_refresh_token_required
    def put(self):
        try:

            user_public_id = get_jwt_identity()

            user = User.query.filter_by(
                user_public_id=user_public_id).first()

            payload = request.get_json()

            if not payload['actual_password'] or payload['new_password'] or payload['confirm_new_password']:
                return make_response(jsonify(
                    dict(
                        message='Você deve preencher os campos "actual_password", "new_password" e "confirm_new_password".'
                    )
                ), 400)

            if not payload['new_password'] == payload['confirm_new_password']:
                return make_response(jsonify(
                    dict(
                        message='Nova senha divergente de confirmação de nova senha.'
                    )
                ), 400)

            if check_password_hash(user.password, payload['actual_password']):
                pwd_cript = generate_password_hash(
                    payload['new_password'], method='sha256')
                user.password = payload['new_password']

                user_change_password(user.user_public_id, user.password)

                return make_response(jsonify(
                    dict(
                        message='Senha alterada com sucesso.'
                    )
                ), 200)

        except Exception:
            return make_response(jsonify(
                dict(
                    message=f'Alguma coisa ocorreu de errado com a requisição. Verifique os parâmetros.',
                )
            ), 500)
