#Exercício Python 69:
#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

from os import system

maioresde18 = quanthomem = menorde20 = 0

while True:
    print("---CADASTRAR NOVA PESSOA---")
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo[M/F]: ")).strip().lower()[0]

    if idade >= 18:
        maioresde18 += 1
    if "m" in sexo:
        quanthomem += 1
    if "f" in sexo and idade < 20:
        #if idade < 20:
            menorde20 += 1
    
    continuar = str(input("Gostaria de continuar?[S/N]")).strip().lower()[0]

    if "n" in continuar:
        break

system("cls")
print("Fim dos cadastros!")
print(f"Maiores de 18: {maioresde18}\n"
    f"Homens cadastrados: {quanthomem}\n"
    f"Mulheres com menos de 20 anos: {menorde20}")
