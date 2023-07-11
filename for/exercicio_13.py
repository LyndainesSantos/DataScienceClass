# Escreva um algoritmo que recebe dois números do usuário e verifica se eles são números amigos. Números amigos são pares
# de números inteiros em que a soma dos divisores próprios de um número é igual ao outro número e vice-versa.

def soma_divisores(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    return soma

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma_divisores_num1 = soma_divisores(num1)
soma_divisores_num2 = soma_divisores(num2)

if soma_divisores_num1 == num2 and soma_divisores_num2 == num1:
    print("Os números", num1, "e", num2, "são números amigos.")
else:
    print("Os números", num1, "e", num2, "não são números amigos.")
