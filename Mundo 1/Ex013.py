#Exercício Python 13:
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário? R$'))
novosalario = salario + (salario * 0.15)

print(f'O novo salário do funcionário com ajuste de 15% será de: R${novosalario:.2f}!')
