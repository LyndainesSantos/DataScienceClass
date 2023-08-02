# Faça um programa que leia 4 notas de um aluno e imprima sua média. Após a média ser calculada,
# informe se o aluno foi ou não aprovado.
# a. Aprovado --- média maior ou igual a 7
# b. Reprovado --- média menor que 5
# c. Em recuperação --- média entre 5 e 7

n = 4
list_nota = []

for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    list_nota.append(nota)

soma = sum(list_nota)
media = soma / len(list_nota)

print(f"A média do aluno: {media}")

if(media >= 7):
    print("Aprovado")
elif(5 <= media < 7):
    print("Em recuperação")
else:
    print("Reprovado")