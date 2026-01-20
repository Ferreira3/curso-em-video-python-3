#Exercício Python 107:
#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use algumas dessas funções.

from exer107 import moeda

preço = float(input("Digite o preço: R$"))

print(f"A metade de R${preço:.2f} é R${moeda.metade(preço):.2f}!")
print(f"O dobro de R${preço:.2f} é R${moeda.dobro(preço):.2f}!")
print(f"Aumentando 10% de R${preço:.2f}, temos R${moeda.aumentar(preço, 10):.2f}!")
print(f"Diminuindo 10% de R${preço:.2f}, temos R${moeda.diminuir(preço, 10):.2f}!")
