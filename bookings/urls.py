from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name='session_list'),
    path('new/', views.session_create, name='session_create'),
    path('<int:pk>/edit/', views.session_update, name='session_update'),
    path('<int:pk>/delete/', views.session_delete, name='session_delete'),
]
