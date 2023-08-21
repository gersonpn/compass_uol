


lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']



for nome in lista:
    n = nome[::-1]

    if nome == n:
      print(f'A Palavra: {nome} é um palíndromo')
    else:
       print (f'A Palavra: {nome} não é um palíndromo')
