# Faça um programa que receba dez números, calcule e mostre a soma dos números pares e dos números impares

soma = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    if(numero % 2 == 0):
        soma += numero

print("A soma dos números pares é igual a ", soma)