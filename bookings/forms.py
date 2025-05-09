from django import forms
from .models import TrainingSession
from django.core.exceptions import ValidationError
from datetime import date


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'session_date', 'session_time', 'notes', 'excerpt']

    def clean_session_date(self):
        session_date = self.cleaned_data.get('session_date')
        if session_date and session_date < date.today():
            raise ValidationError('Cannot book in the past.')
        return session_date
