import tornado

class WSHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, rfidthread):
        super(WSHandler, self).__init__()
        self.rfidthread = rfidthread

    def open(self):
        self.rfidthread.subscribe(lambda x, lself=self: self.write_message(lself, x))

    def on_message(self, message):
        pass

    def send_message(self, message):
        self.write_message(message)

    def on_close(self):
        pass

