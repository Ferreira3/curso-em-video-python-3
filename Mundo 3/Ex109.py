#Exercício Python 109:
#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from exer109 import moeda

preço = float(input("Digite o preço: R$"))

print(f"A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}!")
print(f"O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}!")
print(f"Aumentando 10% de {moeda.moeda(preço)}, temos {moeda.aumentar(preço, 10, True)}!")
print(f"Diminuindo 10% de {moeda.moeda(preço)}, temos {moeda.diminuir(preço, 10, True)}!")
