# Faça uma função para calcular o valor/hora de um funcionário.
def main():
    horas_mes = int(input("Digite as horas trabalhas: "))
    valor_mes = float(input("Digite o valor recebido por mês: "))

    valor_hora = valor_mes / horas_mes

    return valor_hora

if __name__ == '__main__':

    print("O valor por hora é R$", main())