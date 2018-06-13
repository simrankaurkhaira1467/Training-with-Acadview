
#ASSIGNMENT ON FUNCTIONS

#question 1: Create a function to calculate the area of a circle by taking radius from user.

import math
r=float(input("enter the radius:"))
def calculate_area(r):
    area=math.pi*r*r
    print("The area of circle is: %f" %(area))

calculate_area(r)

#question 2: Create a function perfect() to print all perfect numbers between 1 and 1000.

def perfect(n):
 sum=0
 for i in range(1,n):
     if n%i==0:
        sum=sum+i

 if sum==n:
  return True
 else:
  return False
for i in range(1,1001):
    if perfect(i):
     print(i)

#question 3: Print multiplication table of 12 using recursion.

def table(n,i):
    print(n*i)
    i=i+1
    if i<=10:
        table(n,i)
table(12,1)

#question 4: Write a function to calculate power of a number using recursion.

a=int(input("Enter value of a(base):"))
b=int(input("Enter value of b(power):"))

def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
print(power(a,b))

#question 5: Write a function to find factorial of a number but also store the factorials calculated in a dictionary.

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter the number:"))
f=fact(num)
dict={num:f}
print(dict)


