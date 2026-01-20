#Exercício Python 86:
#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[[],[],[],],
          [[],[],[],],
          [[],[],[]]]

for i, v in enumerate(matriz):
    for ind, v in enumerate(matriz[i]):
        num = int(input(f"Adicione um valor para [{i}, {ind}]: "))
        matriz[i][ind].append(num)

print(f"{"SUA MATRIZ":^15}")
for i in matriz:
    print(i)
