#Exercício Python 113:
#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("Erro! Digite um número inteiro válido.")
            continue
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print("Erro! Digite um número real válido.")
            continue
        else:
            return num


inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {inteiro} e o real {real}!")
