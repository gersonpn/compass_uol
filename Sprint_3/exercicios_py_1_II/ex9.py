#Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (sobre, idade) in enumerate(zip(sobreNomes, idades)):
    nome = primeirosNomes[indice]
    print(f'{indice} - {nome} {sobre} está com {idade} anos')
