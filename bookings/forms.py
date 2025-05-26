from django import forms
from .models import Booking, AvailableSlot


class BookingForm(forms.ModelForm):
    """
    This form is based on the booking model which includes
    fields for: slot, notes and status.

    The slot queryset excludes slots that are already booked
    with a pending or confirmed booking.
    """

    class Meta:
        model = Booking
        fields = ['slot', 'notes', 'status']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        unavailable_slots = Booking.objects.filter(
            status__in=[Booking.Status.PENDING, Booking.Status.CONFIRMED]
        ).values_list('slot_id', flat=True)

        self.fields['slot'].queryset = (
            AvailableSlot.objects.exclude(id__in=unavailable_slots)
        )
