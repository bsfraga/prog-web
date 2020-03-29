from model.pessoa import Pessoa

class Crud:
    '''
    Classe que gerencia os dados da aplicação.
    - Adiciona
    - Altera
    - Consulta
    - Remove
    '''

    def __init__(self):
        '''
        Construtor da classe Crud. Quando instânciado, cria uma nova instância de Pessoa.
        '''
        self.p = Pessoa()

    def insert(self, nome, idade):
        '''
        Este método tem como finalidade, adicionar na lista contida dentro do Objeto Pessoa nomes e idades.
        '''
        if not nome and not idade:
            return f'Você deve informar o nome e a idade da pessoa para adicionar na lista.'

        self.p.add_pessoa_list(nome, idade)
        return f'Pessoa adicionada!\nNome: {self.p.nome}\t\tIdade: {self.p.idade}.\n'

    def get_by_name(self, nome):
        '''
        Este método tem como finalidade procurar dentro da lista contida no Objeto Pessoa
        as ocorrencias de um determinado nome e retorna os valores caso encontre.
        '''
        print(f'Procurando em memória o registro pelo \'Nome\' [{nome}]...\n')
        if not nome:
            return 'Você deve informar um nome.'

        for pessoa in self.p.list_pessoas:
            if pessoa['nome'] == nome:
                return f'Registro encontrado!\nNome: {pessoa["nome"]}\t\tIdade: {pessoa["idade"]}.'
            else:
                return 'O nome informado não consta no registro.'

    def get_all(self):
        '''
        Este método tem como finalidade listar todos os registros salvos dentro da lista contida no Objeto Pessoa.
        '''
        print(f'Pessoas registradas em memória:\n')
        content = ''
        for pessoa in self.p.list_pessoas:
            content += f'\t\tNome: {pessoa["nome"]}\t\tIdade: {pessoa["idade"]}\n'

        return content

    def delete(self, nome):
        '''
        Este método tem como finalidade remover a ocorrencia recebida por parâmetro.
        Utiliza como chave de busca para remoção o Nome.
        '''
        if not nome:
            return f'Você deve informar um nome para remover da lista de pessoas.'

        for pessoa in self.p.list_pessoas:

            if pessoa['nome'] == nome:
                list_size_before = len(self.p.list_pessoas)
                self.p.list_pessoas.remove(pessoa)

                if len(self.p.list_pessoas) < list_size_before:
                    return f'Removido o \'Nome\' [{nome}] da lista de pessoas com sucesso.'
                else:
                    return f'Não foi possível remover o \'Nome\' [{nome}] da lista de pessoas.'

    def put(self, nome, novo_nome, nova_idade):
        '''
        Este método tem como finalidade alterar um registro contido na lista contida no Objeto Pessoa.
        Utilizada como chave o Nome e recebe os novos valores de nome e idade.
        É obrigatório passar um valor de nome, para buscas. Um valor de novo_nome para alterar o nome
        buscado e um valor nova_idade para alterar a idade da pessoa buscada.
        '''
        if not nome:
            return f'Você deve informar o \'Nome\' para que seja efetuado a alteração da Pessoa.'
        if not novo_nome:
            return f'Você deve informar um \'Novo Nome\' para que o nome seja modificado.'
        if not nova_idade:
            return f'Você deve informar uma \'Nova Idade\' para que a idade seja modificada.'

        for pessoa in self.p.list_pessoas:
            if pessoa['nome'] == nome:
                print(f'Registro encontrado...\n\t\tNome: {pessoa["nome"]}\t\tIdade: {pessoa["idade"]}')
                pessoa['nome'] = novo_nome
                pessoa['idade'] = nova_idade
                return f'\nRegistro alterado com sucesso!\n\t\tNome: {pessoa["nome"]}\t\tIdade: {pessoa["idade"]}'
