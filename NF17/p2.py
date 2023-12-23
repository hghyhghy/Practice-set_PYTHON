

# print a string in a reverse order 

# taking user input 

name=input("Enter the name ")

l=name.split()

l.reverse()

for i in l:

    print(i, end=" ")

print()

lis=input("Enter a list ")

s1=lis.split()

print(s1)

result=" "

for element in s1:

    result=result+str(element)

print("Concatenated element in the list is ", result)

# find the list of words which are longer than a given range 

# taking the user input 

st=input("Enter the list of the words ")

n=int(input("Enter the length"))

# splitting the list

temp=st.split()

# creating a list to store values

word_length=[]

# using a for loop

for x in temp:

    if len(x)>n:
        
        word_length.append(x)

print(f"The words with length greater than {n} is ", word_length)

