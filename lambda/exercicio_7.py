# Dada uma lista de valores numéricos, utilize reduce() e
# uma função lambda para obter o valor máximo da lista.

from functools import reduce
lista = [1,2,3,4,5,6,7,8,9]
resultado = reduce(lambda x, y: x if x > y else y, lista)
print(resultado)