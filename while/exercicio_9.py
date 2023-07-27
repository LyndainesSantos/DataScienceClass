# Escreva um programa que leia uma lista de palavras do usuário e imprima as palavras em ordem alfabética usando uma
# estrutura while.

palavras = []
quantidade = int(input("Digite a quantidade de palavras na lista: "))

while quantidade > 0:
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)
    quantidade -= 1

indice = 0

while indice < len(palavras) - 1:
    if palavras[indice] > palavras[indice + 1]:
        palavras[indice], palavras[indice + 1] = palavras[indice + 1], palavras[indice]
        if indice > 0:
            indice -= 1
    else:
        indice += 1

print("Palavras em ordem alfabética:")
for palavra in palavras:
    print(palavra)