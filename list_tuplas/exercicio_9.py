# Faça um algoritmo que relaize a leitura de 7 números e imprima os índices dos números  que são divisíveis por 3 e por 9.
# Use o enumerate.

list_numeros = []
n = 7

for i in range(n):
    numero = int(input("Digite um número: "))
    list_numeros.append(numero)

for indice, numero in enumerate(list_numeros):
    if (numero % 3 == 0 and numero % 9 == 0):
        print(f"No índice {indice} tem número divisível por 3 e 9")