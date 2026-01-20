#Exercício Python 80:
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print("Valor adicionado ao final da lista!")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Valor adicionado na posição {pos}")
                break
            pos += 1

print(f"Lista na ordem: {lista}")
