from wsmain import WSHandler
from tornado import web, httpserver, ioloop
import rfid_reader as rfid

rfidthread = rfid.rfid_reader("/dev/ttyUSB0", 9600)
rfidthread.setDaemon(True)
rfidthread.start()

application = web.Application([(r'/ws', WSHandler, {"rfidthread": rfidthread}), ])


if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()