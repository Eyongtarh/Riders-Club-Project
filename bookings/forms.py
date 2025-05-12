from django import forms
from .models import Booking
from datetime import date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select a date'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'Select a time'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add any notes (optional)'
            })
        }

    def clean_date(self):
        date_field = self.cleaned_data['date']
        if date_field < date.today():
            raise forms.ValidationError("Cannot book in the past.")
        return date_field
