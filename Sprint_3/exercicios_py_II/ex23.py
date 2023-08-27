class Calculo:
    def soma(self, x,y):
        return x + y
    def subtracao (self, x,y):
        return x - y


calculo = Calculo()


soma = calculo.soma(1, 5)
print(soma)

sub = calculo.subtracao(2,5)
print(sub)