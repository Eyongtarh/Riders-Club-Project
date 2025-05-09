from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'created_at')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'notes')
