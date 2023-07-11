# Escreva um algoritmo que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo.

numero = int(input("Digite um número: "))

if(numero > 1 and numero != 2):
    for i in range(2,numero):
        if(numero % i == 0):
            print("Número", numero, "não é primo")
            exit(0)
        else:
            print("O número", numero, "é primo")
            exit(0)
elif(numero == 2):
    print("O número", numero, "é primo")
else:
    print("O número", numero, "não é primo")
