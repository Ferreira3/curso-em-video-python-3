# Desafio 30

from hashlib import sha256
from rich import inspect

class Credencial():
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, nova_senha):
        self.__hash = self._gerar_hash(nova_senha)

    def validar(self, chave):
        return self._gerar_hash(chave) == self.__hash

    def _gerar_hash(self, texto):
        return sha256(texto.encode('utf-8')).hexdigest()


c1 = Credencial()
c1.senha = 'zezao'
inspect(c1, private=True)
print(c1.validar('zezao'))
print(c1.senha)
