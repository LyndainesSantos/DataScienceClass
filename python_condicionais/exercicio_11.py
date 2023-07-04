# Faça um programa que receba dois números e execute as operações listas a seguir, de acordo com a escolha do usuário.
# 1. Média 2. Diferença (maior pelo menor) 3. Produto 4. Divisão

numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite um número: "))
op = int(input("Escolha a opção: "))

if(op == 1):
    media = (numero_1 + numero_2) / 2
    print("A média é", media)
elif(op == 2):
    diferenca = abs(numero_1 - numero_2)
    print("A diferença entre o maior e menor número é", diferenca)
elif(op == 3):
    produto = numero_1 * numero_2
    print("O produto é ", produto)
elif(op == 4):
    divisao = numero_1 / numero_2
    print("A divisão é ", divisao)
else:
    print("Opção inválida!")