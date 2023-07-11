# Fazer um programa para encontrar todos os números pares entre 1 e 100.
# Informar também quantos são e quais são os ímpares

impar = 0

for i in range(1, 101):
    if(i % 2 == 0):
        print("par:", i)
    else:
        impar += 1
        print("ímpar:", i)

print("O total de números ímpares é igual a ", impar)