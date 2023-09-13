animais = ["Cachorro", "Gato", "Elefante", "Leão", "Tigre", "Zebra", "Girafa", "Panda", "Coelho", "Cavalo",
           "Macaco", "Pinguim", "Urso", "Pássaro", "Peixe", "Serpente", "Avestruz", "Rinoceronte", "Hipopótamo"]

animais.sort()

print(animais)

with open("animais.csv", "w") as arquivo:
    arquivo.write("\n".join(animais))
