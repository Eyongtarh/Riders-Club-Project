from django.contrib import admin
from .models import AvailableSlot, Booking


@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    """
    This computes the display of AvailableSlot entries in the
    Django admin panel for list_display, list_filter and search_fields.
    """
    list_display = ('date', 'time', 'location')
    list_filter = ('date', 'location')
    search_fields = ('location',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    This customizes the display of Booking entries in the Django
    admin panel. These entries are: list_display, list_filter,
    and search_fields,
    """
    list_display = ('user', 'slot', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'slot__location')
