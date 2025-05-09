from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'notes']

    def clean_date(self):
        date_field = self.cleaned_data['date']
        if date_field < date.today():
            raise forms.ValidationError("Cannot book in the past.")
        return date_field
