class Pessoa:
    '''
    Objeto pessoa e seus atributos.
    Objeto pessoa projetado para guardar em apenas um instância uma lista de ocorrencias do objeto
    Exemplo:

    list_pessoa:
    [
        {
            'nome':'ABCDE',
            'idade':33,
        }, ...
    ]
    '''

    def __init__(self):
        '''
        Construtor do Objeto pessoa.
        Inicializa os atributos do objeto.
        '''
        self.nome = ''
        self.idade = ''
        self.list_pessoas = []

    def get_pessoa(self):
        '''
        Retorna o conteúdo de Pessoa em um Dicionário
        :return: dict com o conteudo de Pessoa
        '''
        return dict(
            nome=self.nome,
            idade=self.idade
        )

    def add_pessoa_list(self, nome, idade):
        '''
        Para usar apenas uma instância do objeto este método tem como função
        servir de "setter", setando os valores dos parâmetros do objeto e atribuindo os mesmos a uma lista
        no formato de dicionário.
        Exemplo: [{'nome':'ABC', 'idade':32},...]
        '''
        self.nome = nome
        self.idade = idade
        self.list_pessoas.append({'nome': self.nome, 'idade': self.idade})
