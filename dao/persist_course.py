import uuid

from dao.sql_alchemy import db
from model.course import Course
import logging

def insert_course(payload):
    try:
        payload = dict(payload)
        if 'course' in payload['user']:
            new_course = Course(
                course_public_id=uuid.uuid4().__str__(),
                name=payload['user']['course']['name'],
                shift=payload['user']['course']['shift']
            )
            db.session.add(new_course)
            db.session.commit()
            db.session.flush()

            return new_course.course_public_id

    except Exception as e:
        logging.exception('Erro ao inserir curso.')
