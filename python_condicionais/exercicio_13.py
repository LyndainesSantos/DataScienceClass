# Escreva um programa que determine se um triângulo é equilátero, isósceles ou escaleno. O programa deve solicitar ao
# usuário que insira os comprimentos dos três lados do triângulo e exibir uma mensagem indicando qual tipo de triângulo é
# formado.

lado_1 = float(input("Digite o comprimento do primeiro lado: "))
lado_2 = float(input("Digite o comprimento do segundo lado: "))
lado_3 = float(input("Digite o comprimento do terceiro lado: "))

if( lado_1 == lado_2 == lado_3):
    print("Triãngulo é equilátero")
elif(lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3):
    print("Triângulo é escaleno")
else:
    print("Triângulo é isósceles")