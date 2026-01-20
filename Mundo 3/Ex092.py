#Exercício Python 92:
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
pessoa = {}
anoatual = date.today().year

print("---CARTEIRA DE TRABALHO---")
pessoa["nome"] = str(input("Nome: ")).strip().title()
pessoa["idade"] = anoatual - int(input("Ano de nascimento: "))
pessoa["ctps"] = int(input("Carteira de trabalho(0 não tem): "))

if pessoa["ctps"] == 0:
    for k, v in pessoa.items():
        print(f"- {k} tem o valor {v}")
else:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salário"] = int(input("Salário: R$"))
    pessoa["aposentadoria"] = (35 - (anoatual - pessoa["contratação"])) + pessoa["idade"]
    for k, v in pessoa.items():
        print(f"- {k} tem o valor {v}")

print("FIM!")
