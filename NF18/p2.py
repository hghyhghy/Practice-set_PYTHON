

# function composition

# creating two functions 

def addition(a,b):

    s= a+b

    return s

def checker(x):

    if x%2==0:

        print(f"This number {x} is an Even number")
    
    else:


        print(f"This number {x} is an Odd  number")



answer=addition(10,22)

answer1=checker(88)

print(answer)

# program to display the name and age of the students 

# creating the function 

def display(name,age=7):   # passing arguments through functions

    print("Student name is ", name)

    print("Student age  is ", age)


# driver code 
    
display("Subham",20)

display("Shreyoshi",20)

display("Ayush")

# args in python

# creating another function 

def ofstudent(name,age=7,*args):

    print("The information of the students ")

    print("Student name is", name)

    print("Student age  is", age )

    print("Other Information  of studnent  is")

    for i in args:

        print(i)


# driver code

ofstudent("Subham",20,"Male","Btech 3rd Yr")



    


