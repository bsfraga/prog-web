from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.post import Post
from dao.persist_post import remove_post


class RemovePost(Resource):

    @jwt_required
    def put(self, post_public_id):
        try:

            user_public_id = get_jwt_identity()

            if not post_public_id:
                return make_response(jsonify(
                    dict(
                        message='Você deve informar o post_public_id.'
                    )
                ), 422)

            if not remove_post(post_public_id, user_public_id):
                return make_response(jsonify(
                    dict(
                        message=f'Não foi possivel remover o post {post_public_id}'
                    )
                ), 400)
                
            return make_response(jsonify(
                dict(
                    message=f'Post {post_public_id} removido com sucesso.'
                )), 401)
            

        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
