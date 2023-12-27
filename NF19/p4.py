
#super keyword in python

# creating a class called parent 

class Parent():

    # initializing 

    def __init__(self,name):

        self.name=name

    # creating another function of greet 
        
    def greet(self):

        print(f"Hello myself {self.name}")


# creating the class inheriting the another class 
        
class Child(Parent):

    def __init__(self, name,age):

        super().__init__(name)

        self.age=age
    
    def greet(self):

        parent_greet= super().greet()

        return f" I am {self.age} years old "
    

# creating an object in the class 
    
Mychild=Child("akash ", 5)

print(Mychild.greet())