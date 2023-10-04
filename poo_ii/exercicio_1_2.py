# Considere um sistema de gestão de notas fiscais. Crie uma classe base chamada NotaFiscal com atributos como número da
# nota, data, valor total e uma lista de itens. Em seguida, crie classes derivadas NotaFiscalSimples e NotaFiscalDetalhada.
# A NotaFiscalSimples deve ter um método para calcular o imposto com base no valor total, enquanto NotaFiscalDetalhada deve
# ter métodos para adicionar itens à nota e calcular o imposto.
class NotaFiscal:
    def __init__(self, numero_nota, data, valor_total, lista_itens = []):
        self.numero_nota = numero_nota
        self.data = data
        self.valor_total = valor_total
        self.lista_itens = lista_itens
        self.imposto = 0

class NotaFiscalSimples(NotaFiscal):
    def calcular_imposto(self):
        self.imposto = self.valor_total * 0.1
        return self.imposto

class NotaFiscalDetalhada(NotaFiscal):
    def __init__(self, numero, data, valor_total):
        super().__init__(numero, data, valor_total,[])
    def adicionar_itens(self, item, quantidade, preco_unitario):
        self.lista_itens.append((item, quantidade, preco_unitario))
        return self.lista_itens
    def calcular_imposto(self):
        soma = 0
        for i in self.lista_itens:
            soma += i[1] * i[2]
        self.imposto = soma * 0.15
        return self.imposto

class RelatorioAuditoria:
    def gerar_relatorio(self, notas):
        for nota in notas:
            print(f"Nota Fiscal número {nota.numero_nota} - Data: {nota.data}")
            print(f"Valor total: {nota.valor_total}")
            print(f"Imposto na nota fiscal: {nota.imposto}")
            print("-" * 30)



nota_simples = NotaFiscalSimples(1, "04/10/2023", 1000)
print("Imposto NF Simples: ",nota_simples.calcular_imposto())

nota_detalhada = NotaFiscalDetalhada(2, "04/10/2023", 2000)
nota_detalhada.adicionar_itens("Produto X", 1, 500)
nota_detalhada.adicionar_itens("Produto Y", 2, 100)
nota_detalhada.adicionar_itens("Produto Z", 3, 400)
print("Imposto NF Detalhada: ", nota_detalhada.calcular_imposto())

relatorio = RelatorioAuditoria()
notas_fiscais = [nota_simples, nota_detalhada]
relatorio.gerar_relatorio(notas_fiscais)