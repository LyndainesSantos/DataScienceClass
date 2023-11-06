# Implemente uma função lambda que receba um número e verifique se ele é divisível
# por 3 e por 5. A função deve retornar "divisível" se a condição for satisfeita e "não
# divisível" caso contrário.

resultado = lambda x: "divisível" if x % 3 == 0 and x % 5 == 0 else "Não divisível"
print(resultado(15))
print(resultado(7))
