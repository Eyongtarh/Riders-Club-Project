from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """
    This form maps to the ContactMessage model and includes
    the fields for the user's name, email, and message content.
    """

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
