from flask import make_response, jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.persist_post import get_posts
from model.post import Post

class ListPosts(Resource):

    @jwt_required
    def get(self):

        try:
            
            posts = get_posts()

            if not posts:
                return make_response(jsonify(
                    dict(
                        message='Não foi possivel obter a listagem de posts.'
                    )
                ), 400)

            return make_response(jsonify(
                dict(
                    message='Listagem de posts obtida com sucesso.',
                    posts=posts.__str__()
                )
            ), 200)

        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)