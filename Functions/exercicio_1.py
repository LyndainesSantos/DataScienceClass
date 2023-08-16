# IMC = peso / altura ** 2 Crie uma função para calcular o IMC de 4 pessoas.
# Atenção: Use as seguintes estruturas: -laço de repetição. -listas

def calcular_imc(p,h):

    return p / (h**2)

def main(n_pessoas):
    lista_imc = []
    for i in range(n_pessoas):
        nome = input("Informe seu nome: ")
        peso = float(input("Digite o seu peso: "))
        altura = float(input("Informe a sua altura: "))

        imc = calcular_imc(peso, altura)
        lista_imc.append((nome, imc))

    return lista_imc

if __name__ == '__main__':

    lista = main(2)

    for nome, imc in lista:
        print(f'{nome.capitalize()} possui IMC = {imc}')