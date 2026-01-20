#Exercício Python 96:
#Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(largura, comprimento):
    total = largura * comprimento
    print(f"O terreno tem uma área de {total:.1f}m²")


print("-" * 30)
print(f"{"Controle de Terrenos":^30}")
print("-" * 30)
larg = float(input("Largura do terreno(m): "))
comp = float(input("Comprimento do terreno(m): "))
área(larg, comp)
