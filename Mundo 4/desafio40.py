# Desafio 40

import json
import xml.etree.ElementTree as ET

class Aluno():
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario():
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class toJSON():
    def exportar(self, dados):
        dicionario = [d.__dict__ for d in dados]

        return json.dumps(dicionario, indent=2, ensure_ascii=False)


class toXML():
    def exportar(self, dados):
        raiz = ET.Element("dados")
        lista_dicionarios = [d.__dict__ for d in dados]
        
        for item in lista_dicionarios:
            elemento_item = ET.SubElement(raiz, "item")
            
            for chave, valor in item.items():
                sub_elemento = ET.SubElement(elemento_item, chave)
                sub_elemento.text = str(valor)
        
        ET.indent(raiz, space="    ")
        return ET.tostring(raiz, encoding="utf-8").decode("utf-8")


def exportar_dados(formato, pessoas):
        try:
            print(formato.exportar(pessoas))
        except Exception as e:
            print(e)


alunos = [
    Aluno("José", "ADS", "2 per"),
    Aluno("Maria", "ENF", "1 per"),
    Aluno("Everton", "SPI", "4 per")
]

usuarios = [
    Usuario("João", "joao@gmail.com"),
    Usuario("Marina", "marina@hotmail.com"),
    Usuario("Enzo", "enzo@outlook.com")
]

exportar_dados(toJSON(), alunos)
exportar_dados(toXML(), alunos)
exportar_dados(toJSON(), usuarios)
exportar_dados(toXML(), usuarios)
