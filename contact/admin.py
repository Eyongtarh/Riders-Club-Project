from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    This is the dmin interface customization for the ContactMessage
    model for list_display and search_fields.
    """
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
