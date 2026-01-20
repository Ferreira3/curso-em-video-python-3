#Exercício Python 61:
#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('====== 10 TERMOS DE UMA PA ======')

primtermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termoatual = primtermo
cont = 1

while cont <= 10:
    print(termoatual,end=' > ')
    termoatual += razao
    cont += 1
    
print('FIM!')
