from django.contrib import admin
from .models import TrainingSession


class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('author', 'session_date', 'session_time', 'notes')
    search_fields = ['author__username', 'session_date']


admin.site.register(TrainingSession, TrainingSessionAdmin)
