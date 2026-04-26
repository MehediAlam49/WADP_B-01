from django.shortcuts import render,redirect
from authApp.models import *

def signup(request):
    if request.method=='POST':
        userType=request.POST.get('userType')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')
        gender=request.POST.get('gender')
        education=request.POST.get('education')

        if(password==confirmPassword):
            user=custom_model.objects.create_user(username=username, password=confirmPassword)
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.Gender=gender
            user.UserType=userType
            user.Education=education

            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')