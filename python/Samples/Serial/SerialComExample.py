#Matthew Moran 09/16/2024
#Serial Communication sample, useful for communicationg with arduino boards via serial ports.

import serial

#The communication baudrate, the board and program need to match to communicate properly
BAUDRATE = 9600

#Port to communicate to the board with, this needs to be on the correct port the board is connected too.
PORT = 'COM7'

#Define Serial Communication
serial = serial.Serial(PORT, BAUDRATE)

#Send a char over serial....
serial.write(bytearray('S', 'ascii'))

#Recieve over serial.
while True:
    from_serial = serial.readline()
    print(from_serial)

    

