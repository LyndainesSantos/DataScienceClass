# Escreva um programa que verifique se um ano é bissexto. O programa deve solicitar ao usuário que insira um ano e exibir
# uma mensagem indicando se o ano é bissexto ou não.
# Lembre-se de que um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

