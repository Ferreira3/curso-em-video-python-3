#Exercício Python 62:
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('====== TERMOS DE UMA PA V3.0 ======')

primtermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
termoatual = primtermo
cont = 1
quanttermos = 10
quantmostrados = 0

while quanttermos != 0:
    while cont <= quanttermos:
        print(termoatual,end=' > ')
        termoatual += razao
        cont += 1
        quantmostrados += 1
        
    print('PAUSA',end='\n')
    quanttermos = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 1

print(f'A progressão foi finalizada com {quantmostrados} termos mostrados!')
print('FIM!')
