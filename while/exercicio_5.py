# Escreva um programa que leia uma lista de números inteiros do usuário e encontre o menor número da lista usando uma
# estrutura while.

numeros = []
quantidade = int(input("Digite a quantidade de números na lista: "))

while quantidade > 0:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    quantidade -= 1

menor = numeros[0]
indice = 1

while indice < len(numeros):
    if numeros[indice] < menor:
        menor = numeros[indice]
    indice += 1

print("O menor número da lista é:", menor)