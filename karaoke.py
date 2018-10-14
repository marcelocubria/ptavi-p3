#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except FileNotFoundError:
        print("Usage: python3 karaoke.py file.smil")
    print(len(sHandler.tag_list))
    for index, etiqueta in enumerate(sHandler.tag_list):
        if etiqueta in sHandler.tags and sHandler.tag_list[index+1] == sHandler.tags[etiqueta][0]:
            linea = sHandler.tag_list[index] + "\t"
            for index2, atributo in enumerate(sHandler.tags[etiqueta]):
                linea += sHandler.tag_list[index+1+index2*2] + "="
                linea += sHandler.tag_list[index+2+index2*2] + "\t"
            print(linea)
