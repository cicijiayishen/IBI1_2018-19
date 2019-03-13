# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:27:05 2019

@author: sissy
"""

x=2019
a=2019
#find the biggest 2**n that is smaller than x
n=13   
while x!=0:
    if n>=0:
        if x ==2**n:
            break
            print(n)
        elif x > 2**n:
            x=x-2**n
            print(n)
            n=n-1
        elif x < 2**n:
            n=n-1
    else:
        break