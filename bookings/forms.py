from django import forms
from .models import TrainingSession


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['session_date', 'session_time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class':
                                           'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class':
                                           'form-control'}),
        }
