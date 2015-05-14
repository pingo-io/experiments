import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600)
time.sleep(.5)  # wait for display to boot up

ser.write(chr(254))
ser.write(chr(128))
ser.write(' ' * 32)
ser.write(chr(254))
ser.write(chr(128))
ser.write('Hello')
