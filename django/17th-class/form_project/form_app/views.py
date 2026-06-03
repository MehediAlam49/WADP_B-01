from django.shortcuts import render,redirect
from form_app.forms import *
from form_app.models import *

# Create your views here.
def product_list(request):
    product_data=productModel.objects.all()
    
    context={
        'product_data':product_data
    }
    return render(request, 'product_list.html',context)

def add_product(request):
    #to save the form data in database
    if request.method=='POST':
        form_data=productForm(request.POST,request.FILES)
        if  form_data.is_valid():
            form_data.save()
            return redirect('product_list')
        
    
    #to show the html form
    form_data=productForm()
    context={
        'form_data':form_data
    }
    return render(request, 'add_product.html',context)