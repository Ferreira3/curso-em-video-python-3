#Exercício Python 101:
#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anoNasc):
    from datetime import date
    idade = date.today().year - anoNasc
    if 70 >= idade >= 18:
        return f"Com {idade} anos o voto é obrigatório"
    elif 17 >= idade >= 16 or idade > 70:
        return f"Com {idade} anos o voto é opcional"
    else:
        return f"Com {idade} anos o voto é negado"


print("-" * 35)
nasc = int(input("Digite o ano de nascimento: "))
print(f"Situação: {voto(nasc)}")
