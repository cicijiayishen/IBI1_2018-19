# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:12:42 2019

@author: cici
Practical 13
Advanced Modelling with Copasi and Python

"""

############Running a Copasi model from within Python##########################
import os
import numpy
import matplotlib.pyplot as plt
import re

def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails          
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")      
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()        

xml_to_cps() #It works, creating predator-prey.cps and modelResults.csv

os.system('CopasiSE.exe predator-prey.cps')

#Set the directory
os.chdir("C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical13")

#################Reading and plotting simulation results#######################
csvfile=open('modelResults.csv','r')
result=csvfile.readlines()
list=[]
names=[]
count=0
for line in result:
    if count==0:
        names=re.split(r',+',line)
        count=1
    else:
        l=re.split(r',+',line)
        del(l[0])#delete the first line because it contains names 'A''B'
        list.append(l)
results=numpy.array(list)
results=results.astype(numpy.float)#transform the numbers into actual numbers

#Plot time-population curve
plt.plot(results[:,0],label='Predator (b=0.02, d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1, d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()

#Plot Limit cycle curve
plt.plot(results[:,0],results[:,1])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')
plt.show()

#############Changing values and running the simulation again##################
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse('C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical13/predator-prey.xml')
collection=DOMTree.documentElement
parameters=collection.getElementsByTagName('parameter')
set=[]
for p in parameters:
    print(p.getAttribute('id'),'is',p.getAttribute('value'))
    v=input('Please input a number from 0 to 1 to change the parameter:')
    p.setAttribute('value',v)
    print(p.getAttribute('value'))
xml_to_cps()
#Run the cps file in Copasi
#Get a csv file
#Use the csv file to plot 2 curves

#Running many simulations
#for i in range(0,100)
#do the same thing as 'Changing parameters'