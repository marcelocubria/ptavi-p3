#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.tag_list = []
        self.rootlayout = ["width", "height"]
        self.region = ["id", "top", "bottom", "left," "right"]
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
                self.tag_list.append(attrs.get(atributo, ""))

    def get_tags(self):
            for tag in self.tag_list:
                print(tag)


parser = make_parser()
cHandler = SmallSMILHandler()
parser.setContentHandler(cHandler)
parser.parse(open('karaoke.smil'))
print(cHandler.tag_list)
