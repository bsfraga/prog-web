from model.commentary import Commentary
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import make_response, jsonify, request
from dao.persist_commentary import insert_commentary

class NewCommentary(Resource):

    @jwt_required
    def post(self, post_public_id):

        try:

            if not post_public_id:
                return make_response(jsonify(
                    dict(
                        message='É preciso informar o post_public_id na rota.'
                    )
                ), 422)

            user_public_id = get_jwt_identity()            

            if not user_public_id:
                return make_response(jsonify(
                    dict(
                        message='Não foi possivel obter o user_public_id.'
                    )
                ), 400)

            payload = request.get_json()

            if not payload['content'] or not payload['commentary_removed']:
                return make_response(jsonify(
                    dict(
                        message='Voce deve informar o content e cmomentary_removed. Verifique a documentação.'
                    )
                ), 422)

            if not insert_commentary(payload, user_public_id, post_public_id):
                return make_response(jsonify(
                    dict(
                        message='Não foi possivel adicionar o comentário ao post.'
                    )
                ), 400)

            return make_response(jsonify(
                dict(
                    message=f'Comentário inserido no post "{post_public_id}" com sucesso.'
                )
            ), 201)

        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)