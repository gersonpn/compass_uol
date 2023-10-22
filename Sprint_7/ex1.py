import pandas as pd

data = pd.read_csv('actors.csv')

atores = data['Actor']
total_gross = data['Total Gross']
n_filme = data['Number of Movies']
media_filme = data["Average per Movie"]

# 1 - Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
# A função 'idxmax()' retorna o índice (a posição) da linha onde a coluna 'Number of Movies' tem o valor máximo.
n_filmes = data['Number of Movies'].idxmax()

# Acesse as informações do ator/atriz com o maior número de filmes
ator_filme = data.loc[n_filmes, 'Actor']
# Usando o índice encontrado na etapa anterior, acesse os valores do ator/atriz e do número de filmes nessa linha.
number_of_movies = data.loc[n_filmes, 'Number of Movies']

print(f'O ator/atriz com o maior número de filmes é {ator_filme} com {number_of_movies} filmes.')

# 2 - Apresente a média da coluna contendo o número de filmes.

print(f'A média do número de filmes é: {n_filme.mean():.2f}')


# 3 - Apresente o nome do ator/atriz com a maior média por filme.

# Calcula a média por filme
data['Average per Movie'] = data['Total Gross'] / data['Number of Movies']

# Encontre o índice do ator/atriz com a maior média por filme
indice_max = data['Average per Movie'].idxmax()

# Acesse as informações do ator/atriz com a maior média por filme
actor_maior = data.loc[indice_max, 'Actor']
media = data.loc[indice_max, 'Average per Movie']

print(f'O ator/atriz com a maior média por filme é {actor_maior} com uma média de {media:.2f} por filme.')
