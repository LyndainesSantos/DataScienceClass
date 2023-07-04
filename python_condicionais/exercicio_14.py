# Escreva um programa que calcule o preço final de um produto considerando descontos progressivos. Se o valor total da
# compra for igual ou superior a R$ 100,00, haverá um desconto de 10%. Se for igual ou superior a R$ 200,00, o desconto
# será de 20%. Caso contrário, não haverá desconto. O programa deve solicitar ao usuário que insira o valor total da compra
# e exibir o preço final com o desconto aplicado, se houver.

compra = float(input("Valor da compra: "))

if(100 <= compra < 200):

    desconto = compra * 0.1

elif(compra >= 200):

    desconto = compra * 0.2

else:

    desconto = 0
    print("Não há desconto")

novo_valor = compra - desconto

print("O valor da compra com desconto será R$", novo_valor)