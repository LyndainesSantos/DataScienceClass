# Leia 10 produtos e seus respectivos preços e crie um dicionário onde os nomes dos produtos são as chaves e os preços são
# os valores. Us zip.

strings = ["a", "b", "c", "d"]
inteiros = [1, 2, 3, 4]
list_produto = []
list_preco = []
dicionario = {}
n = 10

for i in range(n):
    produto = input("Informe o nome do produto: ")
    list_produto.append(produto)
    preco = float(input("Informe o preço do produto: "))
    list_preco.append(preco)


for chave, valor in zip(list_produto, list_preco):
    dicionario[chave] = valor

print(dicionario)
