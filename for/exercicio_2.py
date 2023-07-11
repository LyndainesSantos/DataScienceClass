# Fazer um programa que imprime na tela os números entre 100 e 200, com passo informado pelo usuário.

passo = int(input("Digite o passo: "))

for i in range(100, 201, passo):
    print(i)