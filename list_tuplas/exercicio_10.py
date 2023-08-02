# Construa um algoritmo que leia uma lista de números inteiros do usuário e, em seguida, ordená-la em ordem crescente ou
# decrescente, dependendo da escolha do usuário.
def main():
    numeros = []

    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)

    escolha = input("Deseja ordenar em ordem crescente ou decrescente? (crescente / decrescente): ").lower()

    if escolha == "crescente":
        numeros.sort()
        print("Lista ordenada em ordem crescente:", numeros)
    elif escolha == "decrescente":
        numeros.sort(reverse=True)
        print("Lista ordenada em ordem decrescente:", numeros)
    else:
        print("Opção inválida. Por favor, escolha 'crescente' ou 'decrescente'.")

if __name__ == "__main__":
    main()