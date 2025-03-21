from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('<str:room_name>/', views.chat_room, name='chat_room'),
    path('', views.chat_room, name='chat_room_default'),
]
