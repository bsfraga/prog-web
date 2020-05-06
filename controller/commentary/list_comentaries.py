
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from dao.persist_commentary import get_commentaries

class ListCommentaries(Resource):

    @jwt_required
    def get(self):

        try:

            commentaries = get_commentaries()

            if not commentaries:
                return make_response(jsonify(
                    dict(
                        message='Este post não possui comentários.'
                    )
                ), 400)

            return make_response(jsonify(
                dict(
                    message='Listagem de comentários obtida com sucesso!',
                    commentaries=commentaries.__str__()
                )
            ), 200)


        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
