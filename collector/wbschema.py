# schema.py
import json
import sys


fmt = ''

def get_fmt():
    return unpack_fmt

def get_headers():
    return headers

try:
    with open('schema.json') as data_file:
        fmt = json.load(data_file)

    unpack_fmt = '<'
    for f in fmt:
        unpack_fmt += f['size']*f['instance'];
    print unpack_fmt

    headers = []
    for d in fmt:
        headers.append(d['name'])
    print headers


except IOError as e:
    print e
    print "There was a file error. Did you remember to create a schema.json file?"
    sys.exit(1)

