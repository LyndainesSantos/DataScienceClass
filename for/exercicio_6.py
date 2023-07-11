# Crie um programa que leia dois valores e mostre um menu para calcular.
#   1 - Somar
# 	2 - Multiplicar
# 	3 - Dividir
# 	4 - Subtrair
# 	5 - Sair do programa

print("----------------------------------")
print("Menu:")
print("1 - Somar")
print("2 - Multiplicar")
print("3 - Dividir")
print("4 - Subtrair")
print("5 - Sair do programa")
print("----------------------------------")

numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite um número: "))
opcao = int(input("Digite a opção: "))

if(opcao == 1):
	soma = numero_1 + numero_2
	print("A soma é ", soma)
elif(opcao == 2):
	multiplicacao = numero_1 * numero_2
	print("A multiplicação é ", multiplicacao)
elif(opcao == 3):
	divisao = numero_1 / numero_2
	print("A divisão é ", divisao)
elif(opcao == 4):
	subtracao = numero_1 - numero_2
	print("A subtração é ", subtracao)
elif(opcao == 5):
	print("Programa finalizado!")
	exit(0)
else:
	print("Opção inválida!")
