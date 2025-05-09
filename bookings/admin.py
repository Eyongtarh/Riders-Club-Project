from django.contrib import admin
from .models import TrainingSession


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'session_date', 'session_time')
    search_fields = ('title', 'author__username')
    list_filter = ('session_date',)
