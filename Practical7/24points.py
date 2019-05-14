# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:11 2019

@author: sissy
"""

import re
from fractions import Fraction
re_numtest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
#input the numbers
i=1
while i:
    i=0
    L=input("Please input numbers to compute 24:(use ',' to divide them)")
    L_list=L.split(",")
#check whether the numbers are in range 1 to 23
    for char in L_list:
        if re_numtest.match(char):
            continue
        else:
            print('The input number must be intergers from 1 to 23')
            i=1
            break
num = list(map(int,L_list))
count=0

def points(n):
    global count
    count = count +1
    
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            
            num[i] = a+b
            if(points(n-1)):
                return 1
            
            num[i] = a-b
            if(points(n-1)):
                return 1  
            
            num[i] = b-a
            if(points(n-1)): 
                return 1 
            
            num[i] = a*b
            if(points(n-1)): 
                return 1  
            
            if a:
                #floats are not precise
                num[i] = Fraction(b,a)
                if(points(n-1)): 
                    return 1 
                
            if b:
                num[i] = Fraction(a,b)
                if(points(n-1)): 
                    return 1 
            #Backtracking  
            num[i] = a
            num[j] = b
    return 0 


if (points(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)


