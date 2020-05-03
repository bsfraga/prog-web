from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash


class AlteraSenhaUsuario(Resource):
    @jwt_required
    def put(self):
        try:

            usuario_public_id = get_jwt_identity()

            usuario_atual = Usuario.query.filter_by(
                usuario_public_id=usuario_public_id).first()

            payload = request.get_json()

            old_pwd = payload['actual_password']
            new_pwd = payload['new_password']
            confirm_new_pwd = payload['confirm_new_password']

            if not old_pwd or new_pwd or confirm_new_pwd:
                return make_response(jsonify(
                    {
                        'message': 'Você deve preencher os campos "actual_password", "new_password" e "confirm_new_password".'
                    }
                ), 400)

            if not new_pwd == confirm_new_pwd:
                return make_response(jsonify(
                    {
                        'message':
                        'Nova senha divergente de confirmação de nova senha.'
                    }
                ), 400)

            if check_password_hash(usuario_atual.password, old_pwd):
                pwd_cript = generate_password_hash(new_pwd, method='sha256')
                usuario_atual.password = new_pwd
                return make_response(jsonify(
                    {
                        'message': 'Senha alterada com sucesso.'
                    }
                ), 200)

        except Exception as e:
            return make_response(jsonify(
                {
                    'message': f'Alguma coisa ocorreu de errado com a requisição. Verifique os parâmetros.',
                    'Exception': f'{e}',
                }
            ), 500)
