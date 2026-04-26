
from django.shortcuts import render

def home(request):
    tableData={
        'companyName':'google',
        'contact': '01772050842',
        'country':'USA',
    }
    return render(request, "index.html", tableData)

def about(request):
    return render(request, "about.html")
    
