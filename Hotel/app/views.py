from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User , auth 
from .models import Manager , Client , Employee , Reservation ,  Room
from django.core.paginator import Paginator
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
    return render(request , 'app/manager/manager_dash.html')




#-----------------client----------------#
def client_login(request):
    if request.method != 'POST':
        return render(request , 'app/client_login.html')
    user = authenticate(request , username=request.POST['username'] , password=request.POST['password'])
    if user is not None:
        auth.login(request , user)
    return redirect('client-dash')

def client_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']  
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password != password2:
            return render(request, 'app/client/client_signup.html', {'error': 'Passwords do not match'})

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        user.save()

        return redirect('client-login')

    return render(request, 'app/client/client_login.html')

#----------reservations---------
def reservations(request):
    reservations = Reservation.getAllReservations()
   
    return render(request, 'app/manager/manager_res.html', {'reservations': reservations})


#---------Employee----------------

def manager_employee(request):
    employees = Employee.objects.all()  # Assuming you have a model named Employee
    paginator = Paginator(employees, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/manager/manager_employee.html', {'page_obj': page_obj})