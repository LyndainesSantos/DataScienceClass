# A partir de uma lista de palavras, utilize filter() e uma
# função lambda para filtrar apenas as palavras que possuem
# mais de 5 letras.
lista = ["olá", "bom dia", "boa tarde", "boa noite"]
resultado = list(filter(lambda x: len(x) > 5, lista))
print(resultado)