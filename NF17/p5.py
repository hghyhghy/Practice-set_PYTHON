

# python program to print all possible numbers

number=1

print("Printing all possible numbers upto 11")

# using while loop 

while number< 11:

    print(number)

    number=number+1

# python program to print odd positioned element from the list 
    
# creating a list first 
    
l=[12,34,21,33,22,1,45]

print("The original list is ")

print(l)

n=len(l)

print("The elements on the list in odd position is ")


for x in range(0,n,2):

    print(l[x])


# program to find common elements in two lists 
    
a=[12,34,21,33,22,1,45]

a1=[10,30,21,33,28,11,45]

# using a for loop 

print(f"The common elements between two lists {a} and {a1} are ")

for num1 in a:

    for num2 in a1:

        if num1==num2:

            print(num2)


