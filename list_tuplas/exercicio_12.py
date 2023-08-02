# Leia uma lista de duas coordenadas (x e y) e calcule a distância eucliadiana usando zip.

import math
list_x = []
list_y = []

for i in range(2):

    x = float(input(f"Informe a posição de x{i+1}: "))
    y = float(input(f"Informe a posição de y{i+1}: "))
    list_x.append(x)
    list_y.append(y)

for x1, y1, x2, y2 in zip(list_x[:-1], list_y[:-1], list_x[1:], list_y[1:]):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"A distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é {distancia:.2f}")

