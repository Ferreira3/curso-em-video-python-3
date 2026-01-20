#Exercício Python 10:
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n1 = float(input('Quanto dinheiro você tem na carteira? R$'))

print(f'Com R${n1:.2f} você consegue comprar US${n1*0.18:.2f}')
