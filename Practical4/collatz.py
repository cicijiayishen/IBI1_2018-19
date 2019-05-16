# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:51:54 2019

@author: cici
Practical4: Variables, Booleans and Loops
"""

#start from a positive integer n
n=int(input('Please input a positive integer:'))
if n<=0:#check validity
    print('Error: The number is not positive.')
elif n>0:
    #if n is even
    #n=n/2
    while 1==1:
        if n%2==0:
            n=n/2
            print(n)
    #if n is odd
    #n=n*3+1
        elif n==1:
            break
        elif n%2==1:
            n=n*3+1
            print(n)
        #print n