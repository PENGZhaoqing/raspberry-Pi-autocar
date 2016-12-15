# -*- coding: utf-8 -*
import RPi.GPIO as gpio

import random as rand
import time
import threading

class AutoRun(threading.Thread):
    def __init__(self, car):
        threading.Thread.__init__(self)
        self.car = car
        self.flag = True

    def run(self):
        while self.flag:
            if (self.car.sensor.dis() < 20):
                if rand.random() > 0.5:
                    self.car.rightspin(70)
                    time.sleep(0.5)
                    print "spinning right"
                    continue
                else:
                    self.car.leftspin(70)
                    time.sleep(0.5)
                    print "spinning left"
                    continue
            self.car.forward(50)
            time.sleep(0.2)
            print "forwarding..."
        self.car.shutdown()

    def stop(self):
        self.flag=False
        
