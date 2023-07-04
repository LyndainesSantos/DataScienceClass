# se a compra for de V=45 e o número de parcelas for P=7, então as parcelas terão valores: 7, 7, 7, 6, 6, 6 e 6. Quer
# dizer, como o resto da divisão de 45 por 7 é 3, então as 3 parcelas iniciais devem ter valor um real maior do que as 4
# parcelas finais. Você precisa ajudar Pedrinho e escrever um programa que, dado o valor da compra e o número de parcelas,
# imprima os valores de cada parcela. O programa deve receber como entrada o valor de V, representando o valor da compra e
# o valor de P, indicando o número de parcelas. A saída deve ser as parcelas.

compra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite o número de parcelas: "))

if(parcelas <=18):
    if(compra % parcelas == 0):
        valor_parcela = compra / parcelas
        print("A compra pode ser dividida em", parcelas, "parcelas de R$", valor_parcela)
    else:
        numero_parcela_inicias = compra % parcelas
        valor_parcelas_iniciais = (compra // parcelas) + 1
        numero_parcela_restante = parcelas - numero_parcela_inicias
        valor_parcelas_finais = compra // parcelas

        print("A compra pode ser dividida em", int(numero_parcela_inicias), "parcelas iniciais de R$",
              valor_parcelas_iniciais, "e", int(numero_parcela_restante), "de R$", valor_parcelas_finais)
else:
    print("O número de parcelas é inválido!")