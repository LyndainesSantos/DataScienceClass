# Escreva um programa que leia uma lista de números inteiros do usuário e encontre a média dos números da lista usando
# uma estrutura for.
import numpy
list_numero = []
soma = 0
quantidade = int(input("Digite um número inteiro positivo: "))

for i in range(quantidade):
    numero = input("Digite um número: ")
    list_numero.append(numero)

for i in list_numero:
    soma += i

media = soma / quantidade

print(f"A média é {soma}")