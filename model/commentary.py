from dao.sql_alchemy import db


class Commentary(db.Model):

    __tablename__ = 'commentary'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    commentary_public_id= db.Column(db.String(80), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    commentary_datetime = db.Column(db.DateTime, nullable=False)
    commentary_removed = db.Column(db.Boolean, nullable=False)
    
    post_public_id = db.Column(db.String(80), db.ForeignKey('post.post_public_id'))
    user_public_id = db.Column(db.String(80), db.ForeignKey('user.user_public_id'))