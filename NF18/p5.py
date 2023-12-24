
# recursive way to find factorial 

# creating a definition 

from math import *

from random import *

def facto(n):

    if n==1:

        return 1
    
    else:

        return n*facto(n-1)

n=7

temp=facto(n)

print(f"The fctorial of the number {n} is ", temp)


# some math operations 

print(exp(5))

print(factorial(7))

print(ceil(7.8))

print(pow(2,3))

print(log(8,3))

print(sqrt(25))

print(random())

print(randint(2,10))

print(randrange(1,10,2))

print(uniform(2,10))





