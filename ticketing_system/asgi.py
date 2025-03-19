import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing  # if you add a routing file for chat

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketing_system.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Uncomment and complete the following for WebSocket support:
    # "websocket": URLRouter(chat.routing.websocket_urlpatterns),
})
