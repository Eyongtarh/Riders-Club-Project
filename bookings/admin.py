from django.contrib import admin
from .models import AvailableSlot, Booking


@admin.register(AvailableSlot)
class AvailableSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'location')
    list_filter = ('date', 'location')
    search_fields = ('location',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'slot__location')
