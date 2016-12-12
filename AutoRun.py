# -*- coding: utf-8 -*
import RPi.GPIO as gpio
from UltraSensor import UltraSensor
import random as rand
import time


class AutoRun:
    def __init__(self, car):
        self.sensor = UltraSensor()
        self.car = car
        self.flag= True

    def run(self):
        try:
            while self.flag:
                if (self.sensor.dis() < 20):
                    if rand.random() > 0.5:
                        self.car.rightspin(90)
                        time.sleep(0.5)
                        print "spinning right"
                        continue
                    else:
                        self.car.leftspin(90)
                        time.sleep(0.5)
                        print "spinning left"
                        continue
                self.car.forward(30)
                time.sleep(0.2)
                print "forwarding..."
        except KeyboardInterrupt:
            self.car.shutdown()

    def stop(self):
        self.flag=False
        
