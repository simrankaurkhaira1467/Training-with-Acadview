#ASSIGNMENT ON THREADS
#QUESTION 1:Create a threading process such that it sleeps for 5 seconds and prints out a message.

import threading
import time

class MyThread(threading.Thread):

    def __init__(self,name):
        ''' Constructor'''
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print("Starting: " + self.name)
        time.sleep(5)
        print("Hello,How are you?")
        print("Exiting: " + self.name)

threadobj=MyThread(1)
threadobj.setName('Simran')
threadobj.start()

#question 2:Make a thread that prints numbers from 1-10, waits for 1 sec in between.

import time
from threading import Thread

def SleepMe(i):
    print("Thread %i." %(i+1))
    time.sleep(1)

for i in range(0,10):
    th=Thread(target=SleepMe,args=(i, ))
    th.start()

#question 3:Make a list that has 5 elements. Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display. Delay goes like 2sec-4sec-6sec-8sec-10sec.

import threading
import time

class MyThread(threading.Thread):

    def __init__(self,list,name):
        """ Constructor"""
        threading.Thread.__init__(self)
        self.list= list
        self.name=name


    def run(self):
        print("Starting:" + self.name)
        for i in range(0,5):
            time.sleep(i * 2)
            print(list[i])
        print("Exiting: " + self.name)

list=[2,3,4,8,9]
thread1=MyThread(list,"Simran")
thread1.start()

#question 4: Call factorial function using thread.

import threading
import time
import math

def fact() :
    no=int(input('enter a number:'))
    res=math.factorial(no)
    print("Factorial:",res)

threading.Thread(target=fact).start()