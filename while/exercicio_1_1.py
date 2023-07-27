# Faça um programa que leia o sexo de uma pessoa, identificado pelos valores ‘M’ ou ‘F’. Caso esteja errado, peça para
# digitar novamente.

while True:

    genero = input("Digite o seu gênero: ")

    if(genero.lower() == 'm'):
        print("Gênero Masculino")
        break
    elif (genero.lower() == 'f'):
        print("Gênero Feminino")
        break

# genero = 'd'
# while (genero != 'm' or genero != 'f'):
#
#     genero = input("Digite o seu gênero: ")
#
#     if(genero.lower() == 'm'):
#         print("Gênero Masculino")
#         break
#     elif (genero.lower() == 'f'):
#         print("Gênero Feminino")
#         break


