from django.shortcuts import render,redirect
from bookApp.models import *

def book(request):
    book=bookModel.objects.all()
    context={
        'book':book
    }
    return render(request, 'book.html',context)


def addBook(request):
    if request.method=='POST':
        bookName=request.POST.get('bookName')
        author=request.POST.get('author')
        publishDate=request.POST.get('publishDate')
        
        book=bookModel(
            BookName=bookName,
            Author=author,
            Publish_date=publishDate,
        )
        book.save()
        return redirect('book')
    return render(request, 'addBook.html')