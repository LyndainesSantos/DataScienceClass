# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = int(input("Quantos núeros deseja digitar? "))

list_numero = []
for i in range(quantidade):
    numero = int(input("Digite um número: "))
    list_numero.append(numero)

print(min(list_numero))
print(max(list_numero))
print(sum(list_numero))
