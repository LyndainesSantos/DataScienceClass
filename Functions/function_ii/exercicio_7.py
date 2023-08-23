# Escreva uma função que receba um número e verifique se ele é primo.
def primo(n):
    cont = 0
    for i in range(2, n):
        if n % i == 0:
            cont += 1
    if cont >= 1 or n == 1:
        return 'O número não é primo!'
    else:
        return 'O número é primo!'

numero = int(input('Insira um número para saber se ele é primo: '))
print(primo(numero))