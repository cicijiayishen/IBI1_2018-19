# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:04:34 2019

@author: sissy
"""

#give me a string of words
s="but soft what light in yonder window breaks"
#split s into individual words
s=s.split(' ')
n=0
#creating an empty list
L=[]
while 1==1:
    sn=s[n]
    #split the word into individual letters
    ln=list(sn)
    #reverse the letters
    ln.reverse()
    #join the reversed letters into words
    jn=''.join(ln)
    #add into the list
    L.append(jn)
    n=n+1
    #len(s)-1
    if n>len(s)-1:
        break
#sort the list
L.sort()
#reverse the list
L.reverse()
print(L)