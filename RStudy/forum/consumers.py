import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

# Aucun besoin d'importer json deux fois
# Il est préférable de regrouper tous les imports ensemble en haut du fichier

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room

        # Ajout au groupe de discussion
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        # Modification de 'event' en 'text_data' pour une meilleure clarté
        print('receive', text_data)
        received_data = json.loads(text_data)
        msg = received_data.get('message')
        if not msg:
            return  # Utilisation de 'return' seul pour quitter la fonction si 'msg' est vide

        response = {
            'message': msg
        }
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'message': json.dumps(response)
            }
        )

    async def chat_message(self, event):
        # Méthode pour gérer l'envoi de messages au groupe
        message = event['message']

        # Envoi du message au WebSocket
        await self.send(text_data=message)

    async def disconnect(self, close_code):
        # Quitter le groupe de discussion
        await self.channel_layer.group_discard(self.chat_room, self.channel_name)
