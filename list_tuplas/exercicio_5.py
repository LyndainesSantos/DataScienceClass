# Faça um programa que leia 10 números inteiros e imprima a lista ordenada em ordem crescente e
# decrescente.

n = 10
list_numero = []

for i in range(n):
    numero = int(input("Digite um número: "))
    list_numero.append(numero)

list_numero.sort()
print("Lista em ordem crescente: ", list_numero)

list_numero.sort(reverse=True)
print("Lista em ordem decrescente: ", list_numero)
