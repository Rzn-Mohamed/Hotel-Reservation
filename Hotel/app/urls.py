from django.urls import path
from . import views

urlpatterns = [
  path('managerlog/', views.manager_login, name='login-in'),
  path('managerdash/', views.manager_dash, name='manager-dash'),
]