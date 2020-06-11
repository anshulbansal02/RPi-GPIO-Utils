import pigpio

pi = pigpio.pi()

class MotorControl:
    def __int__(self, pins, in1, in2, in3, in4, enA, enB):
        """
        Initialize the MotorControl Object with 4 control Gpio and 2 PWM Gpio.
        (in1, in2, in3, in4, enA, enB)
        """

        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.enA = enA
        self.enB = enB


    def setMode(self):
        """
        Implicitly calls set_mode(pin, mode) of pigpio library on
        all pins for abstraction and less code.
        """

        pi.set_mode(self.in1, pigpio.OUTPUT)
        pi.set_mode(self.in2, pigpio.OUTPUT)
        pi.set_mode(self.in3, pigpio.OUTPUT)
        pi.set_mode(self.in4, pigpio.OUTPUT)
        pi.set_mode(self.enA, pigpio.OUTPUT)
        pi.set_mode(self.enB, pigpio.OUTPUT)


    def run(self, m1, m2, threshold):
        """
        Runs both motor with speed m1 and m2 having a threshold value.
        The threshold value prevents humming of motor at lower duty_cycle/Speed.
        """

        if m1 == 0 and m2 == 0:
            pi.clear_bank_1((1 << self.in1) | (1 << self.in2) | (1 << self.in3) | (1 << self.in4))
        else: 
            if m1 > 0:
                pi.write(self.in1, 1)
                pi.write(self.in2, 0)
            elif m1 < 0:
                pi.write(self.in2, 1)
                pi.write(self.in1, 0)

            if m2 > 0:
                pi.write(self.in3, 1)
                pi.write(self.in4, 0)
            elif m2 < 0:
                pi.write(self.in3, 1)
                pi.write(self.in4, 0)

        speed1 = (255-threshold) * (abs(m1)/50) + threshold if abs(m1) > 0 else 0    #threshold - 255
        speed2 = (255-threshold) * (abs(m2)/50) + threshold if abs(m2) > 0 else 0

        pi.set_PWM_dutycycle(self.pwm1, speed1)    
        pi.set_PWM_dutycycle(self.pwm2, speed2)     




