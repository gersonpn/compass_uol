class Passaro:
    def voar(self):
        print("voando...")

    def emitir_som(self):
        print("emitindo som")

        pass

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")


pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

pardal = Pardal()
print('Pardal')

pardal.voar()
pardal.emitir_som()