from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'input-field', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class' : 'input-field', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }