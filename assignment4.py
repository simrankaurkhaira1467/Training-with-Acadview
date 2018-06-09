
#question 1:Take an input from user and decide whether it is a leap year or not.
year = int(input("enter the year"))
if (year%4)==0 & (year%100)==0 & (year%400)==0:
            print("%d is a leap year." %(year))
else:
            print("%d is not a leap year." %(year))

#question 2:Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length = input("Enter the length:")
breadth = input("Enter the breadth:")
if length==breadth:
    print("Dimensions are of square.")
else:
    print("Dimensions are of rectangle.")

#question 3:Take the input age of 3 people and determine oldest and youngest among them.
a1 = int(input("enter age of first person:"))
a2 = int(input("enter age of second person:"))
a3 = int(input("enter age of third person:"))
if (a1 > a2 and a1 > a3):
    print("first is oldest.")
elif (a2 > a1 and a2 > a3):
    print("second is oldest.")
elif (a3 >a1 and a3 > a2):
    print("third is oldest.")

if (a1 < a2 and a1 < a3):
    print("first is youngest.")
elif (a2 < a1 and a2 < a3):
    print("second is youngest.")
elif (a3 < a1 and a3 < a2):
    print("third is youngest.")

#question 4:To know the prizes based on the number of points scored.
points = int(input("enter the positive integer points up to 200"))
if (points>=1 and points<=50):
    print("Sorry!No prize this time.")
elif (points>=51 and points<=150):
    print("Congratulations!You won a Wooden Dog.")
elif (points>=151 and points<=180):
    print("Congratulations!You won a Book.")
elif (points>=181 and points<=200):
    print("Congratulations!You won chocolates.")
else:
    print("Invalid input")

#question 5:A shop will give discount of 10% if the cost of purchased quality is more than 1000. Ask user for quantity.Print total cost for user.
quantity=int(input("Enter the quantity:"))
if ((quantity*100)>1000):
    discount=0.1*quantity*100
    cost=(quantity*100)-discount
    print("The Total cost of user is %d" %(cost))
else:
    print("No discount")



