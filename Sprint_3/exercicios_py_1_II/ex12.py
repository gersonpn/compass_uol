#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

import json

with open('person.json') as arquivo:
    dados = json.load(arquivo)

print (dados)
