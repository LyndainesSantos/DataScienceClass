# Escreva uma função que receba uma lista de números e retorne o maior valor

def maior_numero(numeros: list):
    return max(numeros)

qtde = int(input("Digite a quantidade de números a ser digitada: "))

list_numero = []
for i in range(qtde):
    list_numero.append(float(input("Digite um número: ")))

print(maior_numero(list_numero))