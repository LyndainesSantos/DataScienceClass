# Faça um programa que receba dez números, calcule e mostre a soma dos números pares e dos números impares

soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    if(numero % 2 == 0):
        soma_pares += numero
    else:
        soma_impares += numero

print("A soma dos números pares é igual a ", soma_pares)
print("A soma dos números ímpares é igual a ", soma_impares)