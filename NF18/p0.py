

# the range function in python 

myrange=range(1,21,5)

it=iter(myrange)

print(next(it))

print(next(it))

print(next(it))

print(next(it))

#the zip function in python 

# it returns the sequence of two tuples 

x=[11,22,33]

y=[89,90,99]

Zipped=zip(x,y)

print(list(Zipped))

# program to demonstrate the zip function 

subject=['Maths','English','Computer Science']

marks=[98,90,97]

# using the for loop 

for i,j in zip(subject,marks):

    print(f"Marks in {i} = {j}")


# program to demonstrate the sorted function 
    
mark=[78,45,39,98,56,100]

# sorting the marks

sm=sorted(mark)

print("The sorted marks is ", sm)

# printing the element in reverse order

smr=sorted(mark,reverse=True)

print("The reverse sorted elements are ")

print(smr)