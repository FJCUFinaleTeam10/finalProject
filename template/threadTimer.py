from threading import Thread, Event
import time

from sympy import true


class MyThread(Thread):
    def __init__(self, event, delayTime: int):
        Thread.__init__(self)
        self.stopped = event
        self.delayTime = delayTime

    def run(self):
        while not self.stopped.wait(self.delayTime):
            print(time.asctime(), "my thread")
            # call a function


stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
while true:
    print(time.asctime(), " my test")

