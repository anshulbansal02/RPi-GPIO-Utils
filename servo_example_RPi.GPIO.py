import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(12, gpio.OUT)
p = gpio.PWM(12, 50)

p.start(0)

'''
try:
    while True:
        angle = int(input("Angle: "))
        duty = (angle / 18) + 2
        p.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()
'''

try:
    while True:
        for i in range(181):
            duty = int((i/18)) + 2
            p.ChangeDutyCycle(duty)
            time.sleep(0.04)
        for k in range(180, -1,-1):
            duty = int((k/18)) + 2
            p.ChangeDutyCycle(duty)
            time.sleep(0.04)

except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()

finally:
    p.stop()
    gpio.cleanup()
