
# multiple inheritance 

class Car():

    # creating the function 

    def  drive(self):

        print("The car is moving ")
    

# creating another class 

class Aeroplane():

    def fly(self):

        print("The aeroplane is flying")


# inheriting both class 
        

class  Transport(Car,Aeroplane):

    pass

# creating an object in the class

fv=Transport()

fv.drive()

fv.fly()