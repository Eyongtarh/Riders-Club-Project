from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time')  # Prevent double booking

    def clean(self):
        # Ensure the booking date is today or in the future
        if self.date < date.today():
            raise ValidationError({'date': 'Cannot book in the past.'})

    def __str__(self):
        return f"{self.user.username} - {self.date} at {self.time}"
