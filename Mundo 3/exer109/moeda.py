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
