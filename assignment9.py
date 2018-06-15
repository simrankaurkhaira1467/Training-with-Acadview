#ASSIGNMENT ON CLASSES
#question 1: Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle():
    def __init__(self, radius):
        self.radius=radius

    def getArea(self):
        print("Area is : " + str(3.14 * self.radius * self.radius))

    def getCircumference(self):
        print("Circumference is: " + str(2 * 3.14 * self.radius))

obj=Circle(float(input("Enter the radius:")))
obj.getArea()
obj.getCircumference()

#question 2: Create a Student class and initialize it with name and roll number. Make methods to:
# 1.Display: It should display all information of the student.

class Student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(self.name)
        print(self.rollno)

obj=Student(input("Enter the name of student:"),input("Enter his/her roll number:"))
obj.display()

#question 3: Create a Temperature class. Make two methods:
#1. convertFahrenheit: It will take celsius and will print it into Fahrenheit.
#2. conertCelsius: It will take Fahrenheit and will convert it into celsius.

class Temperature():
    def convertFahrenheit(self, celsius):
        print("Temperature in Fahrenheit is :" + str((celsius * (9/5) +32)))

    def convertCelsius(self, fahrenheit):
        print("Temperature in Celsius is :" + str((fahrenheit-32) * (5/9)))

obj=Temperature()
obj.convertFahrenheit(float(input("Enter temperature in celsius:")))
obj.convertCelsius(float(input("Enter temperature in fahrenheit:")))

#question 4: Create a class MovieDetails and initialize it with Movie name, artist name, Year of release and ratings.
#1. Display: Display the details.
#2. Update: Update the movie details.

class MovieDetails():
    def _init_(self,moviename,artistname,yearofrelease,ratings):
        self.moviename=moviename
        self.artistname=artistname
        self.yearofrelease=yearofrelease
        self.ratings=ratings

    def display(self):
        print("Movie name is :" +str(self.moviename))
        print("Artist name is :" + str(self.artistname))
        print("Year of release is :" + str(self.yearofrelease))
        print("Rating is :" + str(self.ratings))

    def update(self):
        self.moviename=input("enter updated Movie name:")
        self.artistname=input("enter updated Arist name:")
        self.yearofrelease=input("enter updated year of release")
        self.ratings=input("enter updated ratings:")

obj=MovieDetails('YJHD','DEEPIKA','2013','7')
obj.display()
obj.update()
obj.display()

#question 5: Create a class Expenditure and initialize it with expenditure, savings. Make the following methods:
#1. Display expenditure and savings.
#2. Calculate total salary.
#3. Display salary.

class Expenditure():
    def __init__(self,expenditure,savings):
        self.expenditure=expenditure
        self.savings=savings

    def display(self):
        print("The Expenditure is: " + str(self.expenditure))
        print("The Savings are" + str(self.savings))

    def totalsalary(self):
         Expenditure.totalsalary=self.expenditure+self.savings

    def display_totalsalary(self):
         print("Total salary is:" + str(self.totalsalary))

obj=Expenditure(input("\nEnter Expenditure:"), input("Enter savings:"))
obj.display()
obj.totalsalary()
obj.display_totalsalary()



