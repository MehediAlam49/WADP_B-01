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

def editStudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    stuDic={
        'student':student
    }
    return render(request, 'editStudent.html',stuDic)

def updateStudent(request):
    if request.method=='POST':
        myid=request.POST.get('stuID')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        dept=request.POST.get('department')
        city=request.POST.get('city')

        student=studentModel(
            id=myid,
            FirstName=fname,
            LastName=lname,
            Department=dept,
            City=city,
        )
        student.save()
    return redirect('student')


def viewStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    stuDic={
        'student':student
    }
    return render(request, 'viewStudent.html',stuDic)

def teacher(request):
    teacher=teacherModel.objects.all()
    teacherDic={
        'teacher':teacher
    }
    return render(request, 'teacher.html',teacherDic)

def management(request):
    management=managementModel.objects.all()
    managementDic={
        'management':management
    }
    return render(request, 'management.html',managementDic)

def allData(request):
    student=studentModel.objects.all()
    teacher=teacherModel.objects.all()
    management=managementModel.objects.all()
    allData={
        'student':student,
        'teacher':teacher,
        'management':management
    }
    return render(request, 'allData.html',allData)