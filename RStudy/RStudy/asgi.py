import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RStudy.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # 'websocket': AuthMiddlewareStack(
    #     URLRouter(
    #         forum.routing.websocket_urlpatterns
    #     )
    # )
    # "websocket": AllowedHostsOriginValidator(
    #         AuthMiddlewareStack(URLRouter(forum.routing.websocket_urlpatterns))
    #     ),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})