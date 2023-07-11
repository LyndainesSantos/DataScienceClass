# Faça um programa que leia um número inteiro e informe se ele é perfeito ou não.
# Um número perfeito é aquele que é igual à soma de seus divisores. Ex.: 6 = 1 + 2 + 3 = número perfeito

numero = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1,numero):
    if(numero % i == 0):
        soma += i
if(soma == numero):
    print(numero, "é um número perfeito")
else:
    print(numero, "não é um número perfeito")