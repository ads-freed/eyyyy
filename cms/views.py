from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def dashboard(request):
    context = {
        'ticket_count': 100,  # Replace with dynamic data
        'agent_count': 10,
    }
    return render(request, 'cms/dashboard.html', context)
