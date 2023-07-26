# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

quantidade = int(input("Quantos núeros deseja digitar? "))

list_numero = []
for i in range(quantidade):
    numero = int(input("Digite um número: "))
    while (numero < 0 or numero > 1000):
        numero = int(input("Digite um número novamente: "))
    list_numero.append(numero)

print(min(list_numero))
print(max(list_numero))
print(sum(list_numero))
