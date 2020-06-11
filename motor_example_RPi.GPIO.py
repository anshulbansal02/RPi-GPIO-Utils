import RPi.GPIO as GPIO
from time import sleep

in1 = 37
in2 = 33
in3 = 31
in4 = 29
enA = 18
enB = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

pA=GPIO.PWM(enB,1000)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pA.start(0)


def move():
    GPIO.output(in4, GPIO.HIGH)
    for i in range(10, 4, -1):
        pA.ChangeDutyCycle(i*10)
        print(i*10)
        sleep(1)
        
    GPIO.output(in4,GPIO.LOW)


try:
    move()
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()