# Desafio 18
from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    # Método para analisar a quantidade de carne necessária e valor total do churrasco e valor individual por pessoa
    def analisar(self):
        consumo_padrao = 0.4  # 400g por pessoa
        valor_carne = 82.40  # R$82,40 por kg
        quant_recomend = consumo_padrao * self.quant
        custo_total = valor_carne * quant_recomend
        custo_individual = custo_total / self.quant

        tbl_analise = Panel(f'''
        Analisando {self.titulo} com {self.quant} convidados
        Cada participante comerá {consumo_padrao}Kg, Cada Kg custa {valor_carne}
        Recomendo comprar {quant_recomend}Kg de carne
        Valor total: {custo_total}
        Valor individual: {custo_individual}
        '''
        , title=self.titulo, width=70,
        )
        
        print(tbl_analise)

churras1 = Churrasco("Churras dos Brothers", 15)
churras1.analisar()
