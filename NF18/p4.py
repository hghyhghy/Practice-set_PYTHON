
from functools import reduce


# lamda function in python

# add operation using lamda 

add=lambda x,y: x+y

# driver code

r=add(233,24252)

print("The result is ",r)

# the filter function in python

# creating a list first 

# the filter(f,i) where f is the func and i is the iterator 

l=[12,34,23,45,44,78]

# filter to get even numbers from the list 

l1=list(filter(lambda x: x%2==0,l))

print(f"The even numbers from the lsit {l} is ",l1)

# the map function 

li=[2,4,6,8,12]

li1=list(map(lambda x: x*x,li))

print(f"The square of the numbers from the list {li} is ",li1)


# the reduce func in python 

a=[2,4,6,8,12]

b=(reduce(lambda x,y:x+y,a))

print(f"The sum of the numbers from the list {a} is ",b)


 