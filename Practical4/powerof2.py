# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:27:05 2019

@author: cici
Practical4: Variables, Booleans and Loops
"""

#assign x as a positive integer
x=int(input("Please input a positive integer:"))
#check validity
if x<=0:
    print("Error! The number is not a positive integer.")
#write the template of the outcome 
b=str(x)+" is "
c="2**"
#find the biggest 2**n that is smaller than x
#power no bigger than 13
n=13   
#x is possitive
while x!=0:
#make sure n won't be a negative number
    if n>=0:
        if x == 2**n:
            b=b+c+str(n)
            break
        elif x > 2**n:
            x=x-2**n
            b=b+c+str(n)+"+"
            n=n-1
        elif x < 2**n:
            n=n-1
    else:
        break
#outcome
print(b)