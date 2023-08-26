#Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.


def parametro (*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(valor)

parametro(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)