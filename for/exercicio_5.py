# Faça um programa que leia o gênero de uma pessoa, identificado pelos valores ‘M’ ou ‘F’. Caso esteja diferente dessas
# opções, peça para digitar novamente.

genero = input("Digite o seu gênero: ")

if(genero.lower() != 'f' and genero.lower() != 'm'):
    genero = input("Digite o seu gênero: ")
else:
    print("Gẽnero digitado: ", genero)