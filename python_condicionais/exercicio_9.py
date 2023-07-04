# Escreva um programa que receba as notas de três provas de um aluno e calcule a média ponderada, considerando que a
# primeira prova tem peso 2, a segunda prova tem peso 3 e a terceira prova tem peso 5. O programa deve exibir a média
# final e uma mensagem indicando se o aluno foi aprovado (média igual ou superior a 7) ou reprovado (média inferior a 7).

nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
nota_3 = float(input("Digite a nota 3: "))

media_ponderada = (nota_1*2 + nota_2*3 + nota_3*5)/(2 + 3 + 5)

if(media_ponderada >=7):
    print("O aluno foi aprovado com media ", media_ponderada)
else:
    print("O aluno foi reprovado com média", media_ponderada)