#Exercício Python 57:
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F] ')).lower().strip()

while sexo not in 'mf':
    sexo = str(input('Dados inválidos! Digite novamente: ')).lower().strip()

if 'm' in sexo:
    print('Você é do sexo masculino!')
else:
    print('Você é do sexo feminino!')
