from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """
    A Django ModelForm for handling contact messages.

    This form maps to the ContactMessage model and includes
    the fields for the user's name, email, and message content.
    """

    class Meta:
        """
        Metadata for the ContactMessageForm.

        Specifies the model to use (ContactMessage) and the fields
        that should be included in the form.
        """
        model = ContactMessage
        fields = ['name', 'email', 'message']
