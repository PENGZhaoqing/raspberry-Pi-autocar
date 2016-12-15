# -*- coding: utf-8 -*
import RPi.GPIO as gpio
import config as c
import time


class UltraSensor:
    def __init__(self):
        gpio.setup(c.TRIG, gpio.OUT)
        gpio.setup(c.ECHO, gpio.IN)

    def dis(self):
        gpio.output(c.TRIG, False)
        time.sleep(0.5)

        gpio.output(c.TRIG, True)
        time.sleep(0.001)
        gpio.output(c.TRIG, False)

        while gpio.input(c.ECHO) == 0:
            start_time = time.time()

        while gpio.input(c.ECHO) == 1:
            end_time = time.time()

        duration = end_time - start_time
        distance = round(duration / 0.000058, 2)

        return distance
