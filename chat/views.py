from django.shortcuts import render
from .models import ChatMessage
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request, room_name='global'):
    messages = ChatMessage.objects.filter(room=room_name).order_by('created_at')
    return render(request, 'chat/chat_room.html', {'messages': messages, 'room_name': room_name})
