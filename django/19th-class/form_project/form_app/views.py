from django.shortcuts import render,redirect
from form_app.models import *
from form_app.forms import *

# Create your views here.
def product_list(request):
    product_data=ProductModel.objects.all()

    context={
        'product_data':product_data
    }
    return render(request, 'product_list.html',context)


def add_product(request):
    #---to save data in database
    if request.method=='POST':
        form_data=productForm(request.POST, request.FILES)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_amount=data.product_price * data.product_qty
            data.save()
            return redirect('product_list')
    
    #---to show form in html page
    form_data=productForm()
    context={
        'form_data':form_data
    }
    
    return render(request, 'add_product.html',context)


def edit_product(request, p_id):
    product_data=ProductModel.objects.get(id=p_id)
    
    #--to save data in database
    if request.method=='POST':
        form_data=productForm(request.POST,request.FILES, instance=product_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.total_amount=data.product_price * data.product_qty
            data.save()
            return redirect('product_list')
    
    #--to show the form in html page
    form_data=productForm(instance=product_data)
    context={
        'form_data': form_data
    }
    return render(request, 'edit_product.html',context)

def view_product(request, p_id):
    product_data=ProductModel.objects.get(id=p_id)
    context={
        'product_data':product_data
    }
    return render(request, 'product_view.html',context)