# Desafio 16

class Funcionario:

    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f"Olá, sou {self.nome} e trabalho como {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}."

# Criando um objeto da classe Funcionario
funcionario1 = Funcionario("Maria", "Recursos Humanos", "Analista de RH")
print(funcionario1.apresentacao())

funcionario2 = Funcionario("João", "Tecnologia da Informação", "Desenvolvedor de Software")
print(funcionario2.apresentacao())
