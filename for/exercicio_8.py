# Escreva um algoritmo que receba uma string do usuário e conte quantas vogais (a, e, i, o, u) ela possui.

string = input("Digite uma palavra: ")
count = 0

for letra in string:
    if letra.lower() in "aeiou":
        count += 1
print("O número de vogais é ", count)