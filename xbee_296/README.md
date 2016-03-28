Helps you verify your xbee is sending the correct data.
Make sure to copy config.json.bak to config.json before you start the program.

# To run

`python xbee_296.py`


# Where to use this program

You can use one of the lab computers, or attempt to get it working on your computer.
I don't have instructions for windows or mac so help the other students by submitting
instructions if you figure out how to set it up.

# Which port?

Uplug your USB explorer board and plug it back in.
On linux, type 'dmesg'. You should see something like `/dev/ttyUSB0".`
in the lines of text closest to the bottom.

# Expected behavior

This program will fail in two places:

1. Your schema length is off from the specification.
2. Your schema number is defined wrong.
