from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_refresh_token_required

from dao.persist_post import insert_post

class CreatePost(Resouce):

    @jwt_refresh_token_required
    def post(self):
        try:
            
            payload = request.get_json()
            
            if not payload['content'] or not payload['anonymous_post'] or not payload['deleted_post']:
                return make_response(jsonify(
                    dict(
                        message='Corpo de requisição inválido, consulte a documentação.'
                    )
                ), 422)

            persist_result = insert_post(payload)

            if persist_result:
                return make_response(jsonify(
                    dict(
                        message='Post criado com sucesso.'
                    )
                ), 201)

        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
