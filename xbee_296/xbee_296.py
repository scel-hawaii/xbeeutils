from xbee import ZigBee
import struct
import json
import serial
import datetime
import logging

# Load configuration
config = {}
with open('config.json') as data_file:
    config = json.load(data_file)


serial_port = config['serial_port']
baud_rate = config['baud_rate']

# Set our unpack format. See page for more details:
# https://docs.python.org/2/library/struct.html
unpack_fmt = '<HHIHHIhHH'
headers = [
                'schema',
                'address',
                'uptime_ms',
                'batt_mv',
                'panel_mv',
                'bmp185_press_pa',
                'bmp185_temp_decic',
                'humidity_centi_pct',
                'solar_irr_w_m2'
           ]

# Attempt to open the serial port
try:
    ser = serial.Serial(serial_port, baud_rate)
    xbee = ZigBee(ser, escaped=True)

except serial.serialutil.SerialException as e:
    print "Serial Error: ", e
    sys.exit(1)

# Keep doing this
while True:
    frame = xbee.wait_read_frame()
    rf_data = frame['rf_data']
    dlength = len(rf_data)
    timestamp = str(datetime.datetime.now())

    schema_num = struct.unpack('<H', rf_data[0:2])[0]

    print timestamp + " Data frame with length " + str(dlength) + " bytes was received."

    expected_len = 22
    if( dlength != expected_len):
        print "Recieved a packet with a wrong data length"
        print "Expected: ", expected_len
        print "Received : ", dlength
        print "Make sure that your schema is correct in the firmware"
        break

    expected_schema = 296
    if( schema_num != expected_schema):
        print "Recieved a packet with a wrong schema number"
        print "Expected: ", expected_schema
        print "Received : ", schema_num
        print "Make sure that you set your schema correctly."
        break

    udata = struct.unpack(unpack_fmt, rf_data)
    print timestamp + " Data unpacked: " + str(udata)

    pdata = dict(zip(headers, udata))
    print timestamp + " Data processed: " + str(pdata)

