
# reversing the elements of the string as list elements 

string="programming"

print("The original string is")

print(string)

# reversing the string 

rstr=list(reversed(string))

print("The reversed string is ")

print(rstr)

# enumerator in a string 

s="pythonprogramming"

enum=list(enumerate(s))

print(enum)

# binary / octal / hexadecimal representation in string 

num=14

print(f"The {num} in binary:{num:b}, in octal:{num:o}, in hexadecimal:{num:x}")

#function assigned to the variable 

def addition(a,b):
    
    s=a+b

    return s


# assigning the  function to the  varibale 

add=addition

result=add(10,12)

print(result)
