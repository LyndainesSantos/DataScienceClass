# Faça um programa que leia 5 nomes e armazene os valores em uma lista. Ao final, imprima o índice e o nome de cada
# pessoa na lista utilizando o enumrate

list_nome = []
n = 5

for i in range(5):
    nome = input("Digite um nome: ")
    list_nome.append(nome)

for indice, nome in enumerate(list_nome):
    print(f"Índice {indice}: {nome}")