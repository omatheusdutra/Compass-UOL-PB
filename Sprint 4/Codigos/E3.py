from functools import reduce


def calcula_saldo(lancamentos) -> float:
    saldo_inicial = 0
    soma_credito = reduce(
        lambda x, y: x + y, map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos), saldo_inicial)
    return saldo_inicial + soma_credito


lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

saldo_final = calcula_saldo(lancamentos)
print(saldo_final)
