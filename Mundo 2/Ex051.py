#Exercício Python 51:
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print('====== 10 TERMOS DE UMA PA ======')

primtermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
dectermo = primtermo + (10) * razao

for i in range(primtermo, dectermo, razao):
    print(i,end=' > ')

print('FIM!')
