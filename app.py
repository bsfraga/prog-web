from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from utils.blacklist import BLACKLIST

import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['JWT_SECRET_KEY'] = 'NinguemDeveSaberEssaKeyHehe'
app.config['JWT_BLACKLIST_ENABLED'] = True


@app.before_first_request
def cria_banco():
    db.create_all()


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_invalido():
    return jsonify(dict(
        mensagem='Você não está logado.'
    )), 401


# --------------------------Endpoints--------------------------#
api = Api(app)
# --------------------------Login/Logout-----------------------#
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
# --------------------------New Register------------------------#
api.add_resource(NovoUsuario, '/novoUsuario')
# --------------------------User Actions------------------------#
api.add_resource(AlteraUsuario, '/usuario/altera_usuario/<user_pulic_id>')
api.add_resource(ListaUsuarios, '/usuario/listaUsuarios')
api.add_resource(ListaUsuario, '/usuario/listaUsuario/<public_id>')
api.add_resource(AlteraStatus, '/usuario/alteraStatus/<public_id>')
# -------------------------------------------------------------#

if __name__ == '__main__':
    from dao.sql_alchemy import db

    db.init_app(app)
    app.run(debug=True)
