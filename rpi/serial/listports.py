import serial

for i in range(4):
    try:
        ser = serial.Serial(i)
    except OSError as ex:
        print 'not found:', ex.filename
    else:
        print i, ser.name

