from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name='session_list'),
    path('create/', views.session_create, name='session_create'),
    path('edit/<int:pk>/', views.session_update, name='session_update'),
    path('delete/<int:pk>/', views.session_delete, name='session_delete'),
]
