from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('bookings/', include(('bookings.urls', 'bookings'),
                              namespace='bookings')),
]
