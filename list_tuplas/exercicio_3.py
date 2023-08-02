# Faça um programa que leia 10 números e depois mostre o maior e o menor números lidos

list_numero = []

for j in range(10):
    numero = int(input("Informe um núemro: "))
    list_numero.append(numero)

min = min(list_numero)
max = max(list_numero)

print(f"O menor número: {min}")
print(f"O maior número: {max}")