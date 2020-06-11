import pigpio
from time import sleep

in1 = 26
in2 = 13
in3 = 6
in4 = 5
enA = 24
enB = 23

pi = pigpio.pi()

pi.set_mode(in1, pigpio.OUTPUT)
pi.set_mode(in2, pigpio.OUTPUT)
pi.set_mode(in3, pigpio.OUTPUT)
pi.set_mode(in4, pigpio.OUTPUT)
pi.set_mode(enA, pigpio.OUTPUT)
pi.set_mode(enB, pigpio.OUTPUT)

def move():
    pi.write(in1, 0)
    pi.write(in2, 1)
    pi.write(in3, 0)
    pi.write(in4, 1)
    for i in range(255, 50, -25):
        print(i)
        if i == 205:
            pi.write(in1, 1)
            pi.write(in2, 0)
            pi.write(in3, 1)
            pi.write(in4, 0)
            pi.set_PWM_dutycycle(enA, 255)
            pi.set_PWM_dutycycle(enB, 255)
            sleep(1)
            continue
        pi.set_PWM_dutycycle(enA, i)
        pi.set_PWM_dutycycle(enB, i)
        sleep(1)
    pi.set_PWM_dutycycle(enA, 0)
    pi.set_PWM_dutycycle(enB, 0)
    pi.write(in1, 0)
    pi.write(in2, 0)
    pi.write(in3, 0)
    pi.write(in4, 0)

try:
    move()
except KeyboardInterrupt:
    pi.stop()
finally:
    pi.stop()
