from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_required
from flask_restful import Resource

from model.course import Course
from model.user import User


class ListUser(Resource):
    @jwt_required
    def get(self, user_public_id):

        try:

            user = User.query.filter_by(user_public_id=user_public_id).first()

            course = Course.query.filter_by(user_public_id=user_public_id).first()

            return make_response(jsonify(
                dict(
                    user_public_id=user.user_public_id,
                    email=user.email,
                    name=user.name,
                    birthday=user.birthday,
                    username=user.username,
                    course=dict(
                        course_public_id=course.course_public_id,
                        course_name=course.name,
                        course_shift=course.shift
                    )
                )
            ), 200)

        except Exception as e:
            return make_response(jsonify(
                dict(
                    message='Ocorreu um erro interno ao lista o usuário.',
                    Exception=f'{e}'
                )
            ), 500)
