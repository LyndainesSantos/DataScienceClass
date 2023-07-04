# Faça um Programa que leia três números e mostre o maior deles.

# Faça um Programa que peça dois números e imprima o maior deles

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o segundo número: "))

if (numero_1 > numero_2 and numero_1 > numero_3):
    print("O maior é ", numero_1)
elif (numero_2 > numero_1 and numero_2 > numero_3):
    print("O maior é ", numero_2)
else:
    print("O maior é ", numero_3)