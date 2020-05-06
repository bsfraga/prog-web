
from flask import make_response, jsonify, request
from dao.persist_commentary import remove_commentary
from flask_jwt_extended import jwt_required, get_jwt_identity

class RemoveCommentary(Resource):

    @jwt_required
    def put(self, commentary_public_id):

        try:
            
            user_public_id = get_jwt_identity()

            payload = request.get_json()

            if not payload['commentary_removed']:
                return make_response(jsonify(
                    dict(
                        message='Você deve informar o parâmetro "commentary_removed". Verifique a documentação.'
                    )), 422)

            if not remove_commentary(commentary_public_id):
                return make_response(jsonify(
                    dict(
                        message=f'Não foi possível remover o comentário {commentary_public_id}'
                    )
                ))

            return make_response(jsonify(
                    dict(
                        message=f'Comentário {commentary_public_id} removido do post com sucesso.'
                    )
                ))

        except Exception:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
