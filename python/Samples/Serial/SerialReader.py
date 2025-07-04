import serial

#Define Baudrate
BAUDRATE = 115200
#Define Communication Port
PORT = 'COM7'

#Create Serial 
serial = serial.Serial(PORT, BAUDRATE)