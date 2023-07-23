def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = list(map(lambda op, opd: eval(
        str(opd[0]) + op + str(opd[1])), operadores, operandos))
    valores_combinados = zip(operadores, operandos)
    resultados = list(
        map(lambda x: eval(str(x[1][0]) + x[0] + str(x[1][1])), valores_combinados))
    valor_maximo = max(resultados)
    return valor_maximo


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)
