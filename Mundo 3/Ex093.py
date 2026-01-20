#Exercício Python 93:
#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador["nome"] = str(input("Nome do jogador: ")).strip().title()
jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
for i in range(jogador["partidas"]):
    gols.append(int(input(f"Quantos gols na {i+1}º partida? ")))
jogador["total"] = sum(gols)
jogador["gols"] = gols

print("-" * 30) # modelo 1
print(jogador)
print("-" * 30)

print("-" * 30) # modelo 2
for k, v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print("-" * 30)

print("-" * 30) # modelo 3
print(f"O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.")
for i in range(jogador["partidas"]):
    print(f"- Na {i+1}º partida marcou {jogador["gols"][i]} gol(s).")
print(f"Somando um total de {jogador["total"]} gol(s)!")
print("-" * 30)
