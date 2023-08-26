#Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

def pontencia(numero):
    return numero * numero

def my_map(list,f):
    lista = []
    for i in lista:
        lista.append(f(i))
    
