from xbee import ZigBee
import struct
import json
import serial
import datetime

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

    print timestamp + " Data frame with length " + str(dlength) + " was received."
