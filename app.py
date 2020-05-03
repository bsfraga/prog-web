import os

from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import JWTManager
from flask_restful import Api

from controller.acesso.login import Login
from controller.acesso.logout import Logout
from controller.acesso.novo_usuario import NovoUsuario
from controller.usuario.altera_senha_usuario import AlteraSenhaUsuario
from controller.usuario.lista_usuario import ListaUsuario
from utils.blacklist import BLACKLIST
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')


@app.before_first_request
def cria_banco():
    db.create_all()


app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

jwt = JWTManager(app)

@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST



@jwt.revoked_token_loader
def invalid_token():
    return make_response(jsonify(dict(
        mensagem='Você não está logado.'
    )), 401)


# --------------------------Endpoints--------------------------#
api = Api(app)
# --------------------------Login/Logout-----------------------#
api.add_resource(Login, '/api/acesso/login')
api.add_resource(Logout, '/api/acesso/logout')
# --------------------------New Register------------------------#
api.add_resource(NovoUsuario, '/api/acesso/register')
# --------------------------User Actions------------------------#
api.add_resource(AlteraSenhaUsuario, '/api/perfil/alteraSenhaUsuario')
# api.add_resource(ListaUsuarios, '/api/perfil/listaUsuarios')
api.add_resource(ListaUsuario, '/api/perfil/<usuario_public_id>')
# api.add_resource(AlteraStatus, '/api/usuario/alteraStatus/<public_id>')
# -------------------------------------------------------------#
# api.add_resouce(ListaPosts, '/api/posts/)

# ------------------------ EMAIL SETUP -----------------------#



if __name__ == '__main__':
    from dao.sql_alchemy import db

    db.init_app(app)
    app.run(debug=True)
