#Exercício Python 43:
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Peso da pessoa(kg): '))
altura = float(input('Altura da pessoa(m): '))
imc = round(peso / (altura ** 2), 2)

print(f'O seu IMC é de {imc}kg/m². Você está em: ', end='')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
