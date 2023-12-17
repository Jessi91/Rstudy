from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connecter l'utilisateur au WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Déconnecter l'utilisateur du WebSocket
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enregistrer le message dans ParticipationForum

        # Envoyer le message à tous les utilisateurs connectés
        await self.send(text_data=json.dumps({
            'message': message
        }))
