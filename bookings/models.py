from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class AvailableSlot(models.Model):
    """
    This represents an available booking slot for a user. This includes
    the date, time, and location of the slot. The slot is unique based
    on these three fields.

    The Meta class constraints (UniqueConstraint) ensures no two slots have the
    same date, time, and location.

    The ordering, orders slots first by date, then by time.
    """
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
    """
    This outlays a booking made by a user for a specific available slot.
    It includes the status of the booking, user, notes, and the related slot.

    The constraints (UniqueConstraint) here verifies that a user can only
    book a specific slot once.

    The ordering (list), orders bookings by creation date in descending order.
    """
    class Status(models.IntegerChoices):
        """
        This defines the possible statuses of a booking.
        """
        PENDING = 0,
        CONFIRMED = 1,
        CANCELLED = 2,

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='bookings')
    slot = models.ForeignKey(AvailableSlot, on_delete=models.CASCADE,
                             related_name='bookings')
    notes = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices,
                                 default=Status.PENDING)

    class Meta:

        ordering = ['-created_at']

    def clean(self):
        """
        This validation checks that:
        1. The slot date is not in the past.
        2. The slot is not already booked by another user.
        """
        if not self.slot:
            raise ValidationError({'slot':
                                   'A booking must have a valid slot.'})

        if self.slot.date < timezone.now().date():
            raise ValidationError({'slot': 'Cannot book a past slot.'})

        if Booking.objects.filter(slot=self.slot).exclude(pk=self.pk).exists():
            raise ValidationError({'slot':
                                   'This slot has already been booked.'})

    def __str__(self):
        return f"{self.user.username} - {self.slot}"
