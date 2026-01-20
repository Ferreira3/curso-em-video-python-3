#Exercício Python 49: Refaça o DESAFIO 9,
#mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.

n1 = int(input('Digite um número para obter sua tabuada: '))

for i in range(1, 11):
    print(f'{n1} x {i:2} = {n1*i}')
