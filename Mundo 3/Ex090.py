#Exercício Python 90:
#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

dicionario = {}

dicionario["aluno"] = aluno = str(input("Nome do aluno: ")).capitalize()
dicionario["média"] = media = float(input("Média do aluno: "))
if media >=  7:
    dicionario["situação"] = "Aprovado"
elif media < 5:
    dicionario["situação"] = "Reprovado"
else:
    dicionario["situação"] = "Recuperação"

for k, v in dicionario.items():
    print(f"- {k}: {v}")
