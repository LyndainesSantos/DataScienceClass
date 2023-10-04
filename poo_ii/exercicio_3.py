class SistemaBancario:
    def __init__(self, identificador, titular, saldo=0):
        self.identificador = identificador
        self.titular = titular
        self.saldo = saldo

    def verificar_informacoes(self):
        return f"Conta - ID: {self.identificador}, Titular: {self.titular}, Saldo: {self.saldo}"

    def deposito(self, valor):
        self.saldo += valor

class ContaCorrente(SistemaBancario):
    def __init__(self, identificador, titular, saldo=0):
        super().__init__(identificador, titular, saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class ContaPoupanca(SistemaBancario):
    def __init__(self, identificador, titular, saldo=0, juros=0.03):
        super().__init__(identificador, titular, saldo)
        self.juros = juros

    def aplicar_juros(self):
        self.saldo += self.saldo * self.juros

conta_corrente = ContaCorrente(1, "João", 1000)
conta_poupanca = ContaPoupanca(2, "Maria", 500)

conta_corrente.deposito(100)
conta_poupanca.deposito(200)

conta_corrente.sacar(300)
conta_poupanca.aplicar_juros()

# Verificar informações das contas
print(conta_corrente.verificar_informacoes())
print(conta_poupanca.verificar_informacoes())