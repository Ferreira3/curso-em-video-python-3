#Exercício Python 102:
#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    ->Calcula o fatorial de um número.
    :param num: Número que será calculado.
    :param show: (opcional) Decidir se o cáculo será ou não mostrado.
    :return: O valor fatorial de num.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show and i > 1:
                print(i,end=' ')
                print("x",end=' ')
        if show and i == 1:
            print(i,"=",end=' ')
    return f


print(fatorial(5, True))
help(fatorial)
