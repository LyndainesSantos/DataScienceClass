# Escreva uma função que receba uma lista de strings e retorne a quantidade de strings na lista

string = input("Digite algo: ")

def tamanho_strings(s):
    espaco_branco = string.count(" ")
    return len(string) - espaco_branco

print("A quantidade de strings é", tamanho_strings(string))