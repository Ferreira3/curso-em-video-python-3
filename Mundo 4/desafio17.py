# Desafio 17

from rich.panel import Panel
from rich import print

class Produto:
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    # Método para exibir a etiqueta do produto
    def etiqueta(self):
        formated_price = f"R${self.preco:,.2f}"
        print(Panel(f"{self.nome:^30}\n{'.'*30}\n{formated_price:.^30}", title="Produto", width=35))

# Criando objetos da classe Produto
produto1 = Produto("Notebook", 3500.00)
produto1.etiqueta()

produto2 = Produto("Smartphone", 1500.50)
produto2.etiqueta()
