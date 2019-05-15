# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:14:51 2019

@author: cici
Practical 12: Modelling infections
Part 2: The effect of vaccination
"""
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import collections
for p in range(0,11):#Change differrent percentages
    N=10000 #population size
    percentage=p*0.1
    vac=int(N*percentage)#vaccination population size
    I=[1]
    i=1
    S=[9999-vac]
    s=9999-vac
    R=[vac]
    r=vac
    #set parameters
    beta=0.3
    gamma=0.05
    for n in range(0,1000):#loop over 1000 time points
        ratio=i/N
        #Randomly choose people to transfer from S to I
        arrayI=np.random.choice(range(2),s,p=[1-ratio*beta,ratio*beta])
        counterI=collections.Counter(arrayI)
        s=counterI[0]
        S.append(s)
        #Randomly choose people to transfer from I to R
        arrayR=np.random.choice(range(2),i,p=[1-gamma,gamma])
        counterR=collections.Counter(arrayR)
        r=r+counterR[1]
        R.append(r)
        #'I' includes both from I and from S
        i=counterI[1]+counterR[0]
        I.append(i)
    #PLot the graph
    plt.plot(I,label=str(p)+'%')
    plt.title('SIR model')
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.legend()
plt.show()

#Save the figure
#plt.figure(figsize=(6,4),dpi=150)

'''
#Change the color of the lines
from matplotlib import cm
plt.plot(data,color=cm.viridis(30))
'''