from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_required
from flask_restful import Resource

from model.curso import Curso
from model.usuario import Usuario


class ListaUsuario(Resource):
    @jwt_required
    def get(self, usuario_public_id):

        try:

            user = Usuario.query.filter_by(usuario_public_id=usuario_public_id).first()

            curso = Curso.query.filter_by(curso_public_id=user.curso_public_id).first()

            return make_response(jsonify(
                {
                    'usuario_public_id':user.usuario_public_id,
                    'email':user.email,
                    'nome':user.nome,
                    'nascimento':user.nascimento,
                    'username':user.username,
                    'curso':dict(
                        curso_public_id=curso.curso_public_id,
                        curso_nome=curso.nome,
                        curso_turno=curso.turno
                    )
                }
            ), 200)

        except Exception as e:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno ao lista o usuário.',
                    Exception=f'{e}'
                )
            ), 500)
