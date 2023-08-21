#Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não. Importante: Aplique a função range().


for numero in range(2, 101):
    n_primo = True  

    if numero <= 1:
        n_primo = False
    elif numero == 2:
        n_primo = True
    elif numero % 2 == 0:
        n_primo = False

    for div in range(2, int(numero ** 0.5) + 1):
        if numero % div == 0:
            n_primo = False
            break

    if n_primo:
        print(numero)
