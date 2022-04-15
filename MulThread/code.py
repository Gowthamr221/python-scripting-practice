from time import sleep
from threading import *
# by defualt we use one thread from processor
# this thread is called main thread
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("bye")