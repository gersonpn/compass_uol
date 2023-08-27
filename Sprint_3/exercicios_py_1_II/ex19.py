

import random

random_list = random.sample(range(500), 50)

for n in random_list:
    random_list = sorted(random_list)


mediana = 0

metade = len(random_list) // 2

if len(random_list) % 2 == 1:
    mediana = random_list[metade]
else:
    mediana = (random_list[metade - 1] + random_list[metade]) /2



media = (sum(random_list)) / len(random_list)
valor_minimo = (min(random_list))
valor_maximo = (max(random_list))

print (f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")