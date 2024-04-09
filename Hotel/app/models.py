from django.db import models
from django.contrib.auth.models import AbstractUser , User
from datetime import timedelta

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

class Employee(Personne):
    is_employee = models.BooleanField(default = True)
    @classmethod
    def getAllEmployees(cls):
        return cls.objects.all()
    
    @classmethod
    def deleteEmployee(cls, Employee_id):
        return cls.objects.filter(id=Employee_id).delete()




#-----------------Room-----------------

class Room(models.Model):
    TYPES = [
        ('single', 'Single'),
        ('queen', 'Queen'),
        ('king', 'King')
    ]
    num = models.IntegerField()
    type = models.CharField(max_length=50, choices=TYPES)
    description = models.TextField()
    is_reserved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    price = models.IntegerField(default=0)
    # night_price = models.IntegerField()
    
    @classmethod
    def createRoom(cls, num, type, description):
        return cls.objects.create(num=num, type=type, description=description)

    @classmethod
    def updateRoom(cls, num, type, description):
        return cls.objects.filter(num=num).update(type=type, description=description)

    @classmethod
    def deleteRoom(cls, num):
        return cls.objects.filter(num=num).delete()
    
    @classmethod
    def getAllRooms(cls):
        return cls.objects.all()
    
    @classmethod 
    def updateState(cls, num, state):
        return cls.objects.filter(num=num).update(is_reserved=state)
    
    def getPrice(self):
        return self.price

    
    
    
#-----------------Reservations-----------------


class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)  # Change to ManyToManyField
    checkIn = models.DateField()
    checkOut = models.DateField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=50, choices=STATUS)

    @classmethod
    def getAllReservations(cls):
        return cls.objects.all()

    @classmethod
    def createReservation(cls, client, rooms, checkIn, checkOut):  # Modify to accept multiple rooms
        total_price = 0
        for room in rooms:
            room_price = room.getPrice(room)
            duration = (checkOut - checkIn).days
            total_price += room_price * duration

        reservation = cls.objects.create(client=client, checkIn=checkIn, checkOut=checkOut,
                                        totalPrice=total_price, status='pending')
        reservation.rooms.add(*rooms)  # Add all rooms to the reservation
        return reservation
    
        
    
    @classmethod
    def updateStatus(cls, reservation_id, status):
        return cls.objects.filter(id=reservation_id).update(status=status)

    @classmethod
    def deleteReservation(cls, reservation_id):
        return cls.objects.filter(id=reservation_id).delete()