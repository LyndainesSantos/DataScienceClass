# Escreva uma função que receba dois números e retorne o menor deles
def menor_numero(n1,n2):
    lista = [n1,n2]
    return min(lista)

numero_1 = float(input("Informe o número 1: "))
numero_2 = float(input("Informe o número 2: "))

print("O menor número digitado é", menor_numero(numero_1, numero_2))