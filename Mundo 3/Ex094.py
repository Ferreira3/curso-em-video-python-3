#Exercício Python 94:
#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

pessoas = {}
lista = []
somaidade = contacima = contmulher = 0

while True:
    pessoas["nome"] = str(input("Nome: ")).strip().capitalize()
    while True:
        pessoas["sexo"] = str(input("Sexo[M/F]: ")).strip().lower()[0]
        if pessoas["sexo"] in "mf":
            break
        print("ERRO! Digite apenas M ou F!")
    pessoas["idade"] = int(input("Idade: "))
    somaidade += pessoas["idade"]
    lista.append(pessoas.copy())
    while True:
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
        if continuar in "sn":
            break
        print("ERRO! Digite apenas S ou N!")
    if "n" in continuar:
        break

print("-" * 40)
print(f"Quantidade de pessoas cadastradas: {len(lista)}")
print(f"\nMédia de idade: {somaidade / len(lista):.2f}")

print("\nMulheres cadastradas:")
for p in lista:
    if p["sexo"] in "f":
        print(f"{p["nome"]}")
        contmulher += 1
if contmulher == 0:
    print("Nenhuma mulher cadastrada")

print("\nPessoas com idade acima da média: ")
for p in lista:
    if p["idade"] > somaidade / len(lista):
        print(f"{p["nome"]} com {p["idade"]} anos")
        contacima += 1
if contacima == 0:
    print("Nenhuma pessoa com idade acima de média")
print("-" * 40)
