with open('number.txt', 'r') as f:
    number = f.readlines()

number = list(map(lambda x: int(x.strip()), number))
pares = list(filter(lambda x: x % 2 == 0, number))

pares = sorted(pares, reverse=True)

top_5 = pares[:5]
soma = sum(top_5)

print(top_5)
print(soma)
