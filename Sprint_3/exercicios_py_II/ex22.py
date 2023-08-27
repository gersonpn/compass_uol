class Pessoa:
    def __init__(self, id):
        self.__nome = ""  
        self.id = id

    def retornar_nome(self):
        return self.__nome

    def definir_nome(self, novo_nome):
        self.__nome = novo_nome

    nome = property(retornar_nome, definir_nome)


pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
