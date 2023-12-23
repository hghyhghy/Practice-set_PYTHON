

# to find wheather a key is present in the dictionary or not 

# creating a dictionary

d={1:10,2:20,3:30,4:40,5:50,6:607}

print("The created dictionary is ")

print(d)

# taking user input to find the key

x=int(input("Enter the key to search"))

# using a if else loop

if x in d:

    print(f"The key {x} is present in the dictionary {d}")

else:

    print(f"The key {x} is not present in the dictionary {d}")
     
# creating a temporary variable to store data
    
temp=[]

# using  a  for loop

for x in range(1500,2000):

    if x%7==0 and  x%5==0:

        temp.append(str(x))

print(",".join(temp))

# python program to print numbers between 100 and 400 where each digit is even number

# creating an empty list to store data 

empty=[]

# using   a for loop 


for s in range(100,400):

    if (s[0]%2==0) and  (s[1]%2==0)  and  (s[2]%2==0):

        empty.append(s)

print(",".join(empty))