# Escreva um programa que leia um número inteiro positivo do usuário e imprima todos os números pares entre 0 e o número
# digitado.

numero = int(input("Digite um número inteiro: "))

i = 0
while i <= numero:
    if(i % 2 == 0):
        print(i)
    i += 1

# for i in range(0, numero+1):
#     if(i % 2 == 0):
#         print(i)
# while True:
#     if(i <= numero):
#         if(i % 2 == 0):
#             print(i)
#         i+=1
#     else:
#         break

