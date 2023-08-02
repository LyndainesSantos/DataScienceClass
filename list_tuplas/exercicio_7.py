# Faça um programa que leia os nomes dos 3 nadadores que subirão ao pódio na ordem do primeiro
# colocado para o terceiro. Imprima na tela a posição do nadador e seu nome.

list_nome = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º nadador: ")
    list_nome.append(nome)

for pos, nadador in enumerate(list_nome):
    print(pos+1,"º", nadador)

