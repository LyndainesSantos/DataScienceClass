# Escreva um programa que leia uma lista de números inteiros do usuário e encontre o maior número da lista usando uma
# estrutura for.

numeros = []
quantidade = int(input("Digite a quantidade de números na lista: "))

for i in range(quantidade):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

menor = numeros[0]

for i in numeros:
    if i > menor:
        menor = i

print("O maior número da lista é:", menor)