#Exercício Python 22:
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
nomeseparado = nome.split()

print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(' ', ''))} letras!')
print(f'Seu primeiro nome é {nomeseparado[0]} e ele tem {len(nomeseparado[0])} letras!')
