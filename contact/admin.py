from django.contrib import admin
from .models import ContactMessage

# Registering the ContactMessage model in Django Admin with
# a custom admin interface


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the ContactMessage model.

    - list_display: Fields displayed in the model list view.
    - search_fields: Fields that are searchable in the admin.
    """
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
