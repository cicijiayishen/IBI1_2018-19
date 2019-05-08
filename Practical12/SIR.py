# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:00 2019

@author: sissy
"""

import numpy as np
import matplotlib.pyplot as plt
import collections
N=10000 #total number of people in population
I=[1]
i=1
S=[9999]
s=9999
R=[0]
r=0
beta=0.3
gamma=0.05
#loop over 1000 time points
for n in range(0,1000):
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
print(I)
print(S)
print(R)

plt.plot(I,label='infected')
plt.plot(S,label='susceptible')
plt.plot(R,label='recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()

#Save the figure
plt.figure(figsize=(6,4),dpi=150)
