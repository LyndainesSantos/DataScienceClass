# Faça um Programa que receba 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
# operação deve aparecer com uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha a opção: "))

if(opcao == 1):
    result = numero_1 + numero_2
    print(f"A soma é {result}")
elif(opcao == 2):
    result = numero_1 - numero_2
    print(f"A subtração é {result}")
elif(opcao == 3):
    result = numero_1 * numero_2
    print(f"A multiplicação é {result}")
elif(opcao == 4):
    if(numero_2 != 0):
        result = numero_1 / numero_2
        print(f"A divisão é {result}")
    else:
        print("O denominador dever ser um número diferente de zero!")
        exit()
else:
    print("Opção Inválida!")
    exit()

if(result % 2 == 0):
    print("O resultado é par")
else:
    print("O Resultado é ímpar")
if(result >= 0):
    print("O Resultado é positivo")
else:
    print("O Resultado é negativo")

print("O tipo é", type(result))