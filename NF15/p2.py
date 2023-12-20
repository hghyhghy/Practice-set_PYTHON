

# creating a dictionary 

d1={'Name':'Subham','ID':10905521,'Title':'Sarkar'}

print("The dictionary is ")

print(d1)

# creaing an empty dictionary

d={}

print("The empty dictionary is ")

print(d)

# copying element in other dictionary 

d=d1.copy()

print("After copying the dictionary becomes ")

print(d)

# printing the keys and values of the dictionary 

print(f"The keys of the dict {d} is ")

print(d.keys())

print(f"The values of the dict {d} is ")

print(d.values())

# items returns the list of dictionary 

print(f"The items of the dict {d} is ")

print(d.items())

# updating the value of the dictionary 

d0={'Roll':'Junior SDE'}

print(f"After updating the dict {d1} will be ")

d1.update(d0)

print(d1)