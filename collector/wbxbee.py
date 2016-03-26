from xbee import ZigBee
import sys
import serial


def get_data():
    return xbee.wait_read_frame()

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    xbee = ZigBee(ser, escaped=True)
except serial.serialutil.SerialException as e:
    print "Serial Error: ", e
    sys.exit(1)


