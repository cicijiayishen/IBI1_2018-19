# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:10:59 2019

@author: cici
Practical 9: Implementation of a sequence comparison program in Python
"""
#create a list of lists containing BLOSUM62
import pandas as pd
data=pd.read_csv('C:/Users/sissy/Desktop/test Git/IBI1_2018-19/Practical9/BLOSUM62.txt',sep=' +',engine='python')
m=data.to_dict()
myDict={'A':1,'R':2,'N':3,'D':4,'C':5,'Q':6,'E':7,'G':8,'H':9,'I':10,'L':11,'K':12,'M':13,'F':14,'P':15,'S':16,'T':17,'W':18,'Y':19,'V':20,'B':21,'Z':22,'X':23}
#input sequences
seq01=input("Give me a protein sequence:")
seq02=input("GIve me a protein sequence:")
#split the sequences
seq1=seq01.replace('\n','')
seq2=seq02.replace('\n','')
#set initial distance as zero
score=0 #set initial score as zero
count=0
ali=[]#alignment
for i in range(len(seq1)): #compare each amino acid
    if seq1[i]!=seq2[i]:
        score=score+m[seq1[i]][seq2[i]]
        if m[seq1[i]][seq2[i]]>0:
            ali.append('+')
        elif m[seq1[i]][seq2[i]]<0:
            ali.append('-')
    if seq1[i]==seq2[i]:
        score=score+m[seq1[i]][seq2[i]]
        count=count+1#count the number of identical amino acid
        ali.append(seq1[i])#add the letter to alignment
ali=''.join(ali)
percentage=count/len(seq1)
#print out the results
print("Sequence 1:",seq01)
print("Alignment:",ali)
print("Sequence:",seq02)
print("The BLOSUM62 score is:",score)
print("The percentage identity is:",percentage)
print("The normalised BLOSUM62 score is:",score/len(seq1))