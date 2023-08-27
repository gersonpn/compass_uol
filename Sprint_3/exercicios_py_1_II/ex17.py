def separador_lista(lista, tamanho):
    tam_l = len(lista)//tamanho
    sublistas = []


    for i in range(0, len(lista), tam_l):
        sublista = lista[i:i + tam_l]
        sublistas.append(sublista)

    return sublistas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tamanho = 4


sublistas = separador_lista(lista, tamanho)
for sublista in sublistas:
    print(sublista, '\n')
