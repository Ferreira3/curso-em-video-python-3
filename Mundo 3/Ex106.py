#Exercício Python 106:
#Faça um mini-sistema que utilize o Interactive Help do Python.
#O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

cores = ("\033[m", # 0 - sem cor
        "\033[1;37;44m", # 1 - branco fundo azul
        "\033[1;34;47m" # 2 - azul fundo branco
        )


def ajuda(cmd):
    titulo(f"Acessando o manual {cmd}", cor=2)
    print(cores[2], end='')
    help(cmd)
    print(cores[0], end='')


def titulo(msg, cor=0):
    print(cores[cor], end='')
    print("-" * (len(msg)+4))
    print(f"  {msg}  ")
    print("-" * (len(msg)+4))
    print(cores[0], end='')

while True:
    titulo("Sistema de Ajuda Python", cor=1)
    resp = str(input("Digite uma função ou biblioteca: ")).strip().lower()
    if resp in "fim":
        break
    else:
        ajuda(resp)
titulo("FIM", cor=1)
