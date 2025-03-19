from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

PRIORITY_CHOICES = (
    ('normal', 'Normal'),
    ('high', 'High'),
    ('critical', 'Critical'),
    ('urgent', 'Urgent'),
)

STATUS_CHOICES = (
    ('open', 'Open'),
    ('in_progress', 'In Progress'),
    ('closed', 'Closed'),
)

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tickets_created', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tickets_assigned', on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='normal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to='ticket_attachments/', null=True, blank=True)

    def __str__(self):
        return self.title
