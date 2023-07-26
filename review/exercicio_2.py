# Faça um Programa que verifique se a letra digitada pelo usuário é vogal ou consoante.

letra = input("Digite uma letra: ")

if(letra in "aeiou"):
    print("A letra é vogal")
else:
    print("A letra é consoante")