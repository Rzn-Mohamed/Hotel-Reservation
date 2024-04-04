# authentication.py
from django.contrib.auth.backends import ModelBackend
from .models import Manager, Client

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        
        manager_user = Manager.objects.filter(username=username).first()
        client_user = Client.objects.filter(username=username).first()

        if manager_user and manager_user.check_password(password):
            return manager_user
        elif client_user and client_user.check_password(password):
            return client_user
        else:
            return None
