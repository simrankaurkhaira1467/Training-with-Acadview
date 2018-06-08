#TUPLES
#question 1: Create a tuple with different data types and do the following:
#1. Find the length of tuples.
t= (1,5.6,"hello",True,4)
l=len(t)
print(l)

#2. Print largest and smallest elements of tuple.
tp=(5,6,8,9,4,3,1)
mx=max(tp)
print(mx)
mn=min(tp)
print(mn)
t1=('abcd','xyz','pq')
mx=max(t1)
print(mx)
mn=min(t1)
print(mn)

#3. To find the product of all elements of tuple.
prod=1
for i in tp:
    prod *=i

print(prod)

#SETS
#question 2: Create two set using user defined values.
#creating set 1.
x=input("enter values in set:").split()
s1=set()
for i in x:
    s1.add(i)

print(s1)

#creating set 2.
y=input("enter values in set:").split()
s2=set()
for i in y:
    s2.add(i)

print(s2)

#1. Calculate difference between sets.
print(s1-s2)
print(s2-s1)

#2. Compare two sets.
print(s1==s2)

#3. Print the result of intersection of two sets.
print(s1 & s2)

#DICTIONARY
#question 3:
#1. To create a dictionary to store name and marks of 10 students by user input.
dic={}
for i in range(10):
    key=input()
    value=int(input())
    dic[key]=value

print(dic)

#2. To sort dictionary created in previous question according to marks.
for key,value in sorted(dic.items(), key=lambda x: x[1]):
    print("%s : %s" %(key,value))

#3. Count occurences of each letter in word "MISSISSIPPI". Store count of every letter with a letter in a dictionary.
def char_freq(str):
    dict ={}
    for n in str:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

print(char_freq('MISSISSIPI'))