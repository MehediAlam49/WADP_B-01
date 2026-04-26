from django.shortcuts import render

def home(request):
    tableData = {
        'companyName': 'Google',
        'contact': '01772050842',
        'country': 'USA',

        'companyName1': 'Amazon',
        'contact1': '01572050842',
        'country1': 'US',
    }
    return render(request, 'home.html', tableData)
def about(request):
    return render(request, 'about.html')
def news(request):
    return render(request, 'news.html')
def contact(request):
    return render(request, 'contact.html')