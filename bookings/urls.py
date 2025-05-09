from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_session_list, name='session_list'),
    path('create/', views.training_session_create, name='session_create'),
    path('<int:pk>/update/',
         views.training_session_update, name='session_update'),
    path('<int:pk>/delete/',
         views.training_session_delete, name='session_delete'),
]
