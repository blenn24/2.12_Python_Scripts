# Importing Libraries
import serial
import time
vel = 0
curv = 0
serv = 90
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

stage = 0

def send_command(velocity, curvature, servo_angle):
    msg = f"{velocity},{curvature},{servo_angle}\n".encode() # encode message as bytes
    arduino.write(msg)
    return

while(True):
    if(stage == 0):
        vel = 0.3

    if arduino.in_waiting > 0:
        response = arduino.readline().decode().strip()
        print("Received from Arduino:", response)
        send_command(vel,curv,serv)
    


