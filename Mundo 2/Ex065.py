#Exercício Python 65:
#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]')).lower()
cont = 1
soma = num
maior = num
menor = num

while continuar not in 'n':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).lower()
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1

print(f'A média dos valores foi {soma/cont:.2f}.')
print(f'O menor valor foi {menor} e o maior foi {maior}.')
print('FIM!')
