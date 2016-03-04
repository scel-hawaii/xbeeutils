import serial
from datetime import datetime
import msvcrt
from xbee import ZigBee

def transmit_data():
    print "Input data to transmit"
    send_str = raw_input()
    xbee.send("tx",data= send_str,dest_addr_long=DEST_ADDR_LONG,dest_addr=DEST_ADDR_SHORT)
    

def print_data(data):
    #check against frame id type
    #only print if it's an rx
    if( data['id'] == 'rx'):
        current_time = str(datetime.now())
        current_time = current_time[11:-7]
        print "Timestamp: " + current_time + " , " + data['rf_data']
    
if __name__ == '__main__':
    '''
    #Xbee (Router to Coordinator) Macros
    PORT = 5
    BAUD_RATE = 9600
    #64-bit addr
    DEST_ADDR_LONG = "\x00\x00\x00\x00\x00\x00\x00\x00"
    #16-bit addr
    DEST_ADDR_SHORT = "\x00\x00"
    '''
    
    #Xbee (Coordinator to Router) Macros
    PORT = 3
    BAUD_RATE = 9600
    #64-bit addr
    DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xE6\x72\xD8"
    #16-bit addr
    DEST_ADDR_SHORT = "\xD4\x9D"

    # Open serial port
    ser = serial.Serial(PORT, BAUD_RATE)

    # Create API object
    xbee= ZigBee(ser, callback = print_data);

    print "Enter command"
    print "T for transmit mode or E to exit"
    while(True):
        #when any key is hit
        if msvcrt.kbhit():
            menu_input = msvcrt.getch()
            #check key pressed
            if menu_input == "e" or menu_input == "E":
                #exit program
                break
            elif menu_input == "t" or menu_input == "T":
                transmit_data()
            else:
                print "Invalid command. T for transmit mode or E to exit"
    
    ser.close()
