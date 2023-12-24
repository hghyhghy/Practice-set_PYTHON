

# program to find area and perimeter of the circle 

# creating a  function 

def ofperimeterandarea(r):

    a=2*3.14*r

    p=3.14*r*r

    return a,p

# driver code 

area,peri=ofperimeterandarea(6.5)

print("The area of the circle is ", area)

print("The perimeter of the circle is ", peri)

# global variable in python 

# creating another function 

def func(x):

    # declaring global variable 

    global y 

    y=x+10

    z=6

    print("x,y,z inside the function", x,y,z)

# driver code 

x,y,z=5,34,56

print("Before the funcion call the values of x,y,x are ",x,y,z)

func(x)

print("After the funcion call the values of x,y,x are ",x,y,z)

