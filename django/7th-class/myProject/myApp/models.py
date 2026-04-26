from django.db import models

# Create your models here.
class studentModel(models.Model):
    FirstName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=80)
    Department= models.CharField(max_length=80)
    City= models.CharField(max_length=80)

    def __str__(self):
        return self.FirstName
    
class teacherModel(models.Model):
    FirstName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=80)
    Department= models.CharField(max_length=80)
    City= models.CharField(max_length=80)

    def __str__(self):
        return self.FirstName