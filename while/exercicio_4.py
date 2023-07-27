# Escreva um programa que leia um número inteiro positivo do usuário e imprima a soma de todos os números ímpares entre
# 1 e o número digitado.

soma = 0
i = 0

numero = int(input("Digite um número inteiro: "))

while True:
    if(i <= numero):
        if(i % 2 !=0):
            soma += i
        i += 1
    else:
        break

print(f"A soma dos números ímpares é {soma}")

# for i in range(1, numero+1):
#     if(i % 2 !=0):
#         soma += i