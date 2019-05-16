# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:10:27 2019

@author: cici
Practical 12: Modelling infections
Part 3: Looking at disease spread in 2D
"""
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array for all susceptible population
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)#randomly choose where the outbreak will be
population[outbreak[0],outbreak[1]]=1
#set parameters
beta=0.3
gamma=0.05
#loop for 100 time points
for n in range(0,101):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! 
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    #plot graphs
    if n==0 or n==10 or n==50 or n==100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')