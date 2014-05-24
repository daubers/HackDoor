__author__ = 'matt'

import src.rfid_reader as rfid

def printit(message):
    print(message)

test = rfid.rfid_reader("/dev/ttyUSB0", 9600)
test.subscribers.append(printit)
test.start()