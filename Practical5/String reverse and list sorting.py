# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:04:34 2019

@author: cici
Practical 5: Working with numbers
"""

#give me a string of words
s=input('Please input a string of words:')
#split s into individual words
s=s.split(' ')
n=0
#creating an empty list

L=[]
#improved loop
for element in s:
    L.append(element[::-1])
#sort the list
L.sort()
#reverse the list
L.reverse()
print(L)