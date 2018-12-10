from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('Connect')
        self.accept()

    def disconnect(self, code):
        print('Disconnect')

    def receive(self, text_data):
        incame_data = json.loads(text_data)
        print(incame_data)
        self.send(text_data=text_data)