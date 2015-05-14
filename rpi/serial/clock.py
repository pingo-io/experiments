import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600)
time.sleep(.5)  # wait for display to boot up

def clear():
    ser.write(chr(254))
    ser.write(chr(128))
    ser.write(' ' * 32)
    
def pos(line=0, column=0):
    first_pos = (128, 192)
    ser.write(chr(254))
    code = first_pos[line] + column
    ser.write(chr(code))

clear()

while True:
    pos()
    ser.write(time.strftime('%H:%M:%S'))
    time.sleep(1)
