from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from tasks.models import *
from tasks.forms import productForm,ProfileForm

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
@login_required
def home(request):
    return render(request, 'home.html')

#Product
@login_required
def product_list(request):
    try:
        product_data= ProductModel.objects.filter(created_by=request.user)
    except:
        product_data=None

    context={
        'product_data':product_data
    }
    return render(request, 'product_list.html',context)
@login_required
def add_product(request):
    current_user=request.user
    #--to add data in database
    if request.method=='POST':
        form_data=productForm(request.POST, request.FILES)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=current_user
            data.total_amount= data.price * data.qty
            data.save()
            return redirect('product_list')

    
    #--to show form in html page
    form_data=productForm()
    context={
        'form_data':form_data,
        'title_form':'Add Product Page',
        'submit_btn':'add Product'
    }
    return render(request, 'master/base_form.html',context)
@login_required
def edit_product(request, id):
    product_data=get_object_or_404(ProductModel,id=id)
    if request.method=='POST':
        form_data=productForm(request.POST, instance=product_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.save()
            return redirect(product_list)
    
    form_data=productForm(instance=product_data)
    context={
        'form_data':form_data,
        'title_form':'Edit Product Page',
        'submit_btn':'Edit Product'
    }
    return render(request, 'master/base_form.html',context)


@login_required
def view_product(request, id):
    product_data=get_object_or_404(ProductModel,id=id)
    
    context={
        'product_data':product_data
    }
    return render(request, 'view_product.html',context)
@login_required
def delete_product(request,id):
    product_data=get_object_or_404(ProductModel,id=id)
    product_data.delete()
    return redirect('tproductlist')

@login_required
def profile_page(request):
    return render(request, 'profile.html')

@login_required
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