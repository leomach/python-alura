from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco, tipo, tamanho):
        self._nome = nome.title()
        self._preco = preco
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} | {self.tipo} | {self._tamanho} | {self._preco}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)