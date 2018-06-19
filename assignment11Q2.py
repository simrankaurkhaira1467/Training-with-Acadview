#question 2:Make a thread that prints numbers from 1-10, waits for 1 sec in between.

import time
from threading import Thread

def SleepMe(i):
    print("Thread %i." %(i+1))
    time.sleep(1)

for i in range(0,10):
    th=Thread(target=SleepMe,args=(i, ))
    th.start()