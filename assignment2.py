#question 1: Create a list with user-defined inputs.
names = ["simran",'ashita',"sonali","shreya","diyansha"]
print(names)

#question 2: Add the given list to above created list.
a=['google',"apple","facebook","microsoft",'tesla']
names.append(a)
print(names)

#question 3: Count the number of times an object occurs in a list.
l = [1,6,1,"hi",1.25,"hello",["hi",1]]
print(l.count("hello"))
print(l.count("hi"))
print(l.count(1))

#question 4: Create a list with numbers and sort it in ascending order.
num = [9,7,4,0,5,2,6,1]
print(num)
num.sort()
print(num)

#question 5: We have two lists A and B which are in ascending order. Write a program to merge them into single sorted list C.
A=[1,2,3,4]
B=[5,6,7,8,9]
C= A + B
print(C)

#question 6: Implement stack and queue using lists.
#implementing stack
stack=['hello','hi','how','are','you']
stack.append('feeling')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.append('doing')
print(stack)

#implementing queue
from collections import deque
queue = deque(['google',"apple","facebook","microsoft",'tesla'])
print(queue)
queue.append("twitter")
print(queue)
print(queue.popleft())
queue.append("ibm")
print(queue)
print(queue.popleft())

#optional question: Count even and odd numbers in a list.
nm = [1,2,5,4,7,9,6,8,0,8]
even=0
odd=0
for x in nm:
    if not x % 2:
        even=even+1
    else:
        odd=odd+1

print("even numbers=%d" %(even))
print("odd numbers=%d" %(odd))



