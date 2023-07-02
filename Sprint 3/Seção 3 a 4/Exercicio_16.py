# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores.
# A string deve ter valor  "1,3,4,6,10,76"

def somar_numeros(string_numeros):
    numeros = string_numeros.split(",")  
    soma = 0
    for numero in numeros:
        soma += int(numero) 
    return soma
    
string_numeros = "1,3,4,6,10,76"
resultado = somar_numeros(string_numeros)

print(resultado)
