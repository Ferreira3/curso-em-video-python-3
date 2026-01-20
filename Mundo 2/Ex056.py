#Exercício Python 56:
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidades = 0
idademaisvelho = 0
homemaisvelho = ''
contmulhermenos20 = 0

for pessoas in range(1, 5):
    print(f'----{pessoas}° PESSOA----')
    
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidades += idade

    if 'f' in sexo and idade < 20:
        contmulhermenos20 += 1
    if 'm' in sexo and idade > idademaisvelho:
        idademaisvelho = idade
        homemaisvelho = nome

print(f'A média da idade do grupo é de {(somaidades / 4):.1f}!')
print(f'Temos {contmulhermenos20} mulheres com menos de 20 anos!')

if homemaisvelho:
    print(f'O homem mais velho do grupo é {homemaisvelho} com {idademaisvelho} anos!')
else:
    print('Não tivemos nenhum homem no grupo!')
