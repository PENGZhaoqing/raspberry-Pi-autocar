# -*- coding: utf-8 -*
import RPi.GPIO as gpio
import UltraSensor
import random as rand
import time


class AutoRun:
    def __init__(self, car):
        self.sensor = UltraSensor
        self.car = car

    def run(self):
        while True:
            try:
                if (self.sensor.dis < 20):
                    if rand.random() > 0.5:
                        self.car.rightspin(50)
                        time.sleep(0.5)
                        continue
                    else:
                        self.car.leftspin(50)
                        time.sleep(0.5)
                        continue
                self.car.forward(30)
                time.sleep(0.2)

            except KeyboardInterrupt:
                self.car.shutdown()
