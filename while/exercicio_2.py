# Escreva um programa que leia uma lista de números inteiros do usuário e imprima apenas os números que são múltiplos de
# 3 usando uma estrutura while

quantidade = int(input("Digite a quantidade de palavras na lista: "))
cont = 0
while (cont < quantidade):
    cont += 1
    numero = int(input("Digite um número: "))

    if (numero % 3 == 0):
        print(f"O número {numero} é múltiplo de 3")