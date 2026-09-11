# Desafio 33

from abc import ABC
from rich import inspect
from datetime import datetime

class Pessoa(ABC):

    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_ano:int):
        if self.get_ano_atual() >= novo_ano >= 1920:
            self._nascimento = novo_ano
            return

        raise ValueError('Erro: Ano digitado é inválido')

    @property
    def idade(self):
        ano_atual = self.get_ano_atual()
        return ano_atual - self._nascimento

    def get_ano_atual(self):
        return datetime.now().year

class Aluno(Pessoa):

    cursos = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome:str, nascimento:int, curso:str):
        
        super().__init__(nome, nascimento)

        if curso in self.cursos:
            self._curso = curso
        else:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso: str):
        if novo_curso in self.cursos:
            self._curso = novo_curso
            return
        else:
            raise ValueError(f"O curso {novo_curso} não está na lista de cursos oficiais")

    def add_curso(self, curso: str):
        self.cursos.append(curso)


a1 = Aluno('Maria', 2000, "ADS")
a1.add_curso("MODA")
a1.curso = "MODA"
inspect(a1, methods=True, private=True)
a2 = Aluno('José', 1999, "ADM")
print(a2.cursos)