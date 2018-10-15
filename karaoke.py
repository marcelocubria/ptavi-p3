#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import urllib.request
import json


class KaraokeLocal():

    def __init__(self, fichero):
        self.parser = make_parser()
        self.sHandler = SmallSMILHandler()
        self.parser.setContentHandler(self.sHandler)
        self.parser.parse(fichero)
        self.lista = self.sHandler.get_tags()

    def __str__(self):
        self.linea_total = ""
        for index, etiqueta in enumerate(self.lista):
            # comprueba que si src no es etiqueta si no atributo no lo cuente
            if etiqueta in self.sHandler.tags:
                if self.lista[index+1] == self.sHandler.tags[etiqueta][0]:
                    linea = self.lista[index] + "\\t"
                    for indx2, atr in enumerate(self.sHandler.tags[etiqueta]):
                        linea += self.lista[index+1+indx2*2] + "="
                        linea += self.lista[index+2+indx2*2] + "\\t"
                    linea = linea[:-2]
                    linea += "\\n"
                    self.linea_total += linea + "\n"
        return self.linea_total

    def do_local(self):
        for index, etiqueta in enumerate(self.lista):
            if etiqueta == "src":
                link = self.lista[index + 1]
                if link[0:7] == "http://":
                    nombre_archivo = "archivo" + str(index)
                    urllib.request.urlretrieve(link, nombre_archivo)
                    link = link.split("/")[-1]
                    self.lista[index + 1] = link

    def to_json(self, fichero_smil, nombre_json="mismo"):
        if nombre_json == "mismo":
            nombre_json = fichero_smil.split('.')[0] + '.json'
        json.dump(self.lista, open(nombre_json, 'w'))


if __name__ == "__main__":
    try:
        fichero = open(sys.argv[1])
        mi_karaoke = KaraokeLocal(fichero)
        print(mi_karaoke.__str__())
        mi_karaoke.to_json(sys.argv[1])
        mi_karaoke.do_local()
        mi_karaoke.to_json(sys.argv[1], "local.json")
        print(mi_karaoke.__str__())
    except FileNotFoundError:
        print("Usage: python3 karaoke.py file.smil, file not found")
    except IndexError:
        print("Usage: python3 karaoke.py file.smil, index error")
