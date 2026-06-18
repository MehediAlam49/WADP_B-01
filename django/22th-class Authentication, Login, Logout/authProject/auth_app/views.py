from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')
        
        if password==conf_password:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('login_page')
        else:
            print('Both password are not match')
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('login_page')

@login_required
def home(request):
    return render(request, 'home.html')