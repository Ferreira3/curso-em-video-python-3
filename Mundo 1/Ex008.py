#Exercício Python 8:
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite uma distância em metros: '))

print(f'Essa distância equivale a:\n{n1*1000}mm\n{n1*100}cm\n{n1/1000}km\n')
