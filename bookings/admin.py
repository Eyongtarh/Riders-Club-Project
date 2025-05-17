from django.contrib import admin
from .models import AvailableSlot, Booking


@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    """
    Admin configuration for AvailableSlot model.

    This class customizes the display of AvailableSlot entries in the
    Django admin panel.
    - list_display: Shows the date, time, and location of each slot.
    - list_filter: Enables filtering by date and location.
    - search_fields: Allows searching by location.
    """
    list_display = ('date', 'time', 'location')
    list_filter = ('date', 'location')
    search_fields = ('location',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Booking model.

    This class customizes the display of Booking entries in the Django
    admin panel.
    - list_display: Shows the user, slot, booking status, and creation
    timestamp.
    - list_filter: Enables filtering by status and creation date.
    - search_fields: Allows searching by username and slot location.
    """
    list_display = ('user', 'slot', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'slot__location')
