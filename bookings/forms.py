from django import forms
from .models import TrainingSession
from datetime import date


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['author', 'session_date', 'session_time', 'notes']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'session_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_session_date(self):
        session_date = self.cleaned_data.get('session_date')
        if session_date < date.today():
            raise forms.ValidationError('Cannot book in the past.')
        return session_date
