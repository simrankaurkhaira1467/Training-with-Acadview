#ASSIGNMENT ON SOME COMMONLY USED PACKAGES.

#question 1: What is time tuple?
#answer: Python time functions handle time as a tuple of 9 numbers(year,month,day,hour,minute,second,day of week,day of year and daylight savings).
#It basically provides usage of tuple for the ordring and notation of time.

import time
#gmtime shows the time tuples.
print(time.gmtime(time.time()))

#question 2: Write a program to get formatted time.

import time
localtime=time.asctime(time.localtime(time.time()))
print("local current time :",localtime)

#question 3: Extract month from the time.
import datetime
now=datetime.datetime.now()
print("Current month: %d" %now.month)

#question 4: Extract day from the time.
print(time.strftime("%d, %j"))


#question 5: Extract date from the time.
print(time.strftime("%d" in "%d/%m/%y")


#question 6: Write a program to print time using localtime method.

import time
localtime=time.localtime(time.time())
print("local current time :",localtime)

#question 7: Find the factorial of a number input by user using math package functions.

import math
n=int(input("Enter the number:"))
f=math.factorial(n)
print("The factorial of %d is %d." %(n,f))


#question 8: Find the GCD of a number input by user using math package functions.

import math
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
g=math.gcd(n,m)
print("The GCD of %d and %d is %d." %(n,m,g))


#question 9: Use OS package and do:(a)get present working directory. (b)Get the user environment.
import os
print(os.getcwd())
print(os.getenv('TEMP')