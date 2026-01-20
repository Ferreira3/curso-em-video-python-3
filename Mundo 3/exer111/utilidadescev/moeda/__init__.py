def aumentar(n, taxa, format=False):
    result = n + (n * taxa/100)
    return result if not format else moeda(result)


def diminuir(n, taxa, format=False):
    result = n - (n * taxa/100)
    return result if not format else moeda(result)


def dobro(n, format=False):
    result = n * 2
    return result if not format else moeda(result)


def metade(n, format=False):
    result = n / 2
    return result if not format else moeda(result)


def moeda(n):
    return f"R${n:.2f}"


def resumo(valor, aumen, desc):
    print("-" * 35)
    print(f"{"RESUMO DO VALOR":^35}")
    print("-" * 35)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"Acréscimo de {aumen}%: \t{aumentar(valor, aumen, True)}")
    print(f"Desconto de {desc}%: \t{diminuir(valor, desc, True)}")
    print("-" * 35)
