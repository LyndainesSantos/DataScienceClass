numero = input("Digite um número: ")

numero_reverso = numero[::-1]

if (numero == numero_reverso):
    print("O número", numero, "é um palíndromo.")
else:
    print("O número", numero, "não é um palíndromo.")

