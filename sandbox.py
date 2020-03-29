# coding=utf-8
from builtins import dict, str
import pprint

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_json(self):
        return dict(nome=self.nome,
                    idade=self.idade)

class Usuario:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_json(self):
        return dict(username=self.username,
                    email=self.email)


class Main:

        p = Pessoa('Bruno', 26)
        user = Usuario('baelfire', 'pikdasgalaxiass@gmail.com')

        data = dict(pessoa=p.get_json(),
                    usuario=user.get_json())

        pprint.pprint(data, sort_dicts=False, indent=4)

        for obj in data:
            if 'pessoa' not in str(obj):
                print ('Obj pessoa não encontrado')
            elif 'usuario' not in str(obj):
                print('Obj usuario nao encontrado')
            else:
                print (f'{str(obj)} não é requisito da função')
if __name__ == '__main__':
    Main()