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