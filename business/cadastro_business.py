class CadastroBusiness:
    """
        TODO: adicionar regra de negocio para cada parâmetro informado.
    """
    @classmethod
    def valida_body_request(cls, request):
        data = request.get_json()
        data = dict(data)
        if 'curso' in data['usuario']:
            for item in data['usuario']['curso']:
                if type(item) == dict:
                    if 'nome' not in item and 'turno' not in item:
                        return 'Dados informados não conferem com os dados de Curso. Visite a documentação.'
        elif 'usuario' in data:
            for item in data['usuario']:
                if type(item) == dict:
                    if 'username' not in item and 'email' not in item and 'password' not in item and 'nome' not in item and 'data_nascimento' not in item:
                        return 'Dados informados não conferem com os dados de Usuário. Visite a documentação.'
        else:
            return data
