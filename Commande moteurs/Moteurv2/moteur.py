pwm = PCA9685(0x40, debug=True)

pwm.setPWMFreq(50)


class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4
Motor = MotorDriver()


pwm.setDutycycle(self.PWMA, speed)

pwm.setLevel(self.AIN1, 1)

Motor.MotorRun(0, 'forward', 0)

