#Exercício Python 95:
#Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
listajogadores = []
gols = []

while True:
    jogador["nome"] = str(input("Nome do jogador: ")).strip().title()
    jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    for i in range(jogador["partidas"]):
        gols.append(int(input(f"    Quantos gols na {i+1}º partida: ")))
    jogador["gols"] = gols[:]
    listajogadores.append(jogador.copy())
    gols.clear()
    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]
        if continuar not in "sn":
            print("Erro! Digite apenas S ou N")
        else:
            break
    if continuar in "n":
        break

print("-" * 40)
print(f"{"No.":<5}{"NOME":<15}{"GOLS":<15}{"TOTAL":<15}")
print("-" * 40)
for index, pessoa in enumerate(listajogadores):
    print(f"{index:<5}{pessoa["nome"]:<15}{str(pessoa["gols"]):<15}{sum(pessoa["gols"]):<15}")
while True:
    mostrar = int(input("Mostrar levantamento de qual jogador(999 para parar)? "))
    if mostrar == 999:
        break
    else:
        if mostrar > len(listajogadores):
            print("Jogador não encontrado. Tente novamente!")
        else:
            print(f"Levantamento de {listajogadores[mostrar]["nome"]}:")
            for ind, gols in enumerate(listajogadores[mostrar]["gols"]):
                print(f"- {ind+1}º jogo: fez {gols} gol(s)")

print("FIM!")
