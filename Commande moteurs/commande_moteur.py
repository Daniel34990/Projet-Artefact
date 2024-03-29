from adafruit_motorkit import MotorKit
kit = MotorKit(0x40)
import time

# Forward at full throttle
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
# A 1.0 second sleep pauses the code while
# motors are running. After 1.0 sec., the
# lines after sleep will set throttle to zero,
# effectively turning the motor off.
time.sleep(1.0)
# Stop & sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)

# Right at half speed
kit.motor1.throttle = 0.5
kit.motor2.throttle = -0.5
# let motors run for 2.0 seconds.
time.sleep(2.0)
# Stop. Sleep for 3 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(3.0)

# Backward at 3/4 speed
kit.motor1.throttle = -0.75
kit.motor2.throttle = -0.75
# let motors run for 2.5 seconds
time.sleep(2.5)
# Stop. Sleep for 1 sec.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
time.sleep(1.0)

# Forward rt at full speed, backward left at 1/4 speed
kit.motor1.throttle = 1.0
kit.motor2.throttle = -0.25
# let motors run for 3 seconds
time.sleep(3.0)
# Stop. No need for a sleep here because we're done.
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0
