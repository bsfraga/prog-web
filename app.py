import os

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from controller.acesso.confirm_register import ConfirmRegister
from controller.acesso.login import Login
from controller.acesso.logout import Logout
from controller.acesso.new_user import NewUser
from controller.post.create_post import CreatePost
from controller.post.edit_post import EditPost
from controller.post.remove_post import RemovePost
# from controller.usuario.altera_senha_usuario import AlteraSenhaUsuario
from controller.usuario.list_user import ListUser
from utils.blacklist import BLACKLIST

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
api = Api(app)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')


@app.before_first_request
def cria_banco():
    db.create_all()


app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True


@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST



@jwt.revoked_token_loader
def invalid_token():
    return make_response(jsonify(dict(
        message='Você não está logado.'
    )), 401)


# --------------------------Endpoints--------------------------#

# --------------------------Login/Logout-----------------------#
api.add_resource(Login, '/api/access/login')
api.add_resource(Logout, '/api/access/logout')
# --------------------------New Register------------------------#
api.add_resource(NewUser, '/api/access/register')
api.add_resource(ConfirmRegister, '/api/access/confirmRegister/<user_public_id>')
# --------------------------User Actions------------------------#
# api.add_resource(AlteraSenhaUsuario, '/api/perfil/alteraSenhaUsuario')
# api.add_resource(ListaUsuarios, '/api/perfil/listaUsuarios')
api.add_resource(ListUser, '/api/profile/<user_public_id>')
# api.add_resource(AlteraStatus, '/api/usuario/alteraStatus/<public_id>')
# -------------------------------------------------------------#
# api.add_resouce(ListaPosts, '/api/posts/)
api.add_resource(CreatePost, '/api/post/newPost')
api.add_resource(EditPost, '/api/post/editPost/<post_public_id>')
api.add_resource(RemovePost, '/api/post/removePost/<post_public_id>')

# ------------------------ EMAIL SETUP -----------------------#

'''
Set up flask to send json as they were developed
'''
app.config['JSON_SORT_KEYS'] = False


if __name__ == '__main__':
    from dao.sql_alchemy import db

    db.init_app(app)
    app.run(debug=True)
