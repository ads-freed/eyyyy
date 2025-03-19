from django.contrib import admin
from .models import EmailLog, NotificationLog, ErrorLog, LoginHistory

admin.site.register(EmailLog)
admin.site.register(NotificationLog)
admin.site.register(ErrorLog)
admin.site.register(LoginHistory)
