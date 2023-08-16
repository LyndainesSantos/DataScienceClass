def operacao(n1, n2):
    while True:
        op = input("Escolha a opção: ")
        if(op == "+"):
            print(soma(n1, n2))
        elif(op == "-"):
            print(subtracao(n1, n2))
        elif(op == "*"):
            print(multiplicacao(n1, n2))
        elif(op == "/"):
            print(divisao(n1, n2))
        else:
            print(print("Operação Inválida"))
            continue
        break

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "O divisor deve ser diferente de Zero!"

def teste():

    print("Menu: \n"
          "+ : Soma\n"
          "- : Subtração\n"
          "* : Multiplicação\n"
          "/ : Divisão\n")

    numero1 = float(input("Informe um número: "))
    numero_2 = float(input("Informe um número: "))

    operacao(numero1, numero_2)

if __name__ == '__main__':
    teste()