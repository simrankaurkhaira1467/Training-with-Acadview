#ASSIGNMENTS ON LOOPS
#question 1: Take 10 integers from user and print it on screen.

print("enter the elements:")
list=[int(x) for x in input().split()]
print(list)

#question 2: Write an infinite loop. An infinite loop never ends. Condition is always tue.

while(1):
    print("true")

#question 3: Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
print("enter the elements:")
list=[int(x) for x in input().split()]
print(list)
def square(list):
    sq = []
    for i in list:
        sq.append(i ** 2)
    return sq

print(square(list))

#question 4: From a list containing ints,strings,floats,make three lists to store them separately.

num=[1,'hi',89.0,'hello',67,'s',23.4]
print(num)
i=[]
f=[]
s=[]
for x in range(len(num)):
    if type(num[x])==int:
       i.append(num[x])
    if type(num[x])==str:
       f.append(num[x])
    if type(num[x])==float:
       s.append(num[x])
print(i)
print(f)
print(s)

#question 5: using range(1,101),make a list containing even and odd numbers.
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

#question 6: print the pattern:
#*
#**
#***
#****

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")

#question 7: Create a user defined dictionary and get keys corresponding to the value using for loop.
print("enter key and values in dictionary:")
dict={}
for i in range(5):
    key = input()
    value = input()
    dict[key]=value

for x in dict:
    print(x)

#question 8: Take input from user to make a list. again take one input and search it in list and delete that element if found. iterate over list using for loop.
print("enter values:")
list = [int(x) for x in input().split()]
n=input("enter element to search: ")
for i in list:
    if n==i:
     list.remove(n)

print(list)
