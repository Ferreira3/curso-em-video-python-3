#Exercício Python 84:
#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

listapessoas = []
dados = []

while True:
    dados.append(str(input("Nome: ")).capitalize())
    dados.append(float(input("Peso(kg): ")))
    if len(listapessoas) == 0:
        maisleve = maispesado = dados[1]
    else:
        if dados[1] > maispesado:
            maispesado = dados[1]
        if dados[1] < maisleve:
            maisleve = dados[1]
    listapessoas.append(dados[:])
    dados.clear()
    continuar = input("Deseja continuar?[S/N] ").strip().lower()[0]
    if "n" in continuar:
        break

print(f"Pessoas cadastradas: {len(listapessoas)}")
print(f"O maior peso foi {maispesado}kg. Peso de ",end='')
for p in listapessoas:
    if p[1] == maispesado:
        print(p[0],end='... ')
print(f"\nO menor peso foi {maisleve}kg. Peso de ",end='')
for p in listapessoas:
    if p[1] == maisleve:
        print(p[0],end='... ')
