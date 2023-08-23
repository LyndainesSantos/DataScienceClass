# Escreva uma função que receba uma lista de números e retorne a soma entre eles.
def soma_numeros(lista_numero):
    return sum(lista_numero)

qtde = int(input("Informe quantos números deseja digitar: "))
lista_n = []

for i in range(qtde):
    lista_n.append(float(input("Digite um número: ")))

print("A soma total é", soma_numeros(lista_n))