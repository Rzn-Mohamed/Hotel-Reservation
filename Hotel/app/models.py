from django.db import models
from django.contrib.auth.models import AbstractUser , User

class Personne(models.Model):
    user = models.OneToOneField(User , null = True , on_delete = models.CASCADE)
    fullname = models.CharField(null = True , max_length = 255)
    address = models.CharField(null = True , max_length = 255)
    phone_num = models.CharField(null = True, max_length = 255)
    pic = models.ImageField(upload_to = 'profile_pics' , null = True , blank = True)
    class Meta:
        abstract = True
    
    #nshufo hadshi ash m7tajino wlala
    @classmethod
    def create(cls , user , fullname , address , phone_num):
        return cls.objects.create(user = user , fullname = fullname , address = address , phone_num = phone_num)

    @classmethod
    def update(cls , user , fullname , address , phone_num):
        return cls.objects.filter(user = user).update(fullname = fullname , address = address , phone_num = phone_num)
    
    @classmethod
    def delete(cls , user):
        return cls.objects.filter(user = user).delete()

class Manager(Personne):
    is_manager = models.BooleanField(default = True)
    pass
    
class Client(Personne):
    is_client = models.BooleanField(default = True)
    pass