#Exercício Python 70:
#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

from os import system

totalcompra = maiorde1k = valormaisbarato = maisbarato = 0

while True:
    print("---CADASTRAR NOVO PRODUTO---")
    nomeproduto = str(input("Nome do produto: "))
    valorproduto = float(input("Valor do produto: R$"))
    totalcompra += valorproduto

    if totalcompra == valorproduto or valorproduto < valormaisbarato:
        valormaisbarato = valorproduto
        maisbarato = nomeproduto
    if valorproduto > 1000:
        maiorde1k += 1
    
    continuar = ' '
    while continuar not in "sn":
        continuar = str(input("Deseja continuar?[S/N]")).strip().lower()[0]
    if "n" in continuar:
        break
    
system("cls")
print("FIM DOS CADASTROS!")
print(f"Total da compra: R${totalcompra:.2f}\n"
      f"Produtos acima de R$1.000,00: {maiorde1k}\n"
      f"O produto mais barato foi {maisbarato}, custando R${valormaisbarato:.2f}!")
