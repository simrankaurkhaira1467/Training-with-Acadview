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
