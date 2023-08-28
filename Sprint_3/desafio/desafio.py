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
        'Total Gross': total_bruto.strip(),
        'Number of Movies': n_filmes.strip(),
        'Average per Movie': media_filmes.strip(),
        '1_Movie': maior_filme.strip(),
        'Gross': valor_bruto.strip()
    }

dados_gross = []
dados_bruto_total = {}
aparicoes_filmes = {}

maior_media = 0.0
ator_com_maior_media = None

for ator, info in dados.items():
    print(ator)
    for chave, valor in info.items():
        print(f"- {chave}: {valor}")

    filme_maior_bilheteria = info['1_Movie']
    if filme_maior_bilheteria in aparicoes_filmes:
        aparicoes_filmes[filme_maior_bilheteria] += 1
    else:
        aparicoes_filmes[filme_maior_bilheteria] = 1

    try:
        bruto = float(info['Gross'])
        if bruto >= 0:
            dados_gross.append(bruto)
    except ValueError:
        pass

    try:
        bruto_total = float(info['Total Gross'])
        if bruto_total >= 0:
            dados_bruto_total[ator] = bruto_total
    except ValueError:
        pass

    try:
        media_filmes = float(info['Average per Movie'])
        if media_filmes > maior_media:
            maior_media = media_filmes
            ator_com_maior_media = ator
    except ValueError:
        pass

filmes_ordenados = sorted(aparicoes_filmes.items(), key=lambda x: (x[1], x[0]), reverse=True)

dados_bruto_total_ordenados = sorted(dados_bruto_total.items(), key=lambda x: x[1], reverse=True)


with open('etapa1.txt') as etapa1:
    print(max(dados.items(), key=lambda k: k[1]['Number of Movies']), file=etapa1)

with open('etapa2.txt') as etapa2:
  media =  sum(dados_gross) / len(dados_gross)
  print(f"A media da receita foi de ${media:.3f} dolares", file=etapa2)

with open('etapa3.txt') as etapa3:
    print(f"A atriz com a maior media de receita bruta por filme é {ator_com_maior_media} com uma média de ${maior_media:.3f}", file=etapa3)

with open('etapa4.txt') as etapa4:
    for sequencia, (nome_filme, quantidade) in enumerate(filmes_ordenados, start=1):
        linha = f"{sequencia} - O filme '{nome_filme}' aparece {quantidade} vez(es) no dataset"
        print(linha, file=etapa4)

with open('etapa5.txt') as etapa5:
    for ator, bruto_total in dados_bruto_total_ordenados:
        print(f'{ator}: {bruto_total}', file=etapa5)
