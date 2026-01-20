#Exercício Python 15:
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
kmrodado = int(input('Quanto Km rodados? '))
valortotal = (dias * 60)+(kmrodado * 0.15)

print(f'O total a pagar é de R${valortotal:.2f}!')
