# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:11 2019

@author: sissy
"""

import re
from fractions import Fraction
#input the numbers
L=input("Please input numbers to compute 24:(use ',' to divide them)")
L_list=L.split(",")
re_numtest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
#check whether the numbers are in range 1 to 23
for char in L_list:
    if re_numtest.match(char):
        continue
    else:
        print('The input number must be intergers from 1 to 23')
        break
num = list(map(int,L_list))
print(num)
count=0
n=len(num)

def calculate(a,b,cal):
    if cal==0:
        return(a+b)
    elif cal==1:
        return(a-b)
    elif cal==2:
        return(b-a)
    elif cal==3:
        return(a*b)
    elif cal==4 and b!=0:
        return(Fraction(a,b))
    elif cal==5 and a!=0:
        return(Fraction(b,a))
def points(number):
    global count
    count = count+1
    
    if n == 1:
        if(float(num[0])==24):
            return 1 #Find the solution
        else:
            return 0 #Do not find solution
    #select two different numbers

    for i in range(0,n):
        count+=1
        for j in range(i+1,n):
            count+=1
            for cal in range(0,6):
                count+=1
                a = num[i]
                b = num[j]
                num[j] = num[n-1]
                num[i] = calculate(a,b,cal)
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


