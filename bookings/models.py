from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import datetime


class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.TimeField()
    notes = models.TextField(blank=True, max_length=500)

    def clean(self):
        # Validate that the session date is not in the past
        if self.session_date < datetime.date.today():
            raise ValidationError({'session_date': 'Cannot book in the past.'})

    def __str__(self):
        return f"{self.user.username} - {self.session_date}"
