from django.shortcuts import render
from myApp.models import studentModel,teacherModel

def student(request):
    student= studentModel.objects.all()
    stuDic ={
        'stuData': student
    }
    return render(request, 'studentPage.html', stuDic)

def addStudent(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        depatrment = request.POST.get('department')
        City = request.POST.get('city')

        student = studentModel(
            FirstName=fname,
            LastName=lname,
            Department=depatrment,
            City=City,
            
        )
        student.save()
        
    return render(request, 'addStudent.html')

def teacher(request):
    teacher = teacherModel.objects.all()
    teacherDic={
        'teacherData':teacher
    }
    return render(request, 'teacherPage.html',teacherDic)