#Exercício Python 110:
#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from exer110 import moeda

vlr = float(input("Digite um valor para ser analisado: R$"))

moeda.resumo(vlr, 10, 10)
