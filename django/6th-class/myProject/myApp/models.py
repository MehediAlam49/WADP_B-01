from django.db import models

# Create your models here.
class studentModel(models.Model):
    FirstName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=50,null=True)
    Department = models.CharField(max_length=50,null=True)
    City = models.CharField(max_length=50,null=True)

    # def __str__(self):
    #     return self.FirstName+"-"+self.LastName+"-"+ self.Department
    
class teacherModel(models.Model):
    teacherName = models.CharField(max_length=50)
    teacherid = models.CharField(max_length=50)
    teacherType = models.CharField(max_length=50)

    def __str__(self):
        return self.teacherName+"-"+self.teacherid+"-"+self.teacherType