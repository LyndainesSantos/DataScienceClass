# Escreva um programa que leia uma lista de números inteiros do usuário e imprima apenas os números pares usando uma
# estrutura for.

quantidade = int(input("Digite a quantidade de palavras na lista: "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))

    if(numero % 2 == 0):
        print(f"O número {numero} é par")