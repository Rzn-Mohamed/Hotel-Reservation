from django.urls import path
from . import views

urlpatterns = [
  path("managerregister/", views.manager_register, name="manager-signup"),
  path('managerlog/', views.manager_login, name='manager-login'),
  path('managerdash/', views.manager_dash, name='manager-dash'),
  path('employee/', views.manager_employee, name='manager-employee'),
  path('addemployee/', views.Add_employee, name='manager-addemployee'),
  path('editemployee/<int:employee_id>', views.edit_employee, name='manager-Editemployee'),
  path('deleteemployee/<int:id_employee>', views.delete_employee, name='deleteemployee'),
  path("reservations/", views.reservations, name="manager-res"),
  path("facture/<int:reservation_id>/", views.facture, name="facture"),
  path('delete-reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
  path('edit-reservation/<int:reservation_id>/', views.edit_reservation, name='edit-reservation'),
  path('room/', views.manager_room, name='manager-room'),
  path('addroom/', views.addroom, name='addroom'),
  path("roomdetails/<int:room_id>/", views.roomdetails, name="roomdetails"),
  path("editroom/<int:room_id>/", views.editroom, name="editroom"),
  path("deleteroom/<int:room_id>/", views.deleteroom, name="deleteroom"),
  path("clientlist/", views.clientList, name="clientlist"),
  path('managersettings/', views.manager_settings, name='manager-settings'),
  path('managereditsettings/', views.manager_update, name='manager-editsettings'),
  path("delete_confirmation/", views.delete_confirmation, name="delete_confirmation"),
  #----------------client----------------#
  path("clientsignup/", views.client_signup, name="client-signup"),
  path("clientlog/", views.client_login, name="client-login"),
  path("clientdash/", views.client_dash, name="client-dash"),
  path("clientres/", views.reservation_history, name="client-res"),
  path("",views.landing,name="landingpage"),
  path("clientroom",views.client_room,name="clientroom"),
  path("clientAddreservation/<int:room_id>",views.client_reservation,name="client-Addreservation"),
  path("clientAddreservation/clientAddreservationForm/<int:room_id>",views.clientAddreservationForm,name="clientAddreservationForm"),
  path('clientsettings/', views.client_settings, name='client-settings'),
  path('clienteditsettings/', views.client_update, name='client-editsettings'),
  path('client_deleteconfirmation/', views.delete_confirmation, name='client-deleteconfirmation'),
  path('logout/', views.logout_view_client, name='logout'),

]