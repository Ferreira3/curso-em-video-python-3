#Exercício Python 36:
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Em quantas anoss você quer quitar a casa? '))
prestacao = valorcasa / (anos * 12)

if prestacao > (salario * 0.30):
    print(f' EMPRÉSTIMO NEGADO!\nO valor da parcela mensal(R${prestacao:.2f}) excedeu 30% do seu salário(R${(salario * 0.30):.2f}).')
else:
    print(f'EMPRÉSTIMO APROVADO!\nSua parcela mensal ficou no valor de {prestacao:.2f}.')
