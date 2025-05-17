from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    A form for creating and updating Booking instances.

    This form is based on the Booking model and includes fields for:
        - slot: The time slot for the booking.
        - notes: Additional information or comments about the booking.
        - status: The current status of the booking (e.g., confirmed, pending).

    Widgets:
        - 'notes' uses a Textarea with 3 rows for better UX.
        - 'status' uses a dropdown Select widget for status selection.
    """

    class Meta:
        model = Booking
        fields = ['slot', 'notes', 'status']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(),
        }
