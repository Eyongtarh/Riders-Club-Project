from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date as session_date

# Create your models here.


class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.TimeField()
    notes = models.TextField(blank=True)

    def clean(self):
        if self.session_date < session_date.today():
            raise ValidationError({'date': 'Cannot book in the past.'})

    def __str__(self):
        return f"{self.user.username} - {self.session_date}"
