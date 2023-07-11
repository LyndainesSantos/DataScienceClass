# Escreva um algoritmo que solicita ao usuário um número N e imprime os N primeiros termos da sequência de Fibonacci

n = int(input("Digite o número de termos da sequência de Fibonacci: "))

fibonacci = [0, 1]  # Inicializa a lista com os dois primeiros termos

if n <= 0:
    print("Digite um número inteiro positivo.")
elif n == 1:
    print("Sequência de Fibonacci até o", n, "termo:")
    print(fibonacci[0])
else:
    print("Sequência de Fibonacci até o", n, "termo:")
    print(fibonacci[0])
    print(fibonacci[1])
    for i in range(2, n):
        termo = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(termo)
        print(termo)