# Escreva uma função que receba uma string e verifique se ela é um palíndromo.

def verifica_palindromo(s):
    if(s == s[::-1]):
        return "A string é palíndromo!"
    else:
        return "A string não é palíndromo!"

string = input("Digite uma string: ")

print(verifica_palindromo(string))