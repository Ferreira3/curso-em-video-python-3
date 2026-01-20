#Exercício Python 82:
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas

lista = list()
listapar = list()
listaimpar = list()

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    choice = input("Deseja continuar?[S/N] ").strip().lower()[0]
    if "n" in choice:
        break

print(f"Lista COMPLETA: {lista}")
print(f"Lista PAR: {listapar}")
print(f"Lista ÍMPAR: {listaimpar}")
