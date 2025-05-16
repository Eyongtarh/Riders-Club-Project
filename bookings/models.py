from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class AvailableSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'time', 'location'],
                name='unique_slot'
            )
        ]
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.date} at {self.time} in {self.location}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='bookings')
    slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE,
                             related_name='bookings')
    notes = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['slot', 'user'],
                name='unique_user_slot_booking'
            )
        ]
        ordering = ['-created_at']

    def clean(self):
        super().clean()

        if self.slot.date < timezone.now().date():
            raise ValidationError({'slot': 'Cannot book a past slot.'})

        # Check if slot is already booked
        if Booking.objects.filter(slot=self.slot).exclude(pk=self.pk).exists():
            raise ValidationError({'slot':
                                   'This slot has already been booked.'})

    def __str__(self):
        return f"{self.user.username} - {self.slot}"
