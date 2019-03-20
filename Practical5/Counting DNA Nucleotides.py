# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:04:47 2019

@author: sissy
"""

DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
DNA=list(DNA)
myDict = {}
for word in DNA:
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1
myDict

A=myDict['A']
T=myDict['T']
G=myDict['G']
C=myDict['C']
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
import matplotlib.pyplot as plt
labels = 'A', 'T', 'G', 'C'
sizes = [A, T, G, C]
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()