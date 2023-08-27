dados = {}

with open('actors.csv') as arquivo:
    linhas = arquivo.readlines()
    info = linhas[0].strip().split(',')

for linha in linhas[1:]:
    valores = linha.strip().split(',')
    ator = valores[0]
    total_bruto = valores[1]
    n_filmes = valores[2]
    media_filmes = valores[3]
    maior_filme = valores[4]
    valor_bruto = valores[5]

    dados[ator] = {
        'Total Bruto': total_bruto.strip(),
        'Número de Filmes': n_filmes.strip(),
        'Média de Filmes': media_filmes.strip(),
        'Maior Filme': maior_filme.strip(),
        'Valor Bruto': valor_bruto.strip()
    }

for ator, info in dados.items():
    print(ator)
    for chave, valor in info.items():
        print(f"- {chave}: {valor}")
    print()



print(valor)