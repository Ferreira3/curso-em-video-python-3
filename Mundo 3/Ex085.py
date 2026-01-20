#Exercício Python 85:
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]

for i in range(7):
    num = int(input(f"Digite o {i+1}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f"Pares: {sorted(lista[0])}")
print(f"Ímpares: {sorted(lista[1])}")
