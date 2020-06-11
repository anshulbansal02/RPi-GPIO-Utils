import pigpio
import time
import socket
import sys
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.0.110", 5555))


pi = pigpio.pi()
#pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)

try:
    while True:
        data, server = sock.recvfrom(4096)
        values = re.findall(r"[-+]?\d*\.\d+|\d+", str(data))
        z = abs(float(values[1]))
        x = abs(float(values[0]))
        angleZ = z / (1/180)
        angleX = x / (1/180)
        dutyZ = int((angleZ/0.09)) + 500
        dutyX = int((angleX/0.09)) + 500

        print(f'z: {z}  angleZ: {angleZ}  dutyZ: {dutyZ}')
        print(f'x: {x}  angleX: {angleX}  dutyX: {dutyX}')

        pi.set_servo_pulsewidth(17, dutyX)
        pi.set_servo_pulsewidth(18, dutyZ)


except KeyboardInterrupt:
    pi.stop()
    sock.close()
finally:
    pi.stop()
    sock.close()

'''
ISSUES: 
1. Sensor data was inconsistant, so it crashes. 
2. Sensor data was mixed, so the pan-tilt servos were behaving abnormal. Figured out with relative orientation sensor data.
3. Moreover the data will be streamed from Websockets (socket.io)
'''
