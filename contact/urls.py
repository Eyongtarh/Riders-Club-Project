from django.urls import path
from .views import contact_view

"""
This module defines the URL pattern for accessing the contact view.
"""

urlpatterns = [
    # Route for the contact page
    path('contact/', contact_view, name='contact'),
]
