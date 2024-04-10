from django.urls import path
from . import views

urlpatterns = [
  path('managerlog/', views.manager_login, name='manager-login'),
  path('managerdash/', views.manager_dash, name='manager-dash'),
  path('employee/', views.manager_employee, name='manager-employee'),
  path('Addemployee/', views.Add_employee, name='manager-addemployee'),
  path('deleteemployee/<int:id_employee>', views.delete_employee, name='deleteemployee'),
  path('clientlog/', views.manager_dash, name='client-login'),
  path('clientdash/', views.manager_dash, name='client-dash'),
  path("clientsignup/", views.client_signup, name="client-signup"),
  path("reservations/", views.reservations, name="manager-res"),
  path("facture/<int:reservation_id>/", views.facture, name="facture"),
  path('room/', views.manager_room, name='manager-room'),
  path('addroom/', views.addroom, name='addroom'),
  

]