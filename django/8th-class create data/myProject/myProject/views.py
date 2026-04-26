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
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dept=request.POST.get('department')
        city=request.POST.get('city')

        student=studentModel(
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
