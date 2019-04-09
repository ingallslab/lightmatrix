import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'
ser.open()
ser.readline()
ser.write(bytes("<15,3,10,100>", 'utf-8'))
ser.close()
