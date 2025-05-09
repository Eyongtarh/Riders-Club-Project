from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class TrainingSession(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.TimeField()
    notes = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)

    def clean(self):
        # Ensure the session date is today or in the future
        if self.session_date < date.today():
            raise ValidationError({'session_date': 'Cannot book in the past.'})

    def __str__(self):
        return f"{self.author.username} - {self.session_date}"
