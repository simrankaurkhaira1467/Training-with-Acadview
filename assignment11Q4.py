#question 4: Call factorial function using thread.

import threading
import time
import math

def fact() :
    no=int(input('enter a number:'))
    res=math.factorial(no)
    print("Factorial:",res)

threading.Thread(target=fact).start()