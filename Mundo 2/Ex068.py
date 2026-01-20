#Exercício Python 68:
#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

wincounter = 0

print("=" * 15)
print("PAR OU ÍMPAR")
print("=" * 15)

while True:
    numpc = randint(0, 10)
    numuser = int(input("Digite um número: "))
    userchoice = str(input("Par ou Ímpar?[P/I] ")).lower().strip()[0]

    if "p" in userchoice:
        if (numpc + numuser) % 2 == 0:
            print(f"Você escolheu {numuser} e o computador escolheu {numpc}, somando {numuser + numpc}. VOCÊ VENCEU!")
            wincounter += 1
        else:
            print(f"Você escolheu {numuser} e o computador escolheu {numpc}, somando {numuser + numpc}. VOCÊ PERDEU!")
            break
    elif "i" in userchoice:
        if (numpc + numuser) % 2 != 0:
            print(f"Você escolheu {numuser} e o computador escolheu {numpc}, somando {numuser + numpc}. VOCÊ VENCEU!")
            wincounter += 1
        else:
            print(f"Você escolheu {numuser} e o computador escolheu {numpc}, somando {numuser + numpc}. VOCÊ PERDEU!")
            break
    else:
        print("Opção inválida!")
        continue

print(f"GAME OVER! Você venceu um total de {wincounter} rodada(s)!")
