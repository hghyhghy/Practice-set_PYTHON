
 # creating the dictionary 

d1={'Name':'Subham','ID':10905521,'Title':'Sarkar'}

print("The created dictionary is ")

print(d1)

# iterating over the key 
    
for j in d1.keys():

    print(j,":",d1[j])

# iterating over key value pairs 
    
for i,k in d1.items():

    print(i,":",k)

# popping element from the dictionary 
    
# creating another dictionary

d={1:20,2:45,3:23,4:56}

print("The newly created dictionary is ")

print(d)

print(d.pop(2))


print("After popping the dict becomes ")

print(d)

