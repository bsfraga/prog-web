from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_refresh_token_required


class EditPost(Resource):

    @jwt_refresh_token_required
    def put(self, post_public_id):
        try:
            pass
        except Exception:
            pass