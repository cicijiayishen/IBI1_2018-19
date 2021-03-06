# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:04:47 2019

@author: cici
Practical 5: Working with numbers
"""
#give me a sequence of DNA
DNA=input('Please input a DNA sequence:')
#split the sequence into letters
DNA=list(DNA)
#create a dictionary
myDict = {}
for word in DNA:
    #ignore other letters
    if word in ['A','T','G','C']:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
print(myDict)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
import matplotlib.pyplot as plt
labels = myDict.keys()#able to handle when there are other letters
sizes = myDict.values()
explode = [0]*len(labels)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()