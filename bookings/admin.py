from django.contrib import admin
from .models import TrainingSession


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('author', 'session_date', 'session_time')
    search_fields = ('author__username', 'session_date')
    list_filter = ('session_date',)
