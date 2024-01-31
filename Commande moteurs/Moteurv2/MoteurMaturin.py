

import RPi.GPIO as GPIO

class Mot:
    def __init__(self,A,B,E):
        GPIO.setup(A,GPIO.OUT)
        GPIO.setup(B,GPIO.OUT)
        GPIO.setup(E,GPIO.OUT)
        self.A = A
        self.B = B
        self.E = E
        self.pwm = GPIO.PWM(E,100)
        self.pwm.start(0)
        GPIO.output(self.E,GPIO.LOW)

    def avancer(self):
        GPIO.output(self.E,GPIO.HIGH)
        GPIO.output(self.A,GPIO.LOW)
        GPIO.output(self.B,GPIO.HIGH)

    def reculer(self):
        GPIO.output(self.E,GPIO.HIGH)
        GPIO.output(self.A,GPIO.HIGH)
        GPIO.output(self.B,GPIO.LOW)


    def vitesse(self,pourcentage):
        self.pwm.ChangeDutyCycle(pourcentage)

