#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import urllib.request

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    try:
        fichero = open(sys.argv[1])
    except FileNotFoundError:
        print("Usage: python3 karaoke.py file.smil")
    parser.parse(fichero)
    lista = sHandler.get_tags()
    for index, etiqueta in enumerate(lista):
        # comprueba que si src no es etiqueta si no atributo no lo cuente
        if etiqueta in sHandler.tags and lista[index+1] == sHandler.tags[etiqueta][0]:
            linea = lista[index] + "\\t"
            for index2, atributo in enumerate(sHandler.tags[etiqueta]):
                linea += lista[index+1+index2*2] + "="
                linea += lista[index+2+index2*2] + "\\t"
            linea = linea[:-2]
            linea += "\\n"
            print(linea)
        # este if descarga archivos remotos y cambia a local
        if etiqueta == "src":
            link = lista[index + 1]
            if link[0:7] == "http://":
                nombre_archivo = "archivo" + str(index)
                urllib.request.urlretrieve(link, nombre_archivo)
                link = link.split("/")[-1]
                lista[index + 1] = link
