#Exercício Python 114:
#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

try:
    requests.get("http://www.pudim.com.br/")
except:
    print("Não consegui acessar o site!")
else:
    print("Consegui acessar o site!")