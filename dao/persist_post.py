import datetime

from model.post import Post

def get_post(post_public_id):
    post = Post.query.filter_by(post_public_id=post_public_id).first()

    if not post:
        return False

    return post

def get_post_by_content(string):
    '''
        TODO
    '''
    pass


def insert_post(payload):
    pass
