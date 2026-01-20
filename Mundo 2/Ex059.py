#Exercício Python 059:
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#O programa deverá realizar a operação solicitada em cada caso.

from time import sleep

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
saida = False

while saida is False:
    sleep(1)
    print('Qual operação deseja realizar com os valores?')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior valor\n[ 4 ] Digitar Novos números\n[ 5 ] Sair do programa')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print(f'A soma de {valor1} e {valor2} é {valor1 + valor2}!')
    elif opcao == 2:
        print(f'A multiplicação de {valor1} e {valor2} é {valor1 * valor2}!')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}!')
        elif valor2 > valor1:
            print(f'O maior valor é {valor2}!')
        else:
            print('Os valores são iguais!')
    elif opcao == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        saida = True
    else:
        print('Opção inválida! Tente novamente!')

print('FIM!')
