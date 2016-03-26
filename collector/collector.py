# collector.py
#
# A simpler xbee data collection script.
#

import datetime
import struct
import wbschema
import wbxbee

queue = []

def print_log(message):
    print datetime.datetime.now().time(), message

def parse(data_frame):
    data = data_frame['rf_data']
    # print 'Data length: ' + str(len(data))
    schema = struct.unpack('<H', data[0:2])[0]

    if(schema == 3):
        struct_fmt = wbschema.get_fmt()
        headers = wbschema.get_headers()

        values = struct.unpack(struct_fmt, data);
        d = dict(zip(headers, values))
    else:
        queue.append(data)
        print_log("[Warning] Unknown packet type detected")
        print_log("[Data] " + str(data))

def store_db(data):
    print_log("Storing Data")
    return True

# Continuously read and print packets
while True:
    try:
        response = wbxbee.get_data()
        data = parse(response)
    except KeyboardInterrupt:
        break

ser.close()
