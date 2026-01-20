#Exercício Python 53:
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digita uma frase: ')).lower()
frasesemespaco = ''
fraseinvertida = ''

for i in range(len(frase)):
    if frase[i] != ' ':
        frasesemespaco += frase[i]

for i in range(1, len(frasesemespaco)+1):
    fraseinvertida += frasesemespaco[-i]

print(f'O contrário de {frasesemespaco.upper()} é {fraseinvertida.upper()}')

if frasesemespaco == fraseinvertida:
    print(f'A FRASE \"{frase.upper()}\" É UM PALÍNDROMO!')
else:
    print(f'A FRASE \"{frase.upper()}\" NÃO É UM PALÍNDROMO!')
