# Escreva um programa que leia uma palavra do usuário e conte o número de vogais na palavra usando uma estrutura for.

string = input("Digite uma palavra: ")
count = 0

for letra in string:
    if letra.lower() in "aeiou":
        count += 1
print("O número de vogais é ", count)