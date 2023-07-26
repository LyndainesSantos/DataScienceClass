# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
# a números inteiros positivos e menores que 16

while True:
    resultado = 1
    numero = int(input("Fatorial de: "))
    if(numero < 0 or numero > 16):
        continue
    for n in range(1, numero+1):
        resultado *= n

    print(resultado)