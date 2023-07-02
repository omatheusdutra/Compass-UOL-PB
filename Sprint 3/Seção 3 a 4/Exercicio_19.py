# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

# import random 
# amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)

# Use as variáveis abaixo para representar cada operação matemática:

# mediana
# media
# valor_minimo 
# valor_maximo 


import random

random_list = random.sample(range(500), 50)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

random_list.sort()
if len(random_list) % 2 == 0:
    mediana = (random_list[len(random_list) // 2 - 1] + random_list[len(random_list) // 2]) / 2
else:
    mediana = random_list[len(random_list) // 2]

output = "Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}".format(media, mediana, valor_minimo, valor_maximo)
print(output)
