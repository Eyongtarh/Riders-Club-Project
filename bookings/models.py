from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class AvailableSlot(models.Model):
    """
    Represents an available booking slot for a user. This includes the date,
    time, and location of the slot. The slot is unique based on these three
    fields.

    Attributes:
        date (DateField): The date of the available slot.
        time (TimeField): The time of the available slot.
        location (CharField): The location where the slot is available.

    Meta:
        constraints (UniqueConstraint): Ensures no two slots have the
        same date, time, and location.
        ordering (list): Orders slots first by date, then by time.
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
        """
        Returns a string representation of the AvailableSlot instance,
        combining the date, time, and location.
        """
        return f"{self.date} at {self.time} in {self.location}"


class Booking(models.Model):
    """
    Represents a booking made by a user for a specific available slot.
    It includes the status of the booking, user, notes, and the related slot.

    Attributes:
        user (ForeignKey): The user who made the booking.
        slot (ForeignKey): The available slot that is being booked.
        notes (TextField): Optional additional notes for the booking.
        created_at (DateTimeField): The timestamp when the booking was created.
        status (IntegerField): The current status of the booking (pending,
        confirmed, or cancelled).

    Meta:
        constraints (UniqueConstraint): Ensures a user can only book a
        specific slot once. ordering (list): Orders bookings by creation
        date in descending order.
    """
    class Status(models.IntegerChoices):
        """
        Defines the possible statuses of a booking.

        PENDING: The booking is pending confirmation.
        CONFIRMED: The booking has been confirmed.
        CANCELLED: The booking has been cancelled.
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
        constraints = [
            models.UniqueConstraint(
                fields=['slot', 'user'],
                name='unique_user_slot_booking'
            )
        ]
        ordering = ['-created_at']

    def clean(self):
        """
        Custom validation for the booking instance. Checks that:
        1. The slot date is not in the past.
        2. The slot is not already booked by another user.
        """
        if self.slot.date < timezone.now().date():
            raise ValidationError({'slot': 'Cannot book a past slot.'})

        # Check if slot is already booked
        if Booking.objects.filter(slot=self.slot).exclude(pk=self.pk).exists():
            raise ValidationError({'slot':
                                   'This slot has already been booked.'})

    def __str__(self):
        """
        Returns a string representation of the Booking instance,
        combining the user's username and the slot details.
        """
        return f"{self.user.username} - {self.slot}"
