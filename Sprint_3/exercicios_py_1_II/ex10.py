#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.


def nao_repetidos(lista):
    conjunto_sem_repeticoes = set(lista)
    lista_sem_repeticoes = list(conjunto_sem_repeticoes)
    return lista_sem_repeticoes

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
l = nao_repetidos(lista)
print(l)
