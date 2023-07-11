# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
# informar qual numero ele deseja ver a tabuada.

numero = int(input("Digite um número: "))

for i in range(1,11):
    print(numero,"x",i,"=",numero*i)