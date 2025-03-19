from django import forms
from .models import Ticket
from ckeditor.widgets import CKEditorWidget

class TicketForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'tags', 'attachment']
