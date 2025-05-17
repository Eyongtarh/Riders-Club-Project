"""
URL configuration for the contact app.

This module defines the URL pattern for accessing the contact view.
"""

from django.urls import path
from .views import contact_view

urlpatterns = [
    # Route for the contact page
    path('contact/', contact_view, name='contact'),
]
