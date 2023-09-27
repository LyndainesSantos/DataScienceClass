# Crie uma classe chamada Pessoa com atributos como nome, idade e cidade de nascimento. Em seguida, crie um método que
# exiba informações sobre a pessoa.

class Pessoa:
    def __init__(self, pessoa_nome, pessoa_idade, pessoa_cidade_natal):
        self.nome = pessoa_nome
        self.idade = pessoa_idade
        self.cidade_natal = pessoa_cidade_natal

    def exibir_infos(self):
        return self.nome, self.idade, self.cidade_natal