# Escreva um algoritmo que calcule a soma de todos os números entre 1 e 1000 que sejam múltiplos de 3 ou 5.
soma_multip_3 = 0
soma_multip_5 = 0

for i in range(1,1001):
    if(i % 3 == 0):
        soma_multip_3 += i
    elif(i % 5 == 0):
        soma_multip_5 += i
print("Soma dos múltiplos de 3: ", soma_multip_3)
print("Soma dos múltiplos de 5: ", soma_multip_5)