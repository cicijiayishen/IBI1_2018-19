# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:05:01 2019

@author: sissy
"""

from xml.dom.minidom import parse
import  xml.dom.minidom
#import pandas as pd
DOMTree = xml.dom.minidom.parse(r'C:\Users\sissy\Desktop\test Git\IBI1_2018-19\Practical8\go_obo.xml')
collection = DOMTree.documentElement
#<?xml version="1.0" encoding="UTF-8"?>
#df = pd.DataFrame(columns=['id','name','definition','childnodes'])
terms = collection.getElementsByTagName("term")
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    if "autophagosome" in defstr.childNodes[0].data:
        print("*****GO*****")
        id = term.getElementsByTagName('id')[0]
        print('id:',id.childNodes[0].data)
        name = term.getElementsByTagName('name')[0]
        print('name:',name.childNodes[0].data)
        print('definition:',defstr.childNodes[0].data)
        #df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[childnodes]}))