def conta_vogais(texto: str) -> int:
    vogais = "aeiou"
    vogais_encontradas = filter(lambda x: x.lower() in vogais, texto)
    quantidade_vogais = len(list(vogais_encontradas))

    return quantidade_vogais
