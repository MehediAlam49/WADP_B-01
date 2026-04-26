from django.shortcuts import render, redirect
from myApp.models import *

def student(request):
    student=studentModel.objects.all()
    stuDic={
        'stuData':student
    }
    return render(request, 'student.html',stuDic)


def addStudent(request):
    if request.method=='POST':
        profilePicture=request.FILES.get('profilePicture')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dept=request.POST.get('department')
        city=request.POST.get('city')

        student=studentModel(
            ProfilePicture=profilePicture,
            FirstName=fname,
            LastName=lname,
            Department=dept,
            City=city,
        )
        student.save()
        return redirect('student')
    return render(request, 'addStudent.html')


def deleteStudent(request,myid):
    dltStudent=studentModel.objects.get(id=myid)
    dltStudent.delete()
    return redirect('student')

def editStudent(request,myid):
    student=studentModel.objects.get(id=myid)

    if request.method=='POST':
        student.FirstName=request.POST.get('firstname')
        student.LastName=request.POST.get('lastname')
        student.Department=request.POST.get('department')
        student.City=request.POST.get('city')

        if request.FILES.get('profilePicture'):
            student.ProfilePicture=request.FILES.get('profilePicture')

        student.save()
        return redirect('student')


    context={
        'student':student
    }
    return render(request, 'editStudent.html',context)

def viewStudent(request,myid):

    student=studentModel.objects.get(id=myid)

    context={
        'student':student
    }
    return render(request, 'viewStudent.html',context)
