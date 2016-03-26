from xbee import ZigBee
import serial
import time

ser = serial.Serial('/dev/ttyUSB1', 9600)
xbee = ZigBee(ser, escaped=True)

while True:
    # xbee.tx(dest_addr='\x9F\x7A', dest_addr_long='\x00\x00\x00\x00\x00\x00\xFF\xFF', data='Hello World')
    xbee.tx(dest_addr='\x00\x00', dest_addr_long='\x00\x00\x00\x00\x00\x00\x00\x00', data='Hello BOB')
    # Wait for and get the response
    # print(xbee.wait_read_frame())
    # ser.close()
    time.sleep(1);
