#Exercício Python 97:
#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
#Ex: escreva(‘Olá, Mundo!’)
#Saída:~~~~~~~~~~
#      Olá, Mundo!
#      ~~~~~~~~~~


def escreva(text):
    text = (f"  {text}  ")
    print("~" * len(text))
    print(text)
    print("~" * len(text))


escreva("Curso em Vídeo")
escreva("Deus é Fiel")
escreva("Python")
escreva("01")
