import csv

with open('estudantes.csv', 'r') as f:

    estudantes = sorted([(row.split(",")[0], sorted(list(map(int, row.split(
        ",")[1:])), reverse=True)[:3]) for row in f.readlines()], key=lambda x: x[0])

    for estudante in estudantes:
        nome = estudante[0]
        notas = estudante[1]
        media = round(sum(notas) / len(notas), 2)
        print(f'Nome: {nome} Notas: {notas} Média: {media}')
