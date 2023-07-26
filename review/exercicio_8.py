# Faça um programa que leia 5 números e informe a soma e a média dos números.
n = 5
soma = 0

for i in range(n):
    numero = int(input("Digite um número: "))
    soma += numero

media = soma/n
print(f"A média dos números digitados é {media}")