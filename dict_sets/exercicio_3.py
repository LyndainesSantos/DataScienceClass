# Refaça o programa anterior e imprima a lista dos alunos aprovados em ordem decrescente da maior média para a menor

def calcular_media(notas):
    return sum(notas) / len(notas)

def obter_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    alunos = []

    num_alunos = int(input("Digite o número de alunos a serem registrados: "))

    for _ in range(num_alunos):
        nome_aluno = input("\nDigite o nome do aluno: ")

        notas_aluno = []
        for i in range(4):
            nota = float(input(f"Digite a nota {i+1}: "))
            notas_aluno.append(nota)

        media_aluno = calcular_media(notas_aluno)

        informacoes_aluno = {
            "Nome": nome_aluno,
            "Notas": notas_aluno,
            "Maior Nota": max(notas_aluno),
            "Menor Nota": min(notas_aluno),
            "Média": media_aluno,
            "Situação": obter_situacao(media_aluno)
        }

        alunos.append(informacoes_aluno)

    alunos_aprovados = [aluno for aluno in alunos if aluno["Situação"] == "Aprovado"]
    alunos_aprovados = sorted(alunos_aprovados, key=lambda x: x["Média"], reverse=True)

    print("\nLista de Alunos Aprovados (em ordem decrescente de média):")
    for idx, aluno in enumerate(alunos_aprovados, start=1):
        print(f"{idx}. Nome: {aluno['Nome']}, Média: {aluno['Média']}")

if __name__ == "__main__":
    main()