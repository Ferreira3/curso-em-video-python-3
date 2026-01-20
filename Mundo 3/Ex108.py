#Exercício Python 108:
#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from exer108 import moeda

preço = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}!")
print(f"O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}!")
print(f"Aumentando 10% de {moeda.moeda(preço)}, temos {moeda.moeda(moeda.aumentar(preço, 10))}!")
print(f"Diminuindo 10% de {moeda.moeda(preço)}, temos {moeda.moeda(moeda.diminuir(preço, 10))}!")
