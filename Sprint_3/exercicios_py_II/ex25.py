class Aviao():
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade

avioes = [
    Aviao("BOIENG456", 1500, 400),
    Aviao("Embraer Praetor 600", 863, 14),
    Aviao("Antonov An-2", 258, 12)
]



for aviao in avioes:
    print(f"Modelo: {aviao.modelo}")
    print(f"Velocidade máxima: {aviao.velocidade_maxima}km/h")
    print(f"Capacidade para: {aviao.capacidade} passageiros")
    print(f"Cor: {aviao.cor}")
