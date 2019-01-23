

from time import sleep
from threading import *

class Saket(Thread):

    def run(self):
        for i in range(5):

            print("Saket")
            sleep(1)

class Vats(Thread):

    def run(self):
        for i in range(5):
            print("Vats")
            sleep(1)

t1=Saket()

t2=Vats()

t1.start()
sleep(0.2)
t2.start()

t1.join()
print("Bye Vats")