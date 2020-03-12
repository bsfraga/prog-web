from crud import Crud


def main():
    c = Crud()
    print(c.insert(nome='Bruno', idade=26))
    print(c.insert(nome='Suane', idade=21))
    print(c.insert(nome='Teste', idade=99))
    print(c.get_by_name('Bruno'))
    print(c.get_by_name('Suane'))
    print(c.get_all())
    print(c.delete('Teste'))
    print(c.insert(nome='Teste', idade=99))
    print(c.put('Teste', 'Teste Nome Modificado', 30))
    print(c.get_all())


if __name__ == '__main__':
    main()