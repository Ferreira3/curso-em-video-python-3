#Exercício Python 44:
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros

print('='*20)
print('====LOJAS ZEZÃO====')
print('='*20)

valortotal = round(float(input('Valor total das compras: R$')), 2)

print('Qual será a forma de pagamento?' \
'\n[1] à vista dinheiro/pix' \
'\n[2] à vista cartão' \
'\n[3] 2x no cartão' \
'\n[4] 3x ou mais no cartão'
)

formapagamento = int(input('Forma de pagamento: '))

print('O total da sua compra será de: R$', end='')

if formapagamento == 1:
    print(f'{valortotal - (valortotal * 0.10)} com 10% de desconto')
elif formapagamento == 2:
    print(f'{valortotal - (valortotal * 0.05)} com 5% de desconto')
elif formapagamento == 3:
    print(valortotal)
elif formapagamento == 4:
    valorparcelado = valortotal + (valortotal * 0.20)
    print(f'{valorparcelado} com 20% de acréscimo')
    quantparcelas = int(input('Quantas parcelas? '))
    print(f'Você pagará em {quantparcelas}x de R${(valorparcelado/quantparcelas)}')
else:
    print('Opção inválida!')
