def conta_vogais(string):
    vogal = lambda char: char.lower() in 'aeiou'
    vogais = filter(vogal, string)

    quantidade_vogais = len(list(vogais))

    return quantidade_vogais

texto = "nome"
resultado = conta_vogais(texto)
print(resultado)
