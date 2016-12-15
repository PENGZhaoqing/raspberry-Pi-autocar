import RPi.GPIO as gpio
import config as c
from UltraSensor import UltraSensor

class Wheel(object):
    def __init__(self, F_PIN, B_PIN):
        '''
        :param in_pin1 in_pin2: IN1 IN2 or IN3 IN4
        :param enable_pin1 enable_pin2: ENA or ENB
        '''
        gpio.setup(F_PIN, gpio.OUT)
        gpio.setup(B_PIN, gpio.OUT)
        self.F_pwm=gpio.PWM(F_PIN,50)
        self.B_pwm=gpio.PWM(B_PIN,50)
        self.state = "stop"
        
    def forward(self, speed):
        if self.state == "backward":
            self.B_pwm.stop()
        self.F_pwm.start(0)
        self.F_pwm.ChangeDutyCycle(speed)
        self.state = "forward"

    def backward(self, speed):
        if self.state == "forward":
            self.F_pwm.stop()
        self.B_pwm.start(0)
        self.B_pwm.ChangeDutyCycle(speed)
        self.state = "backward"

    def stop(self):
        if self.state== "forward":
            self.F_pwm.stop()
        if self.state== "backward":
            self.B_pwm.stop()
        self.state="stop"

class Car(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        self.sensor = UltraSensor()
        self.left_wheel = Wheel(c.LF_PIN, c.LB_PIN)
        self.right_wheel = Wheel(c.RF_PIN, c.RB_PIN)

    def forward(self, speed):
        self.left_wheel.forward(speed)
        self.right_wheel.forward(speed)

    def backward(self, speed):
        self.left_wheel.backward(speed)
        self.right_wheel.backward(speed)

    def leftspin(self, speed):
        self.left_wheel.backward(speed)
        self.right_wheel.forward(speed)

    def rightspin(self, speed):
        self.left_wheel.forward(speed)
        self.right_wheel.backward(speed)

    def left(self, speed):
        self.left_wheel.stop()
        self.right_wheel.forward(speed)

    def right(self, speed):
        self.left_wheel.forward(speed)
        self.right_wheel.stop()

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()

    def shutdown(self):
        self.stop()
        gpio.cleanup()
    
    def reset(self):
        self.shutdown()
        self.__init__()
