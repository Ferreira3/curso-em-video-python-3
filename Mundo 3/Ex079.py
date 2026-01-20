#Exercício Python 79:
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input("Digite um valor: "))
    if num in lista:
        print("O valor já existe na lista. Tente outro!")
    else:
        print("Valor adicionado na lista com sucesso!")
        lista.append(num)

    choice = input("Deseja continuar?[S/N] ").strip().lower()[0]
    if "n" in choice:
        break

print(f"Lista em ordem crescente: {sorted(lista)}")
