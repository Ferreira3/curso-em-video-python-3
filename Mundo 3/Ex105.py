#Exercício Python 105:
#Faça um programa que tenha uma função notas() que pode receber várias notas
#de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)


def notas(*notas, sit=False):
    """
    ->Analisa notas e situações de alunos.
    :param notas: Recebe uma quantidade (n) de notas.
    :param sit: (opcional) Exibe a situação da média das notas.
    :return: Dicionário com o total, maior, menor e média das notas recebidas.
    """
    notasDict = {}
    notasDict["total"] = len(notas)
    notasDict["maior"] = max(notas)
    notasDict["menor"] = min(notas)
    notasDict["média"] = sum(notas) / len(notas)
    if sit == True:
        if notasDict["média"] >= 7:
            notasDict["situação"] = "BOA"
        elif notasDict["média"] >= 5:
            notasDict["situação"] = "RAZOÁVEL"
        else:
            notasDict["situação"] = "RUIM"
    return notasDict


x = notas(2.5, 5.5, 1.5, sit=True)
print(x)
