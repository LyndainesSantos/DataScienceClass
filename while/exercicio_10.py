# Escreva um programa que leia um número inteiro positivo do usuário e calcule o fatorial desse número usando uma
# estrutura while.

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número deve ser positivo.")
else:
    fatorial = 1
    i = 1

    while i <= numero:
        fatorial *= i
        i += 1

    print("O fatorial de", numero, "é", fatorial)
