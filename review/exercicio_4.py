# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente".

telefone = input("Telefonou para a vítima? ")
local = input("Esteve no local do crime? ")
morar = input("Mora perto da vítima? ")
dever = input("Devia para a vítima? ")
trabalhar = input("Já trabalhou com a vítima? ")

cont = 0

if(telefone == 's'):
    cont += 1
if(local == 's'):
    cont +=1
if(morar == 's'):
    cont +=1
if(dever == 's'):
    cont +=1
if(trabalhar == 's'):
    cont +=1

if(cont == 2):
    print("Suspeito")
elif(3 <= cont <= 4):
    print("Cúmplice")
elif(cont == 5):
    print("Assassino")
else:
    print("Inocente")
