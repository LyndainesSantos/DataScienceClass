# Faça um Programa que peça dois números e imprima o maior deles

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if (numero_1 > numero_2):
    print("O maior é ", numero_1)
elif (numero_2 > numero_1):
    print("O maior é ", numero_2)
else:
    print("Os números são iguais")