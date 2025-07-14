from modelos.avaliacao import avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |  {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao_nova = avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao_nova)
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        total = sum(avaliacao.nota for avaliacao in self._avaliacao)
        return round(total / len(self._avaliacao),1)