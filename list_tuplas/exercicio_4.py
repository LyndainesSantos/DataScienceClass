# Faça um programa que leia 10 números inteiros e separe os mesmos em pares e ímpares. Mostre
# quantos pares foram lidos, bem como o maior e o menor número par. Faça o mesmo para os ímpares.

list_numero = []
list_par = []
list_impar = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    list_numero.append(numero)
    if (numero % 2 == 0):
        list_par.append(numero)
    else:
        list_impar.append(numero)

tam_par = len(list_par)
tam_impar = len(list_impar)

if tam_par > 0:
    maior_par = max(list_par)
    menor_par = min(list_par)
    print(f"Quantidade de números pares: {tam_par}")
    print(f"Maior número par: {maior_par}")
    print(f"Menor número par: {menor_par}")
else:
    print("Nenhum número par foi digitado!")

if tam_impar > 0:
    maior_impar = max(list_impar)
    menor_impar = min(list_impar)
    print(f"Quantidade de números ímpares: {tam_impar}")
    print(f"Maior número ímpar: {maior_impar}")
    print(f"Menor número ímpar: {menor_impar}")
else:
    print("Nenhum número ímpar foi digitado!")
