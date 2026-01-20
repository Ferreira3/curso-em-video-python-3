#Exercício Python 14:
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em °C: '))
conversaotemperatura = (temp * 1.8) + 32

print(f'A temperatura de {temp:.1f}°C equivale a {conversaotemperatura:.1f}°F!')
