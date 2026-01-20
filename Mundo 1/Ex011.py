#Exercício Python 11:
#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
quanttinta = area / 2

print(f'A área da sua parede é de {area}m²!')
print(f'Será necessário {quanttinta:.2f}L para pintar a parede!')
