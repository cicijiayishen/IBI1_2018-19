# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:05:01 2019

@author: cici
Practical 8: Working with information
"""
import xml.dom.minidom
import re
import pandas as pd

filePath=input('Please input your file path:')#Your file path
fileName='go_obo.xml';
resName='autophagosome.xlsx'
file=filePath+'/'+fileName
res=filePath+'/'+resName

re_immu = re.compile(r'autophagosome')
#Function to find childnodes 
def Child(id, resultSet):
    for t in go:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid, resultSet)
                
#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])

#create the DOM tree    
DOMTree = xml.dom.minidom.parse(filePath) 
obo = DOMTree.documentElement
go = obo.getElementsByTagName('term')
for term in go:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_immu.search(defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        resultSet = set()
        Child(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]})) 
        print(id, len(resultSet))

#save to excel
df.to_excel(res,index=False)