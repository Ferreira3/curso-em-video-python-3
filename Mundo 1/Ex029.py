#Exercício Python 29:
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

print('RADAR ELETRÔNICO')
velocidade = int(input('Qual foi a velocidade do carro no radar? '))
valormulta = (velocidade - 80) * 7 #Cálculo do valor da multa
print('Analisando a velocidade...')
sleep(3)

if velocidade > 80:
    print(f'Você excedeu o limite permitido da via e foi multado no valor de R${valormulta}!')
else:
    print('Velocidade dentro do limite permitido da via. Não houve multa!')
