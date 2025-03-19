from django.shortcuts import render
from .models import EmailLog, NotificationLog, ErrorLog, LoginHistory
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@staff_member_required
def email_logs(request):
    logs = EmailLog.objects.all()
    return render(request, 'logs/email_logs.html', {'logs': logs})

@staff_member_required
def notification_logs(request):
    logs = NotificationLog.objects.all()
    return render(request, 'logs/notification_logs.html', {'logs': logs})

@staff_member_required
def error_logs(request):
    logs = ErrorLog.objects.all()
    return render(request, 'logs/error_logs.html', {'logs': logs})

@login_required
def login_history(request):
    logs = LoginHistory.objects.filter(user=request.user)
    return render(request, 'logs/login_history.html', {'logs': logs})
