#Exercício Python 42:
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print('É possível formar um triângulo!')
    if l1 == l2 == l3:
        print('Será um triângulo equilátero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Será um triângulo isósceles!')
    else:
        print('Será um triângulo escaleno!')
else:
    print('Não é possível formar um triângulo!')
