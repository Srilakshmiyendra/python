from django.shortcuts import render,HttpResponse,redirect
from .models import register
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def Register(request):
    if request.method == 'POST':
        Name = request.POST["Name"]
        Email = request.POST["Email"]
        Password = request.POST["Password"]
        Confirm_Password = request.POST["Confirm_Password"]
        if Password == Confirm_Password:
         registers = register(Name=Name,Email=Email,Password=Password,Confirm_Password=Confirm_Password)
         registers.save()
         messages.success(request, 'Registration successful! You can now log in.')

    return render(request,'register.html')    

def login_page(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('Email')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('welcome')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
 
def welcome(request):
     return render(request, 'welcome.html')
 
