#Exercício Python 88:
#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print(f"{"MEGA SENA":^30}")
print("-" * 30)

lista = []
jogos =  []
num = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(num):
    while len(lista) != 6:
        numrand = randint(1, 60)
        if numrand not in lista:
            lista.append(numrand)
    jogos.append(sorted(lista[:]))
    lista.clear()

for ind, jg in enumerate(jogos):
    print(f"Jogo {ind+1}: {jg}")

print("BOA SORTE!")
