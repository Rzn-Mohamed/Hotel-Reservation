from django.urls import path
from . import views

urlpatterns = [
  path('managerlog/', views.manager_login, name='manager-login'),
  path('managerdash/', views.manager_dash, name='manager-dash'),
  path('employee/', views.manager_employee, name='manager-employee'),
  path('clientlog/', views.manager_dash, name='client-login'),
  path('clientdash/', views.manager_dash, name='client-dash'),
  path("clientsignup/", views.client_signup, name="client-signup"),
]