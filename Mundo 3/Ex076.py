#Exercício Python 76:
#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Lápis", "1.50", "Borracha", "2.00",
            "Caderno", "24.99", "Caneta", "2.50",
            "Régua", "3.00", "Estojo", "5.00",
            "Livro Matemática", "49.90", "Pacote fol. A4", "35.00")

print("-" * 37)
print(f"{"LISTAGEM DE PREÇOS":^37}")
print("-" * 37)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f"{produtos[i]:.<25}.....R${produtos[i+1]:>5}")

print("-" * 37)
