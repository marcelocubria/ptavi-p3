#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.tag_list = []
        self.rootlayout = ["width", "height", "background-color"]
        self.region = ["id", "top", "bottom", "left", "right"]
        self.img = ["src", "region", "begin", "dur"]
        self.audio = ["src", "begin", "dur"]
        self.textstream = ["src", "region"]
        self.tags = {'root-layout': self.rootlayout, 'region': self.region}
        self.tags['img'] = self.img
        self.tags['audio'] = self.audio
        self.tags['textstream'] = self.textstream

    def startElement(self, name, attrs):
        if name in self.tags:
            self.tag_list.append(name)
            for atributo in self.tags[name]:
                self.tag_list.append(atributo)
                if attrs.get(atributo, "") != "":
                    self.tag_list.append(attrs.get(atributo, ""))
                else:
                    self.tag_list.append("atributo vacio")

    def get_tags(self):
        return self.tag_list

if __name__ == "__main__":
    parser = make_parser()
    SMILHandler = SmallSMILHandler()
    parser.setContentHandler(SMILHandler)
    parser.parse(open('karaoke.smil'))
    print(SMILHandler.get_tags())
