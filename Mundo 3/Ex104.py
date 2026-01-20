#Exercício Python 104:
#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
#só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(txt):
    x = input(txt)
    while not x or x.isnumeric() == False:
        print("ERRO! Digite um número inteiro válido.")
        x = input(txt)
    return int(x)


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
