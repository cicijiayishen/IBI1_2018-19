# What does this piece of code do?
# Answer: Finding Random Prime Numbers between 1 and 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    #p is True than the loop is stopped
    p=True
    n = randint(1,100)
    #u is the ceiling of root of n
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            #p is False, then go another loop
            p=False


     
print(n)
            