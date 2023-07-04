# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

# if(letra in ["a","e","i","o","u"]):
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):

    print("É uma vogal")
else:
    print("É uma consoante")