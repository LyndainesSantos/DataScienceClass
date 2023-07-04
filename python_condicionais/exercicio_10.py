# Escreva um programa que verifique se um número é positivo, negativo ou zero. O programa deve solicitar ao usuário que
# insira um número e exibir uma mensagem indicando se o número é positivo, negativo ou zero.

numero = float(input("Digite um número: "))

if(numero > 0):
    print("O númeo é positivo")
elif(numero == 0):
    print("O número é igual a Zero")
else:
    print("O número é negativo")