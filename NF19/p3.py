
# instance and attribute example 

# creating a class employee 

class Emp():

    # creating the function 

    def __init__(self):

        self.name="Subham Sarkar"

        self.age=20

        self.roll="Junior Consultant"

        self.salary="7LPA"

    def show(self):

        print(self.name)

        print(self.age)

        print(self.roll)

        print(self.salary)


# creating an instance 

E1=Emp()

print("Showing in the dictionary form using vars",vars(E1))

# printing all directory in the emp class

print("All the directories are ", dir(E1))

    