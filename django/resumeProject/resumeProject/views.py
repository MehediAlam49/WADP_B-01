from django.shortcuts import render,redirect
from resumeApp.models import *
def home(request):
    resumeData= resumeModel.objects.all()
    educationData= educationModel.objects.all()
    workData= workModel.objects.all()
    
    resumeDic={
        'resumeData':resumeData,
        'educationData':educationData,
        'workData':workData
    }
    return render(request, 'resume.html',resumeDic)

def addResume(request):
    if request.method=='POST':
        profilePicture=request.FILES.get('profilePicture')
        fullName=request.POST.get('fullName')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        careerObjective=request.POST.get('careerObjective')
        skills=request.POST.get('skills')
        cerfification=request.POST.get('certification')
        projects=request.POST.get('projects')
        references=request.POST.get('references')


        degree=request.POST.get('degree')
        institution=request.POST.get('institution')
        graduationYear=request.POST.get('graduationYear')


        company=request.POST.get('company')
        position=request.POST.get('position')
        startDate=request.POST.get('startDate')
        endDate=request.POST.get('endDate')

        resumeData=resumeModel(
            ProfilePicture=profilePicture,
            FullName=fullName,
            Address=address,
            Phone=phone,
            Email=email,
            CareerObjective=careerObjective,
            Skills=skills,
            Certification=cerfification,
            Projects=projects,
            References=references,
        )

        educationData=educationModel(
            Degree=degree,
            Institution=institution,
            GraduationYear=graduationYear,
        )

        workData=workModel(
            Company=company,
            Position=position,
            StartDate=startDate,
            endDate=endDate,
        )

        resumeData.save()
        educationData.save()
        workData.save()
        return redirect('home')
    return render(request, 'addResume.html')


def editResume(request,myid):
    resumeData=resumeModel.objects.get(id=myid)
    educationData=educationModel.objects.get(id=myid)
    workData=workModel.objects.get(id=myid)

    resumeDic={
        'resumeData':resumeData,
        'educationData':educationData,
        'workData':workData,
    }

    return render(request, 'editResume.html', resumeDic)

def updateResume(request):
    if request.method=='POST':
        resumeID=request.POST.get('resumeID')


        resumeData=resumeModel.objects.get(id=resumeID)
        educationData=educationModel.objects.get(id=resumeID)
        workData=workModel.objects.get(id=resumeID)

        resumeData.FullName=request.POST.get('fullName')
        resumeData.Address=request.POST.get('address')
        resumeData.Phone=request.POST.get('phone')
        resumeData.Email=request.POST.get('email')
        resumeData.CareerObjective=request.POST.get('careerObjective')
        resumeData.Skills=request.POST.get('skills'),
        resumeData.Certification=request.POST.get('certification')
        resumeData.Projects=request.POST.get('projects')
        resumeData.References=request.POST.get('references')
    

        if request.FILES.get('profilePicture'):
            resumeData.ProfilePicture =request.FILES.get('profilePicture')

        educationData.Degree=request.POST.get('degree')
        educationData.Institution=request.POST.get('institution')
        educationData.GraduationYear=request.POST.get('graduationYear')


        workData.Company=request.POST.get('company')
        workData.Position=request.POST.get('position')
        workData.StartDate=request.POST.get('startDate')
        workData.endDate=request.POST.get('endDate')

        resumeData.save()
        educationData.save()
        workData.save()
    return redirect('home')

def deleteResume(request,myid):
    resumeData=resumeModel.objects.get(id=myid)
    educationData=educationModel.objects.get(id=myid)
    workData=workModel.objects.get(id=myid)
    
    resumeData.delete()
    educationData.delete()
    workData.delete()
    return redirect('home')


def viewResume(request, myid):
    resumeData= resumeModel.objects.get(id=myid)
    educationData= educationModel.objects.get(id=myid)
    workData= workModel.objects.get(id=myid)
    
    context={
        'resumeData':resumeData,
        'educationData':educationData,
        'workData':workData
    }
    return render(request, 'viewResume.html',context)