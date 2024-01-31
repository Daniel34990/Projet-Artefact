from adafruit_motorkit import MotorKit
kit = MotorKit(0x40)
import time


def stop_tot():
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

def forward(speed1,speed2) :
    kit.motor1.throttle = speed1
    kit.motor2.throttle = -speed2

def backward(speed1,speed2):
    kit.motor1.throttle = -speed1
    kit.motor2.throttle = speed2

def left(speed):
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed

def right(speed):
    kit.motor1.throttle = -speed
    kit.motor2.throttle = -speed
