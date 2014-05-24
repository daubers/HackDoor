import serial
from threading import Thread


class rfid_reader(Thread):
    """
        This class describes an rfid reader on a serial port
        The port should just return
    """
    def __init__(self, port, baud):
        super(rfid_reader, self).__init__()
        self.ser = serial.Serial(port, baud, timeout=5)
        self.running = False
        self.subscribers = []

    def run(self):
        while self.running:
            pass

    def start(self):
        self.running = True
        super(rfid_reader, self).start()

    def stop(self):
        self.running = False
        


