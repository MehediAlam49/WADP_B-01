from django.shortcuts import render,redirect
from myApp.models import *

def student(request):
    student = studentModel.objects.all()

    studentDic ={
        'stuData': student
    }
    return render(request, 'studentPage.html',studentDic)

def addStudent(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')

        student=studentModel(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        student.save()
        return redirect('studentPage')
    return render(request, 'addStudent.html')



def teacher(request):
    teacher = teacherModel.objects.all()

    teacherDic ={
        'teacherData': teacher
    }
    return render(request, 'teacherPage.html',teacherDic)

def addTeacher(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        department=request.POST.get('department')
        city=request.POST.get('city')

        teacher=teacherModel(
            FirstName=fname,
            LastName=lname,
            Department=department,
            City=city,
        )
        teacher.save()
        return redirect('teacherPage')
    return render(request, 'addTeacher.html')


