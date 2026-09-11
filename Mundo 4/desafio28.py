# Desafio 28

class Termostato():
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp):
        # 1. Valida se o decimal é apenas .0 ou .5
        if temp % 0.5 != 0:
            raise ValueError("A temperatura só pode variar de 0.5 em 0.5.")
        # 2. Valida a faixa entre 16 e 30
        if temp > 30:
            self.__temperatura = 30
        elif temp < 16:
            self.__temperatura = 16
        else:
            self.__temperatura = temp
        
        
        
        self.__temperatura = temp

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"


t1 = Termostato()

try:
    t1.temperatura = 25.5
except Exception as e:
    print(f"Houve um problema: {e}")

print(f"A temperatura atual é de {t1.ftemperatura}")
