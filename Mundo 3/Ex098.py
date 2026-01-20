#Exercício Python 98:
#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep


def contador(start, stop, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print("=" * 30)
    print(f"Contando de {start} até {stop} de {step} em {step}.")
    if start > stop:
        for i in range(start, stop-1, -step):
            print(i, end=' ', flush=True)
            sleep(0.3)
    else:
        for i in range(start, stop+1, step):
            print(i,end=' ', flush=True)
            sleep(0.3)
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
start = int(input("Início: "))
stop = int(input("Fim: "))
step = int(input("Passo: "))
contador(start, stop, step)
