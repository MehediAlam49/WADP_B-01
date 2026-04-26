from django.db import models

# Create your models here.
class studentModel(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName
    
class teacherModel(models.Model):
    FirstName=models.CharField(max_length=100, null=True)
    LastName=models.CharField(max_length=100, null=True)
    Department=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.FirstName
    
class managementModel(models.Model):
    Name=models.CharField(max_length=100, null=True)
    Designation=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name