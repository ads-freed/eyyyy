from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
