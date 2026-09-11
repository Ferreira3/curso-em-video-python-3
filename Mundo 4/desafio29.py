# Desafio 29

class Diario():
    def __init__(self, senha='123'):
        self.__senha = senha
        self.__segredos = list()

    def escrever(self, msg='Mensagem vazia'):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida! Você não tem acesso ao diário.')

        return self.__segredos


d1 = Diario('guanabara')

d1.escrever('primeira mensagem')
d1.escrever('curso em vídeo python')
d1.escrever('prof. guanabara')

try:
    mensagens = d1.ler('guanabara1')
    print('Acesso liberado!')
    for s in mensagens:
        print(f"- {s}")
except Exception as erro:
    print(f"ERRO: {erro}")
