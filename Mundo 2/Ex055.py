#Exercício Python 55:
#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

menorpeso = 0
maiorpeso = 0

for i in range(1, 6):
    pesoatual = float(input(f'Digite o peso da {i}° pessoa: '))
    if i == 1:
        menorpeso =  pesoatual
        maiorpeso = pesoatual
        
    if pesoatual > maiorpeso:
        maiorpeso = pesoatual

    if pesoatual < menorpeso:
        menorpeso = pesoatual

print(f'O menor peso lido foi {menorpeso:.1f}kg e o maior foi {maiorpeso:.1f}kg!')
