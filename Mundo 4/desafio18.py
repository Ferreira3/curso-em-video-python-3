# Desafio 18

from rich.panel import Panel
from rich import print

class Churrasco:
    
    # Atributos de Classe
    consumo_padrao = 0.4  # 400g por pessoa
    valor_carne = 82.40  # R$82,40 por kg

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    # Método para analisar a quantidade de carne necessária, valor total do churrasco e valor individual por pessoa
    def analisar(self):
        quant_recomend = Churrasco.consumo_padrao * self.quant
        custo_total = Churrasco.valor_carne * quant_recomend
        custo_individual = custo_total / self.quant

        tbl_analise = Panel(f'''
        Analisando {self.titulo} com {self.quant} convidados
        Cada participante comerá {Churrasco.consumo_padrao}Kg, Cada Kg custa R${Churrasco.valor_carne:.2f}
        Recomendo comprar {quant_recomend:.3f}Kg de carne
        Valor total: R${custo_total:.2f}
        Valor individual: R${custo_individual:.2f}
        '''
        , title=self.titulo, width=70,
        )
        
        print(tbl_analise)

churras1 = Churrasco("Churras dos Brothers", 15)
churras1.analisar()
