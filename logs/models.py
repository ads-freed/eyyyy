from django.db import models
from django.conf import settings

class EmailLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipient = models.EmailField()
    subject = models.CharField(max_length=200)
    sent_at = models.DateTimeField(auto_now_add=True)

class NotificationLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ErrorLog(models.Model):
    error_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class LoginHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    login_time = models.DateTimeField(auto_now_add=True)
