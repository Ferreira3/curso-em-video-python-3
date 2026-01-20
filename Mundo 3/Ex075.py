#Exercício Python 75:
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um valor: "))
num3 = int(input("Digite um valor: "))
num4 = int(input("Digite um valor: "))
nums = (num1, num2, num3, num4)
contpar = 0

print(f"O valor 9 apareceu {nums.count(9)} vezes!")
if 3 in nums:
    print(f"O primeiro valor 3 está na {nums.index(3)+1}ª posição!")
else:
    print("O valor 3 não aparece na tupla!")

for i in nums:
    if i % 2 == 0:
        print(f"({i})",end='')
        contpar += 1
if contpar > 0:
    print(" Foram os números pares")
else:
    print("Não houveram números pares!")

print("FIM!")
