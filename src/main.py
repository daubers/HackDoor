from wsmain import WSHandler
import tornado
import rfid_reader as rfid

rfidthread = rfid.rfid_reader("/dev/ttyUSB0", 9600)
rfidthread.setDaemon(True)
rfidthread.start()

application = tornado.web.Application([
    (r'/ws', WSHandler, {"rfidthread": rfidthread}),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()