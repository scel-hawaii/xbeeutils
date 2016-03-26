# schema.py
import json
import sys

schemas = {}
schema_nums = []

def load_schemas():
    global schemas
    global schema_nums
    with open('schema.json') as data_file:
        schemas = json.load(data_file)
        schema_nums = schemas.keys()
    # print schemas
    print schemas['97']
    schema_nums = schemas.keys()
    print schemas.keys()

    for s in schema_nums:
        unpack_fmt = '<'
        fmt = schemas[s]['format']
        for f in fmt:
            unpack_fmt += f['size']*f['instance'];
        schemas[s]['unpack_fmt'] = unpack_fmt

    for s in schema_nums:
        headers = []
        fmt = schemas[s]['format']
        for f in fmt:
            headers.append(f['name'])
        schemas[s]['headers'] = headers

try:
    load_schemas()


except IOError as e:
    print e
    print "There was a file error. Did you remember to create a schema.json file?"
    sys.exit(1)

def get_schema(schema_num):
    global schemas
    global schema_nums
    return schema[schema_num]

# Check if a schema number is defined
def contains(schema_num):
    global schemas
    global schema_nums
    s = str(schema_num)
    if s in schema_nums:
        return True
    else:
        return False

def get_headers(schema_num):
    global schemas
    global schema_nums
    s = str(schema_num)
    return schemas[s]['headers']

def get_fmt(schema_num):
    global schemas
    global schema_nums
    s = str(schema_num)
    return schemas[s]['unpack_fmt']


'''
    unpack_fmt = '<'
    for f in fmt:
        unpack_fmt += f['size']*f['instance'];
    print unpack_fmt

    headers = []
    for d in fmt:
        headers.append(d['name'])
    print headers
'''

if __name__ == '__main__':
    print "Finished loading schemas"
    print schemas

