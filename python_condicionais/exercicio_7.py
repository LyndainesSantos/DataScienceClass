# Faça um algoritmo que verifique se o número digitado pelo usuário é múltiplo de três ou não.
# Em caso afirmaivo: imprime a mensagem “É múltiplo de 3”
# Caso contrário, “Não é múltiplo de 3”

numero = float(input("Digite um número: "))

if(numero % 3 == 0):
    print("O número é múltiplo de 3")
else:
    print("O número não é multiplo de 3")