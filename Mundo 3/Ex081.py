#Exercício Python 81:
#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()


while True:
    num = lista.append(int(input("Digite um valor: ")))
    choice = input("Deseja continuar?[S/N] ").strip().lower()[0]
    if "n" in choice:
        break

print(f"Ao total foram digitados {len(lista)} números!")
print(f"Lista em ordem decrescente: {sorted(lista, reverse=True)}")
if 5 in lista:
    print("O número 5 aparece na lista!")
else:
    print("O número 5 não aparece na lista!")
