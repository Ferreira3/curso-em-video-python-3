# Desafio 19

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
    # Método para avançar páginas do livro
    def avancar_paginas(self, quant):
        if (self.pagina_atual + quant) <= self.paginas:
            self.pagina_atual += quant
            print(f"Avançando {quant} páginas...\nVocê chegou na página {self.pagina_atual}")
        else:
            print(f"Avançando {self.paginas - self.pagina_atual} páginas...")
            self.pagina_atual = self.paginas
            print(f"Você chegou na página {self.pagina_atual}, este é o fim do livro.")

livro1 = Livro("10 Coisas que aprendi", 20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(100)
livro1.avancar_paginas(5)
