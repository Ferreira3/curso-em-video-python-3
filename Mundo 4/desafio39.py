# Desafio 39

from abc import ABC
import re
from rich import print

#Regras:
    # 1. VALIDAÇÃO DE NOME DE USUÁRIO
    # Padrão: 5 a 20 caracteres, apenas minúsculas, números e sublinhado (_).

    # 2. VALIDAÇÃO DE SENHA FORTE
    # Padrão: Mínimo de 8 caracteres, pelo menos 1 letra maiúscula e pelo menos 1 símbolo.
    
    # 3. VALIDAÇÃO DE E-MAIL
    # Padrão: 1 arroba (@), aceita letras/números/símbolos comuns e TLD final com 2 ou mais letras.


class Validador(ABC):
    padrao = ''

    def validar(self, valor):
        if re.match(self.padrao, valor):
            return True
        return False


class Usuario(Validador):
    padrao = r"^[a-z0-9_]{5,20}$"


class Senha(Validador):
    padrao = r"^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?\":{}|<>_+\-\[\]\\\/]).{8,}$"


class Email(Validador):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def validar_dado(tipo:Validador, valor:str):
    try:
       resultado = tipo.validar(valor)
       print(f"Valor: '{valor}' é um(a) {tipo.__class__.__name__} válido?", end=' ')
       print("[bold black on green]SIM[/]" if resultado else "[bold white on red]NÃO[/]")
    except Exception as e:
       print(f'Não foi possível validar este tipo! ERRO: {e}')
       

testes_usuario = [
    "user_123",  # Válido (letras, números, _, tamanho 8)
    "admin",  # Válido (letras, tamanho 5)
    "abc",  # Inválido (muito curto, tamanho 3)
    "usuario_com_nome_muito_longo",  # Inválido (muito longo, tamanho 28)
    "User123",  # Inválido (contém letra maiúscula)
    "user-123",  # Inválido (contém hífen, apenas sublinhado é permitido)
]

testes_senha = [
    "Ab1#cdef",       # Válido (8 chars, 1 maiúscula, 1 símbolo)
    "SenhaMuitoLonga123!", # Válido (mais de 8 chars, maiúscula e símbolo)
    "senha123!",      # Inválido (sem maiúscula)
    "SENHA123!",      # Válido (mais de 8 chars, maiúscula e símbolo)
    "Senha12345",     # Inválido (sem símbolo)
    "Ab1!",           # Inválido (muito curta, apenas 4 chars)
]

testes_email = [
    "usuario@email.com",      # Válido (padrão comum)
    "user.name+tag@domain.co",# Válido (com símbolos permitidos e TLD de 2 letras)
    "jose@empresa.com.br",    # Válido (múltiplos pontos no domínio)
    "usuario@email",          # Inválido (sem TLD)
    "usuario@email.c",        # Inválido (TLD com apenas 1 letra)
    "usuarioemail.com",       # Inválido (sem arroba)
    "usuario@br@email.com",   # Inválido (mais de um arroba)
]

for t in testes_usuario:
    validar_dado(Usuario(), t)

for t in testes_senha:
    validar_dado(Senha(), t)

for t in testes_email:
    validar_dado(Email(), t)
