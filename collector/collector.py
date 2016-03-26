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
    print "[" + str(datetime.datetime.now().time()) + "]", message

def parse(data_frame):
    data = data_frame['rf_data']
    schema = struct.unpack('<H', data[0:2])[0]
    data_len = len(data)

    print_log("[Packet]\t Got data of length " + str(data_len) + " and schema " + str(schema))

    if(wbschema.contains(schema)):
        unpack_fmt = wbschema.get_fmt(schema)
        headers = wbschema.get_headers(schema)

        print_log("[Message]\t We know about this packet.")
        print_log("[Message]\t Unpack format: " + unpack_fmt)

        values = struct.unpack(unpack_fmt, data)
        d = dict(zip(headers, values))
        print_log("[Packet]\t End Packet")
        print ""
    else:
        print_log("[Warning]\t Unknown packet type detected")
        print_log("[Data]\t " + str(data))
        print ""

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
