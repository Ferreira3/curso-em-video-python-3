#Exercício Python 31:
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem em KM: '))

if dist <= 200:
    print(f'O valor da sua passagem é de R${(dist * 0.50):.2f}!')
    print(f'A distância da sua viagem é de {dist}km sendo cobrados R$0,50 por km!')
else:
    print(f'O valor da sua passagem é de R${(dist * 0.45):.2f}!')
    print(f'A distância da sua viagem é de {dist}km sendo cobrados R$0,45 por km!')
