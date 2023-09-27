class SysInformatica:
    def __init__(self, nome_item, preco_unit, quantiadae_item = 0):
        self.item = nome_item
        self.preco = preco_unit
        self.quantidade = quantiadae_item
        self.fatura = 0.0


    def gerarFatura(self):
        return self.quantidade * self.preco