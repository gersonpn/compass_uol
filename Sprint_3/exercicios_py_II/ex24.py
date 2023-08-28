class Ordenadora():
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)

crescente = Ordenadora([3,4,2,1,5])
crescente.ordenacaoCrescente()

decrescente = Ordenadora([9,7,6,8])
decrescente.ordenacaoDecrescente()


print(crescente.listaBaguncada)

print(decrescente.listaBaguncada)
