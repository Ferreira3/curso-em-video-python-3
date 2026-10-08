# Desafio 38

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R${self.preco:.2f})"


class Carrinho():
    def __init__(self):
        self.produtos = list()
    
    def total(self):
        total = 0

        print('-' * 25)
        for p in self.produtos:
            print(f"{p[0]}\t\tR${p[1]:.2f}")
            total += p[1]
        print('-' * 25)

        return f"    Total: R${total:.2f}"

    def __add__(self, outro: Produto|Carrinho):
        if isinstance(outro, Produto):
            self.produtos.append([outro.nome, outro.preco])
        elif isinstance(outro, Carrinho):
            self.produtos += outro.produtos
        else:
            raise TypeError('Formato não suportado')
        
        return self


p1 = Produto('Mouse', 350)
p2 = Produto('Teclado', 250)
p3 = Produto('Headset', 750)
p4 = Produto('Monitor', 1250)

c1 = Carrinho()
c2 = Carrinho()

c1 = c1 + p1 + p2
c2 = c2 + p3
print(c1.total())
print(c2.total())
c1 = c1 + c2
print(c1.total())
