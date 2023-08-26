def soma_string (*args):

    numero = args[0].split(',')

    resultado = 0

    for n in numero:
        n = int(n)
        resultado += n

    return resultado

a = "1,3,4,6,10,76"

print(soma_string(a))