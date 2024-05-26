from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
    def alternar_ativo(self):
        self._ativo = not self._ativo
        print(f'O restaurante {self._nome} foi {self.ativo}.')

    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print('Nota inválida.')

    @property
    def media_avaliacao(self):
        if len(self._avaliacao) > 0:
            soma = 0
            for avaliacao in self._avaliacao:
                soma += avaliacao._nota
            media = soma / len(self._avaliacao)
            return round(media, 1)
        else:
            return '-'
        

    def adicionar_no_cardapio(self, item):
         if isinstance(item, ItemCardapio):
              self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. {item._nome} | R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            elif hasattr(item, '_tipo'):
                mensagem_sobremesa = f'{i}. {item._nome} | Tipo: {item._tipo} | R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_sobremesa)
            else:
                mensagem_bebida = f'{i}. {item._nome} | R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)

