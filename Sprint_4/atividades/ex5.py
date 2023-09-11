import csv


def calcular_media_tres_maiores(notas):
    maiores = sorted(notas, reverse=True)[:3]
    media = sum(maiores) / 3
    return round(media, 2)

with open('estudantes.csv', 'r', newline='') as arquivo:
    estudante = csv.reader (arquivo)



    for linha in estudante:
        nome = linha[0]
        notas = list(map(int, linha[1:]))
        media_tres_maiores = calcular_media_tres_maiores(notas)

        print(f"Nome: {nome} Notas: {notas} Média: {media_tres_maiores}")
