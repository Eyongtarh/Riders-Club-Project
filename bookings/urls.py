from django.urls import path
from . import views

"""
This module defines the URL pattern for accessing bookingListView,
bookingCreateView, bookingDetailView, bookingUpdateView, and
BookingDeleteView
"""

app_name = 'bookings'

urlpatterns = [
    path('', views.BookingListView.as_view(), name='booking_list'),
    path('create/', views.BookingCreateView.as_view(), name='booking_create'),
    path('<int:pk>/', views.BookingDetailView.as_view(),
         name='Booking_detail'),
    path('<int:pk>/update/', views.BookingUpdateView.as_view(),
         name='booking_update'),
    path('<int:pk>/delete/', views.BookingDeleteView.as_view(),
         name='booking_delete'),
]
