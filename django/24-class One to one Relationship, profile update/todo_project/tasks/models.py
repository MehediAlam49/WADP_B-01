from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserInfoModel(AbstractUser):
    full_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.username}'
    
    

class TaskModel(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)

    STATUS=[
        ('Pending','Pending'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    ]
    status=models.CharField(choices=STATUS,null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    created_by=models.ForeignKey(CustomUserInfoModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'
    
    
class profileModel(models.Model):
    user=models.OneToOneField(CustomUserInfoModel, on_delete=models.CASCADE, related_name='user_profile')
    address=models.TextField(null=True)
    phone=models.CharField(max_length=20,null=True)
    profile_img=models.ImageField(upload_to='media/profile-img',null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'