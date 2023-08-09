# Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:
# a. Nome do aluno
# b. As 4 notas obtidas
# c. Maior nota
# d. Menor nota
# e. Média
# f. Situação
# Agora imprima as informações deste aluno na saída padrão

aluno = {}
notas = []

aluno["nome"] = input("Informe seu nome: ")

for i in range(4):
    notas.append(float(input(f"Digite a nota {i+1}: ")))

media = sum(notas)/len(notas)
if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

aluno["media"] = media
aluno["maior nota"] = max(notas)
aluno["menor nota"] = min(notas)
aluno["sitiuacao"] = situacao

for idex, infos in enumerate(aluno):
    print(infos,":", aluno[infos])