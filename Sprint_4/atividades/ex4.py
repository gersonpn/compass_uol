def calcular_valor_maximo(operadores, operandos) -> float:
    def operacao_soma(operandos):
        return operandos[0] + operandos[1]

    def operacao_subtracao(operandos):
        return operandos[0] - operandos[1]

    def operacao_multiplicacao(operandos):
        return operandos[0] * operandos[1]

    def operacao_divisao(operandos):
        return operandos[0] / operandos[1]

    def operacao_modulo(operandos):
        return operandos[0] % operandos[1]

    operacoes = {
        "+": operacao_soma,
        "-": operacao_subtracao,
        "*": operacao_multiplicacao,
        "/": operacao_divisao,
        "%": operacao_modulo,
    }

    resultados = [operacoes[operador](operandos) for operador, operandos in zip(operadores, operandos)]

    return max(resultados)

operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))
