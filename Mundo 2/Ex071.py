#Exercício Python 071:
#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("----CAIXA ELETRÔNICO----")

cont50 = cont20 = cont10 = cont1 = 0
valor = int(input("Qual valor você deseja sacar?"))

while valor > 0:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20:
        valor -= 20
        cont20 += 1
    elif valor >= 10:
        valor -= 10
        cont10 += 1
    elif valor >= 1:
        valor -= 1
        cont1 += 1

print(f"Total de {cont50} cédulas de R$50\n"
      f"Total de {cont20} cédulas de R$20\n"
      f"Total de {cont10} cédulas de R$10\n"
      f"Total de {cont1} cédulas de R$1\n"
      "Muito obrigado! Tenha um ótimo dia!")
