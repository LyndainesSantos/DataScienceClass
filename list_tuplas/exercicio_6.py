# Faça um programa que leia o nome de 4 vendedores e o valor total de venda que cada um realizou.
# Imprima na tela os 2 vendedores que mais venderam, ordem decrescente.

list_vendendor = []
list_venda = []
n = 4
for i in range(n):
    nome = input(f"Digite o nome do {i + 1}º vendedor: ")
    list_vendendor.append(nome)
    valor_vendas = float(input(f"Digite o valor total de vendas do {i + 1}º vendedor: "))
    list_venda.append(valor_vendas)

list_vendendor_venda = list(zip(list_vendendor, list_venda))

list_vendendor_venda.sort(key=lambda x: x[1], reverse=True)

print("Primeiro vendendor com maior venda: ", list_vendendor_venda[0][0])
print("Segundo vendendor com maior venda: ", list_vendendor_venda[1][0])