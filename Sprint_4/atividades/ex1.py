with open('number.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

numeros = list(filter(lambda x: x % 2 == 0, map(int, linhas)))

numeros_ordenados = sorted(numeros, reverse=True)

cinco_maiores = numeros_ordenados[:5]

print(cinco_maiores)
soma_cinco_maiores = sum(cinco_maiores)
print(soma_cinco_maiores)
