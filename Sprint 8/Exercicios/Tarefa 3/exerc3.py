import random
import names

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

nomes_aleatorios = [random.choice(nomes_unicos)
                    for _ in range(qtd_nomes_aleatorios)]

with open("nomes_aleatorios.txt", "w") as arquivo:
    arquivo.write("\n".join(nomes_aleatorios))
