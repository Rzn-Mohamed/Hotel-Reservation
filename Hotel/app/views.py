from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User , auth 
from .models import Manager , Client , Employee , Reservation ,  Room,Personne
from django.core.paginator import Paginator
from django.http import HttpResponse , JsonResponse

# Create your views here.

#-----------------manager----------------#
def manager_login(request):
    if request.method != 'POST':
        return render(request , 'app/manager/manager_login.html')
    user = authenticate(request , username=request.POST['username'] , password=request.POST['password'])
    if user is not None:
        auth.login(request , user)
    return redirect('manager-dash')

def manager_dash(request):
    total_employee=Employee.TotalEmployee()
    total_room=Room.TotalRoom()
    total_reservation=Reservation.TotalReservation()
    
   
    
    labels=[]
    data=[]
    
    # queryset=Reservation.objects.order_by('checkIn')
    queryset=Reservation.objects.all()
    # print(queryset)
    month1 = month2 = month3 = month4 = month5 = month6 = month7 = month8 = month9 = month10 = month11 = month12 = 0
    

    for r in queryset:
        month = r.checkIn.month
        match month:
            case 1:
                month1 += 1
            case 2:
                month2 += 1
            case 3:
                month3 += 1
            case 4:
                month4 += 1
            case 5:
                month5 += 1
            case 6:
                month6 += 1
            case 7:
                month7 += 1
            case 8:
                month8 += 1
            case 9:
                month9 += 1
            case 10:
                month10 += 1
            case 11:
                month11 += 1
            case 12:
                month12 += 1

    mois=[month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12]
    for i in mois:
        data.append(i)
              
   
        
    context ={
        'total_employee': total_employee,
        'total_room': total_room,
        'total_reservation': total_reservation,
        "labels":labels,
        "data":data
    }
        
    return render(request , 'app/manager/manager_dash.html',context)






#----------reservations---------
def reservations(request):
    reservations = Reservation.getAllReservations()
   
    return render(request, 'app/manager/manager_res.html', {'reservations': reservations})


#---------Employee----------------

def manager_employee(request):
    employees = Employee.objects.all()  
    paginator = Paginator(employees, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/manager/manager_employee.html', {'page_obj': page_obj})


def delete_employee(request,id_employee):
    Employee.deleteEmployee(id_employee)
    return redirect('manager-employee')



def Add_employee(request):
        if request.method == 'POST':
            name = request.POST.get('fullname')
            address = request.POST.get('address')
            phone_num = request.POST.get('phone_num')

        if request.FILES:
            image = request.FILES["imageEmployee"]

            employee=Employee(fullname=name,address=address,
            pic=image,phone_num=phone_num )
            employee.save()
            
            return redirect("manager-employee")  # Add return statement here

        return HttpResponse("Invalid request") 
    


def edit_employee(request,employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        if request.FILES:
            image = request.FILES["imageEmployee"]

        employee.fullname = request.POST['fullname']
        employee.address = request.POST['address']
        employee.phone_num = request.POST['phone_num']
        employee.pic = image
        employee.save()
        return redirect('manager-employee')
   
   

    

#--------------facture----------------

def facture(request , reservation_id):
    reservation = Reservation.objects.get(id = reservation_id)
    
    return render(request , 'app/manager/facture.html' , {'reservation':reservation})


#------------ROOM-----------
def manager_room(request):
    room = Room.objects.all()  
    paginator = Paginator(room, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/manager/manager_room.html', {'page_obj': page_obj})



def addroom(request):
    if request.method == 'POST':
        num = request.POST['num'] 
        description = request.POST['description']
        type = request.POST['type']
        price = request.POST['price']
        
        image = request.FILES.get('image')
        
        room = Room(num=num, description=description, type=type, price=price, image=image)
        
        room.save()
        
        return redirect('manager-room')
    return render(request, 'app/manager/addroom.html')



def roomdetails(request, room_id):
    
    room = get_object_or_404(Room, id=room_id)

    return render(request, 'app/manager/roomdetails.html', {'room': room})

def editroom(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        room.num = request.POST['num']
        room.description = request.POST['description']
        room.type = request.POST['type']
        room.price = request.POST['price']
        
        image = request.FILES.get('image')
        if image:
            room.image = image
        
        room.save()
        return redirect('manager-room')
    else:
        return render(request, 'app/manager/editroom.html', {'room': room})

def deleteroom(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    room.delete()
    return redirect('manager-room')


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return JsonResponse({'message': 'Reservation deleted successfully'})

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        reservation.status = request.POST['status']
        reservation.checkIn = request.POST['check-in']
        reservation.checkOut = request.POST['check-out']
        reservation.save()
        return redirect('manager-res')
    return render(request, 'app/manager/edit_reservation.html', {'reservation': reservation})





#-----------------client----------------#
def client_login(request):
    if request.method != 'POST':
        return render(request , 'app/client/client_login.html')
    client = authenticate(request , username=request.POST['username'] , password=request.POST['password'])
    if client is not None:
        auth.login(request , client)
    return redirect('client-dash')

from django.contrib.auth.models import User
from .models import Client

def client_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']  
        password2 = request.POST['password2']
        fullname = request.POST['fullname']
        address = request.POST['address']
        phone_num = request.POST['phone_num']
        
        # Check if passwords match
        if password != password2:
            return render(request, 'app/client/client_signup.html', {'error': 'Passwords do not match'})

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Create the client associated with the user
        client = Client.objects.create(user=user, fullname=fullname, address=address, phone_num=phone_num)
        
        
        return redirect('client-login')

    return render(request, 'app/client/client_signup.html')



def client_dash(request):
    return render(request , 'app/client/client_dash.html')

def reservation_history(request):
    client = request.user.client
    reservations = Reservation.objects.filter(client=client)
    return render(request, 'app/client/client_res.html', {'reservations': reservations})