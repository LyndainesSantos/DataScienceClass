# A partir de uma lista de strings, utilize map() e uma função lambda para
# converter todas as letras em maiúsculas.

lista = ["olá", "bom dia", "boa tarde", "boa noite"]
resultado = list(map(lambda x: x.upper(), lista))
print(resultado)