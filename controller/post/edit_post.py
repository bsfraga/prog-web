from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.persist_post import edit_post

class EditPost(Resource):

    @jwt_required
    def put(self, post_public_id):
        try:

            payload = request.get_json()

            user_public_id = get_jwt_identity()

            if not user_public_id:
                return make_response(jsonify(
                    dict(
                        message='Não foi possível obter o usuário de sessão.'
                    )
                ), 400)  # revizar http code

            if not post_public_id:
                return make_response(jsonify(
                    dict(
                        message='Você deve informar o post_public_id para editar um post.'
                    )
                ), 422)

            
            if not edit_post(payload, post_public_id, user_public_id):
                return make_response(jsonify(
                    dict(
                        message=f'Você não pode alterar o post {post_public_id}.'
                    )
                ), 401)

            return make_response(jsonify(
                    dict(
                        message=f'Post {post_public_id} alterado com sucesso.',
                        post_public_id=post_public_id
                    )
                ), 200)
            
        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
