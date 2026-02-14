# Desafio 19

class Livro:
    
    pagina_atual = 1
    
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
    
    # Método para avançar páginas do livro
    def avancar_paginas(self, quant):
        if (Livro.pagina_atual + quant) <= self.paginas:
            Livro.pagina_atual += quant
            print(f"Avançando {quant} páginas...\nVocê chegou na página {Livro.pagina_atual}")
        else:
            print(f"Avançando {self.paginas - Livro.pagina_atual} páginas...")
            Livro.pagina_atual = self.paginas
            print(f"Você chegou na página {Livro.pagina_atual}, este é o fim do livro.")

livro1 = Livro("10 Coisas que aprendi", 20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(100)
