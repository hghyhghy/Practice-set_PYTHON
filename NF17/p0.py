

# python break statement 

i=5

while i>0:

    if i==3:

        break
    
    print (i)

    i=i-1

print("End of the program ")

# continue statement 

# using  a for loop 

for letters in "program":

    if letters== 'g':

        continue
    
    print(letters)


# conditional statement 
    
vowels="aeiou"

while True:
    
    v=input("Enter a letter ")

    if v in vowels:

        print(v,"Is the vowel")

        break
    
    print("This is not a vowel ")

print("Enter another letter")

