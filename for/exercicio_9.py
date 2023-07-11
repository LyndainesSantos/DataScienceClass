# Faça um programa que receba a idade, a altura e o peso de 25 pessoas, calcule e mostre:
# a) A quantidade de pessoas com idade superior a 50 anos;
# b) A média das alturas das pessoas com idade entre 10 e 20 anos;
# c) O percentual de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

cont_idade = 0
soma_altura = 0
cont_altura = 0
cont_peso = 0
n_pessoas = 5

for i in range(n_pessoas):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))

    # a) idade > 50 anos

    if(idade > 50):
        cont_idade += 1
    elif(10 <= idade <= 20):
        soma_altura += altura
        cont_altura += 1
    if(peso < 40):
        cont_peso += 1

media_altura = soma_altura / cont_altura
perc_peso = (cont_peso / n_pessoas)*100

print("Pessoas com mais de 50 anos: ", cont_idade)
print("Média da altura de pessoas entre 10 e 20 anos: ", media_altura)
print("O percentual de pessoas com peso inferior a 40 kg: ", perc_peso, "%")
