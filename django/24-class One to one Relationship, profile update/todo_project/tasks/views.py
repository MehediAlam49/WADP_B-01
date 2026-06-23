from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from tasks.models import *
from tasks.forms import TaskForm,ProfileForm

# Create your views here.

def register_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')
        
        if password==conf_password:
            CustomUserInfoModel.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password
            )
            return redirect('login_page')
    return render(request, 'register_page.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

#Home
def home(request):
    return render(request, 'home.html')

#Task
def task_list(request):
    task_data= TaskModel.objects.filter(created_by=request.user)

    context={
        'task_data':task_data
    }
    return render(request, 'task_list.html',context)

def add_task(request):
    #--to add data in database
    if request.method=='POST':
        form_data=TaskForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.save()
            return redirect('task_list')

    
    #--to show form in html page
    form_data=TaskForm()
    context={
        'form_data':form_data,
        'title_form':'Add Task Page',
        'submit_btn':'add Task'
    }
    return render(request, 'master/base_form.html',context)

def edit_task(request, id):
    task_data=get_object_or_404(TaskModel,id=id)
    if request.method=='POST':
        form_data=TaskForm(request.POST, instance=task_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.save()
            return redirect(task_list)
    
    form_data=TaskForm(instance=task_data)
    context={
        'form_data':form_data,
        'title_form':'Edit Task Page',
        'submit_btn':'Edit Task'
    }
    return render(request, 'master/base_form.html',context)



def view_task(request, id):
    task_data=get_object_or_404(TaskModel,id=id)
    
    context={
        'task_data':task_data
    }
    return render(request, 'view_task.html',context)

def delete_task(request,id):
    task_data=get_object_or_404(TaskModel,id=id)
    task_data.delete()
    return redirect('task_list')


def profile_page(request):
    return render(request, 'profile.html')


def update_profile(request):
    current_user=request.user
    try:
        # use get method
        profile_data=get_object_or_404(profileModel,user=current_user)
        
        #use related name
        #profile_data=current_user.user_profile
    except:
        profile_data=None
        
    if request.method=='POST':
        form_data=ProfileForm(request.POST, request.FILES, instance=profile_data)
        if form_data.is_valid:
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            return redirect('profile_page')
    
    #--to show the form in html page
    form_data=ProfileForm(instance=profile_data)
    
    context={
        'form_data':form_data,
        'title_form':'Update Profile',
        'submit_btn':'Update'
    }
    return render(request, 'master/base_form.html',context)