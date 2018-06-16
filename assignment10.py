#ASSIGNMENT ON CLASSES
#question 1: Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal():
    '''
    This class is made to showcase some features of Animal class.
    '''
    legs = 4
    eyes = 2
    ears = 2

    def Animal_attribute(self):
        '''
            This method is used to show some features of Animal
        Parameters
        ----------
        legs - tells how many legs does Animals have
        eyes - tells how many eyes does Animals have
        ears - tells how many ears does Animals hasve
        Returns
        --------
        '''
        print('%d legs' % self.legs)
        print('%d eyes' % self.eyes)
        print('%d ears' % self.ears)


class Tiger(Animal):
    def __init__(self):
        self.Animal_attribute()



ob=Tiger()







#question 2: Write output of the given code:
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'
a=A()
b=B()
print(a.f())
print(b.f())

#OUTPUT:
#A
#B

#question 3: Create a class Cop. Initialize its name, age, work experience and designation. Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop. Define method add_mission_details. Select an object of Cop and access methods of base class to
#get information for a particular cop and make it available for mission.

class Cop:
    '''
        This class is made to show show details of a cop
    '''
    def __init__(self,name,age,workexp,des):
        self.name=name
        self.age=age
        self.workexp=workexp
        self.des=des

    def Add_details(self):
        self.name=input("Enter the name:")
        self.age=input("Enter the age:")
        self.workexp=input("Enter the work experience:")
        self.des=input("Enter the designation:")

    def Display_details(self):
        print("The name is:" + str(self.name))
        print("The age is:" + str(self.age))
        print("The work experience is:" + str(self.workexp))
        print("The designation is: " + str(self.des))

    def Update_details(self):
        '''
                This method is used to update the cop details
        '''
        self.name = input("Enter the update name : ")
        self.age = input("Enter the updated age   : ")
        self.workexp = input("Enter the updated work experience : ")
        self.desig = input("Enter the updated designation     : ")

class Mission(Cop):
    def add_mission_details(self):
        print("\nCOP IS READY FOR MISSION.......")

obj= Cop('name', 'age', 'work experience', 'designation')
obj.Add_details()
obj.Display_details()
obj.Update_details()
obj.Display_details()


#question 4: Create a class Shape. Initialize it with length and breadth. Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class Shape():

    def __init__(self,length,breadth):
        self.length= length
        self.breadth= breadth

    def Area(self):
        print("Area is : " + str(self.length * self.breadth))

class Rectangle(Shape):
    '''
    This class inherit Shape class method.
    '''
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Square(Shape):
    '''
    This class also inherit shape class.
    '''
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

rect1 = Rectangle(int(input("Enter length of rectangle : ")), int(input("Enter breadth of rectangle : ")))
rect1.Area()

square1 = Square(4, int(input("Enter breath of square : ")))
square1.Area()