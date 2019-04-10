# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:11 2019

@author: sissy
"""
L=input("Please input numbers to compute 24:(use ',' to divide them)")
L_list=L.split(",")
print(L_list)
for i in range(1, len(L)+1):
    L_list=[int(L[i])]
print(L_list)
def compute(x,y,op):
    if op=='+':return x+y
    elif op=='*':return x*y
    elif op=='-':return x-y
    else:return x/y if y else None

def exp(p,iter=0):
    from itertools import permutations
    if len(p)==1:
        return [(p[0],str(p[0]))]
    operation = ['+','-','*','/']
    ret = []
    p = permutations(p) if iter==0 else [p]
    for array_n in p:
        #print(array_n)
        for num in range(1,len(array_n)):
            ret1 = exp(array_n[:num],iter+1)
            ret2 = exp(array_n[num:],iter+1)
            for op in operation:
                for va1,expression in ret1:
                    if va1==None:continue
                    for va2,expression2 in ret2:
                        if va2==None:continue
                        combined_exp = '{}{}' if expression.isalnum() else '({}){}'
                        combined_exp += '{}' if expression2.isalnum() else '({})'
                        new_val = compute(va1,va2,op)
                        ret.append((new_val,combined_exp.format(expression,op,expression2)))
                        if iter==0 and new_val==24:
                            return ''.join(e+'\n' for x,e in ret if x==24)
    return ret
print(exp([L]))

import re
string=input("Please input numbers to compute 24:(use ',' to divide them)")
list_of_numbers=re.split(r',',string)
print(list_of_numbers)
valid_numbers=[]
count=0 #use tuple to returen 2 variables
cc=False
if check():
    select(valid_numbers)



def check():
    for i in range(1,len(list_of_numbers)+1):
        num=int(list_of_numbers[i])
        print(num)
        if num>24 or num<1:
            return(-1)
            

#complexity=e的n次方，e^n