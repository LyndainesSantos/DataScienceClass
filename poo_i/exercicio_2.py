# Crie uma classe chamada ContaBancaria com atributos como número da conta e saldo. Implemente métodos para depositar e
# sacar dinheiro da conta, bem como para verificar o saldo atual.

class ContaBancaria:
    def __init__(self, n_conta, valor_saldo=0):
        self.numero = n_conta
        self.saldo = valor_saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
