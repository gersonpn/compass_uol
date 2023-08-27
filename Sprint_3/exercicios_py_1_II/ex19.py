import random


random_list = random.sample(range(500), 50)
print(random_list)

for n in random_list:
    random_list = sorted(random_list)


print(random_list)


mediana = 0


media = (sum(random_list)) // len(random_list)
valor_minimo = (min(random_list))
valor_maximo = (max(random_list))

print(valor_minimo, valor_maximo, media)