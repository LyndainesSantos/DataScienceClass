# Crie uma classe chamada Triangulo com atributos para os lados A, B e C. Adicione métodos para calcular a área e
# verificar se o triângulo é equilátero, isósceles ou escaleno.
import math
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def verificar(self):
        if (self.a == self.b and self.a == self.c):
            return "Equilátero"
        elif (self.a == self.b or self.a == self.c):
            return "Isósceles"
        else:
            return "Escaleno"