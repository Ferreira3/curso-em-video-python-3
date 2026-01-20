#Exercício Python 12:
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorproduto = float(input('Qual o valor do produto? R$'))
valordesconto = valorproduto * 0.95

print(f'O produto que custava R${valorproduto:.2f}, na promoção com 5% de desconto vai custar R${valordesconto:.2f}!')
