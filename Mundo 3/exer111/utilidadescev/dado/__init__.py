def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).strip().replace(",", ".")
        if not valor or valor.isalpha():
                print(f"\"{valor}\" é um valor inválido!")
        else:
            return float(valor)
