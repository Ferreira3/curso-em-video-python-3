# Desafio 32

from rich import inspect
import hashlib
import stdiomask

class ContaBancaria():
    def __init__(self, id, titular, saldo, chave=0):
        print('Criando a conta...')
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        if chave == 0:
            chave = stdiomask.getpass(prompt="Senha: ", mask="*")
        self.__hash = self._gerar_hash(chave)
        print(f'Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:.2f}')

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome):
        if self.validar_senha():
            self._titular = novo_nome
            print('Nome alterado com sucesso!')
        else:
            print('Senha não confere. Alteração não realizada!')

    def validar_senha(self):
        chave = stdiomask.getpass(prompt="Senha: ", mask="*")
        return self._gerar_hash(chave) == self.__hash

    def sacar(self, valor):
        if not self.validar_senha():
            return 'Senha não confere. Saque não autorizado!'
        if valor > self.__saldo:
            return 'Saldo insuficiente. Saque não autorizado!'
        
        self.__saldo -= valor
        return f'Saque de R${valor:.2f} realizado com sucesso!'
            
    def pede_senha(self):
        return self.__hash
    
    def depositar(self, valor):
        if valor < 0:
            return f'Erro! Valor de depósito inválido.'

        self.__saldo += valor
        return f'Depósito de {valor} realizado com sucesso!'

    def _gerar_hash(self, texto):
        return hashlib.sha256(texto.encode()).hexdigest()


c1 = ContaBancaria(123, 'Eduardo', 1000, 'pythonpoo')
print(c1.validar_senha())
print(c1.sacar(500))
c1.nome = 'Joao'
inspect(c1, private=True, methods=True)
