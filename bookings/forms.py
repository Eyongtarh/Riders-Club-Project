from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    This form is based on the booking model which includes
    fields for: slot, notes and status.

    Widgets applied here contains notes and status.
    """

    class Meta:
        model = Booking
        fields = ['slot', 'notes', 'status']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(),
        }
