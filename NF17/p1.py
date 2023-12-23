

# list comprehension in python 

# generation of squares using list comprehension 

squares=[x**2 for x in range (10)]

print(squares)

# dictionary comprehension 

s={x:x**2 for x in range (1,11)}

print(s)

# nested dictionaries 

favourite_dict={'Tom':[12,13,14],
                
                'Jerry':[23,32,12,21],
                
                'Spike':[89,56,34]}

print("The created dictionary is ")

print(favourite_dict)

# displaying each persons favourite numbers 

for name in favourite_dict:
    
    print("Favourite numbers of >>", name)

    for favourite in favourite_dict[name]:

        print(favourite)

# pyramid structure 
        
# taking user input 
        
n=int(input("Enter a number>>"))

for i in range(1,n+1):

    for j in range(1,i+2):

     print(i,end=" ")
    
    print()
    

