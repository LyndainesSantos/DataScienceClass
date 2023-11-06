# Escreva uma função lambda que receba um número e verifique se ele é par ou
# ímpar. A função deve retornar "par" se o número for par e "ímpar" caso contrário.

resultado = lambda x: "par" if x % 2 == 0 else "ímpar"
print(resultado(2))
print(resultado(5))