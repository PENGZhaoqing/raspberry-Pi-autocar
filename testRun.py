from AutoRun import AutoRun
from car import Car
import time

car=Car()
auto=AutoRun(car)

auto.start()
raw_input('Press return to stop:') 
auto.stop()

