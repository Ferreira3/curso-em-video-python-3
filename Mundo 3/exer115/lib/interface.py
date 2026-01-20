def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("Erro! Digite um número inteiro válido.")
            continue
        else:
            return num


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc


def abrirArquivo(nome):
    try:
        with open(nome, 'x') as arquivo:
            print("Lista criada!")
    except:
        with open(nome, 'r') as arquivo:
            print("Lista aberta!")


def lerArquivo(nome):
        cabecalho("LISTA DE PESSOAS")
        with open(nome, 'rt+') as arquivo:
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace("\n", "")
                print(f"{dado[0]}\t{dado[1]} anos")


def cadastrarPessoa(arquivo):
    cabecalho("CADASTRAR NOVA PESSOA")
    with open('arquivo.txt', 'at') as arquivo:
        novapessoa = "\n"+str(input("Digite o nome: ")).strip().title()
        novapessoa += ";"+str(leiaInt("Digite a idade: "))
        arquivo.write(novapessoa)
