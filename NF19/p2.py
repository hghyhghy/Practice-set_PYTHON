

# creating another class vehicle 

class Vehicle():

    def __init__(self,make,model,year,warranty):

        self.make=make

        self.model=model

        self.year=year

        self.warranty=warranty


#creating objects in th class
        
myvehicle=Vehicle("Audi","Audi-A4",2019,2)

# calling the attributes 

print("The making company name is ", myvehicle.make)

print("The model  name is ", myvehicle.model)

print("The making year  is ", myvehicle.year)

print("The car warranty is ", myvehicle.warranty,"Yrs")

#updating the attributes 

Car=Vehicle("Mahindra","Mahidra-Truck",2017,5)

print("The making company name is ", Car.make)

print("The model  name is ", Car.model)

print("The making year  is ", Car.year)

print("The car warranty is ", Car.warranty,"Yrs")