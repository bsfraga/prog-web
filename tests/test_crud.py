from crud import Crud


class TestCrud:

    def test_insert(self):
        '''
        Valida se o método inserir está funcionando ao chamar o método e passar os valores corretos.
        '''

        c = Crud()

        msg_retorno = c.insert('Bruno', 29)
        assert 'Pessoa adicionada!' in msg_retorno

    def test_insert_without_values(self):
        '''
        Valida o método inserir ao passar valores vazios.
        '''

        c = Crud()

        msg_retorno = c.insert('', '')
        assert "Você deve informar o nome e a idade da pessoa para adicionar na lista." in msg_retorno

    def test_add_values_and_get_all(self):
        '''
        Valida o método  de listagem após adicionar registros
        '''

        c = Crud()

        assert 'Pessoa adicionada!' in c.insert('Bruno', 26)
        assert 'Pessoa adicionada!' in c.insert('Suane', 21)
        assert 'Pessoa adicionada!' in c.insert('Teste', 15)

        msg_retorno_consulta = c.get_all()
        assert 'Bruno' in msg_retorno_consulta and 'Suane' in msg_retorno_consulta and 'Teste' in msg_retorno_consulta

    def test_add_value_and_get_by_name(self):
        '''
        valida o método de listagem de um único registro após inserir.
        '''

        c = Crud()

        assert 'Pessoa adicionada!' in c.insert('Bruno', 26)
        msg_retorno = c.get_by_name('Bruno')
        assert 'Registro encontrado!' in msg_retorno and 'Nome: Bruno' in msg_retorno and 'Idade: 26' in msg_retorno

    def test_delete_value_and_get_all(self):
        '''
        Valida o método delete após inserir registros
        '''

        c = Crud()

        assert 'Pessoa adicionada!' in c.insert('Bruno', 26)
        assert 'Pessoa adicionada!' in c.insert('Suane', 21)
        assert 'Pessoa adicionada!' in c.insert('Teste', 30)
        assert 'Removido o \'Nome\' [Teste]' in c.delete('Teste')
        msg_retorno = c.get_all()
        assert 'Nome: Bruno' in msg_retorno and 'Nome: Suane' in msg_retorno
        assert 'Nome: Teste' not in msg_retorno

    def test_change_person_value_and_get_all(self):
        '''
        Valida o método put após inserir registros e modificá-los
        '''

        c = Crud()

        assert 'Pessoa adicionada!' in c.insert('Bruno', 26)
        assert 'Pessoa adicionada!' in c.insert('Suane', 21)
        assert 'Pessoa adicionada!' in c.insert('Teste', 60)
        msg_retorno_put = c.put('Teste', 'Testado', 500)
        assert 'Registro alterado com sucesso!' in msg_retorno_put
        msg_retorno_get_all = c.get_all()
        assert 'Nome: Bruno' and 'Idade: 26' in msg_retorno_get_all
        assert 'Nome: Suane' and 'Idade: 21' in msg_retorno_get_all
        assert 'Nome: Testado' and 'Idade: 500' in msg_retorno_get_all
