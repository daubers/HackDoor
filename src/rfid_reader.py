import serial, sys
from threading import Thread


class rfid_reader(Thread):
    """
        This class describes an rfid reader on a serial port
        The port should just return
    """
    def __init__(self, port, baud):
        super(rfid_reader, self).__init__()
        try:
            self.ser = serial.Serial(port, baud, timeout=5)
        except serial.SerialException, e:
            print e.message
            sys.exit()
        self.running = False
        self.subscribers = []

    def run(self):
        while self.running:
            if self.ser.inWaiting()>0:
                data = self.ser.readline()
                for subscriber in self.subscribers:
                    subscriber(data.strip("\n"))
    def start(self):
        self.running = True
        super(rfid_reader, self).start()

    def stop(self):
        self.running = False

    def subscribe(self, subobject):
        self.subscribers.append(subobject)

    def unsubscribe(self, subobject):
        self.subscribers.remove(subobject)



