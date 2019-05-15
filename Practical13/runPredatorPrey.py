# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:12:42 2019

@author: sissy
"""

import os
import numpy
import matplotlib.pyplot as plt
import re
os.chdir("C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical13")

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
        del(l[0])
        list.append(l)
        
results=numpy.array(list)


results=results.astype(numpy.float)

plt.plot(results[:,0],label='Predator (b=0.02, d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1, d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.legend()
plt.show()

