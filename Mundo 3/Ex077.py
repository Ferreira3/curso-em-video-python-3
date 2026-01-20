#Exercício Python 77:
#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("Joao", "Maria", "Jose",
         "Eduardo", "Alex", "Carlos",
         "Lucas", "Mateus", "Felipe")

for palavra in tupla:
    print(f"\nVogais de {palavra}: ",end='')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra,end='')

print("FIM!")
