from django.db import models

# Create your models here.
class resumeModel(models.Model):
    ProfilePicture=models.ImageField(upload_to='static/profile')
    FullName=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    CareerObjective=models.TextField()
    Skills=models.CharField(max_length=100)
    Certification=models.CharField(max_length=100)
    Projects=models.CharField(max_length=100)
    References=models.CharField(max_length=100)

class educationModel(models.Model):
    Degree=models.CharField(max_length=100)
    Institution=models.CharField(max_length=100)
    GraduationYear=models.CharField(max_length=100)


class workModel(models.Model):
    Company=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    StartDate=models.CharField(max_length=100)
    endDate=models.CharField(max_length=100)