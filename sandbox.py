# coding=utf-8
from builtins import dict, str
import pprint


class Curso:

    def __init__(self, nome, turno):
        self.nome = nome
        self.turno = turno

    def get_json(self):
        return dict(
            nome=self.nome,
            turno=self.turno
        )


class Usuario:

    def __init__(self, username, email, nome):
        self.username = username
        self.email = email
        self.nome = nome

    def get_json(self):
        return dict(username=self.username,
                    email=self.email,
                    nome=self.nome)

    def valida_usuario(dict_obj):
        if 'username' in dict_obj:
            pass
        if 'email' in dict_obj:
            pass
        if 'nome' in dict_obj:
            pass


class Main:
    user = Usuario('baelfire', 'pikdasgalaxiass@gmail.com', 'Bruno')
    curso = Curso('ADS', 'Sei la')

    data = dict(usuario=user.get_json(),
                curso=curso.get_json(),
                teste=dict(var=15, var2=222))

    print('\n')

    for obj in data.values():
        print(obj)
        if 'username' in obj:
            Usuario.valida_usuario(obj)


if __name__ == '__main__':
    Main()
