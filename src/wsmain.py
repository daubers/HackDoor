from tornado import websocket


class WSHandler(websocket.WebSocketHandler):
    def __init__(self, application, request, rfidthread):
        super(WSHandler, self).__init__(application, request)
        self.rfidthread = rfidthread

    def open(self):
        self.rfidthread.subscribe(lambda x: self.write_message(x))

    def on_message(self, message):
        pass

    def send_message(self, message):
        self.write_message(message)

    def on_close(self):
        pass

