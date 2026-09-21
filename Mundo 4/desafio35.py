# Desafio 35

from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str = None, tamanho:int|float = 0):
        self.nome = nome
        self.tamanho = tamanho / (1024 ** 2)
        self._extensao = self.__class__.__name__.lower()
        self._nome_completo = f"{self.nome}.{self._extensao}"

    @property
    def nome_completo(self):
        return f"'{self._nome_completo}' ({self.tamanho:.1f}MB)"

    @nome_completo.setter
    def nome_completo(self, novo_nome:str = "Arquivo sem nome"):
        self._nome_completo = novo_nome
    
    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def abrir(self):
        return f"Abrindo o arquivo {self.nome_completo} no Adobe Reader"


class DOC(Arquivo):
    def abrir(self):
        return f"Abrindo o arquivo {self.nome_completo} no Microsoft Word"


def abrir_arquivo(obj):
    try:
        print(obj.abrir())
    except:
        print(f"ERRO: Não foi possível abrir o arquivo selecionado")

a1 = DOC('prova', 250000)
a2 = PDF('contrato', 1300000)
a3 = 'Bolo de Goiaba'


abrir_arquivo(a1)
abrir_arquivo(a2)
abrir_arquivo(a3)
