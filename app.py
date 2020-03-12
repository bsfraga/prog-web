from crud import Crud


def main():
    c = Crud()
    c.insert(nome='Bruno', idade=26)
    c.insert(nome='Suane', idade=21)
    c.insert(nome='Teste', idade=99)
    c.get_by_name('Bruno')
    c.get_by_name('Suane')
    c.get_all()
    c.delete('Teste')
    c.insert(nome='Teste', idade=99)
    c.put('Teste', 'Teste Nome Modificado', 30)
    c.get_all()


if __name__ == '__main__':
    main()

# TODO 1: Validar Inserir (unitario)
# TODO 2: Validar Listar (unitario)
# TODO 3: Validar Alterar (unitario)
# TODO 4: Validar Deletar (unitario)
