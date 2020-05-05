import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource

from dao.persist_user import activate_account, get_user
from dao.sql_alchemy import db
from model.user import User


class ConfirmRegister(Resource):

    def put(self, user_public_id):

        try:

            if not user_public_id:
                return make_response(jsonify(
                    dict(
                        message='Não foi possível ativar a conta ou a conta já está ativa.'
                    )
                ), 422)

            user = get_user(user_public_id)

            if not user:
                return make_response(jsonify(
                    dict(
                        message='Link expirado ou inválido.'
                    )
                ), 400)

            persist_result = activate_account(user_public_id)

            if persist_result:

                return make_response(jsonify(
                    dict(
                        message='Conta ativada com sucesso.'
                    )
                ), 200)

            else:

                return make_response(jsonify(
                    dict(
                        message='A conta informada já está ativada.'
                    )
                ), 422)

        except Exception as e:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno.'
                )
            ), 500)
