from django.http import HttpResponse
from django.shortcuts import render,redirect

def homepage(request):
    return HttpResponse("welcome to django website!")

def about(request):
    return HttpResponse("This is about page!")
