

# python program to remove duplicates from the list 
 
# taking user inputs 

i=input("Enter the list of elements ")

# splitting the elements of the list

lis=list(i.split())

# creating a local list varibale to store the values 

temp=[]

# using a for loop 

for x  in lis:

    if x not in temp:

        temp.append(x)

print("The non duplicate elements are ")

print(temp)

print()

# python program to check wheather a list is empty or not

# taking user input 

j=input("Enter the list of elements ")

li=list(j.split())

if not li:

    print("The list is empty")

else:

    print("The list is not empty")

    print(li)


