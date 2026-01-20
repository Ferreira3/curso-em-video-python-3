#Exercício Python 040:
#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = round((nota1 + nota2) / 2, 1)

print(f'A média do aluno foi {media}!')

if media >= 7:
    print('ALUNO APROVADO')
elif media < 5:
    print('ALUNO REPROVADO')
else:
    print('ALUNO EM RECUPERAÇÃO')
