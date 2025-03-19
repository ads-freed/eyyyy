from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('email/', views.email_logs, name='email_logs'),
    path('notifications/', views.notification_logs, name='notification_logs'),
    path('errors/', views.error_logs, name='error_logs'),
    path('login_history/', views.login_history, name='login_history'),
]
