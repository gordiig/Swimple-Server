from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    ONLINE_GROUP_NAME = 'online'

    def connect(self):
        print('Connect')
        async_to_sync(self.channel_layer.group_add)(
            ChatConsumer.ONLINE_GROUP_NAME,
            self.channel_name
        )
        print('Added to online')
        self.accept()

    def disconnect(self, code):
        print('Disconnect')
        async_to_sync(self.channel_layer.group_discard)(
            ChatConsumer.ONLINE_GROUP_NAME,
            self.channel_name
        )
        print('Deleted from online')

    def receive(self, text_data):
        incame_data = json.loads(text_data)
        print(incame_data)
        self.send(text_data=text_data)