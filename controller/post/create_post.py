from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from dao.persist_post import insert_post

class CreatePost(Resource):

    @jwt_required
    def post(self):
        try:
            
            user_public_id = get_jwt_identity()

            if not user_public_id:
                return make_response(jsonify(
                    dict(
                        message="Não foi possivel obter o usuário de sessão."
                    )
                ), 500)

            payload = request.get_json()
            
            if not payload['content']:
                return make_response(jsonify(
                    dict(
                        message='Corpo de requisição inválido, consulte a documentação.'
                    )
                ), 422)

            persist_result = insert_post(payload, user_public_id)

            if type(persist_result) != bool:
                return make_response(jsonify(
                    dict(
                        message='Post criado com sucesso.'
                    )
                ), 201)

        except Exception as e:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.',
                    exception=f'{e}'
                )
            ), 500)
