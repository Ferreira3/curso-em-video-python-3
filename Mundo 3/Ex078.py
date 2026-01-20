#Exercício Python 78:
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

print(f"\nO menor número da lista: {min(lista)} | Posições: ", end='')
for pos, numeros in enumerate(lista):
    if numeros == min(lista):
        print(f"{pos}",end='... ')

print(f"\nO maior número da lista: {max(lista)} | Posições: ", end='')
for pos, numeros in enumerate(lista):
    if numeros == max(lista):
        print(f"{pos}",end='... ')

print("\nFIM!")
