from django import forms
from .models import Note
from .models import ContactMessage


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fullname', 'email', 'message']