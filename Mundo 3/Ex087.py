#Exercício Python 87:
# Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

soma = soma3col = maior2linha = 0
matriz = [[[],[],[],],
          [[],[],[],],
          [[],[],[]]]

for i, v in enumerate(matriz):
    for ind, v in enumerate(matriz[i]):
        num = int(input(f"Adicione um valor para [{i}, {ind}]: "))
        matriz[i][ind].append(num)
        if num % 2 == 0:
            soma += num
        if ind == 2:
            soma3col += num
        if i == 1 and ind == 0:
            maior2linha = num
        else:
            if i == 1 and num > maior2linha:
                maior2linha = num

print(f"{"SUA MATRIZ":^15}")
for i in matriz:
    print(i)

print(f"A soma total dos valores pares é {soma}")
print(f"A soma dos valores da teceira coluna é {soma3col}")
print(f"O maior valor da segunda linha é {maior2linha}")
