from django import forms
from .models import TrainingSession


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['session_date', 'session_time', 'notes']
