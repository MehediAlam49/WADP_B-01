from django.shortcuts import render

def homepage(request):
    tableData = {
        'companyName':'Google',
        'contact':'01772050842',
        'country':'USA',
    }
    return render(request, 'home.html', tableData)
def aboutpage(request):
    return render(request, 'about.html')
def newspage(request):
    return render(request, 'news.html')
def contactpage(request):
    return render(request, 'contact.html')