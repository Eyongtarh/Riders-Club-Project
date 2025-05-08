from django import forms
from .models import TrainingSession


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['session_date', 'session_time', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['session_date'].widget.attrs.update({'type': 'date'})
        self.fields['session_time'].widget.attrs.update({'type': 'time'})
